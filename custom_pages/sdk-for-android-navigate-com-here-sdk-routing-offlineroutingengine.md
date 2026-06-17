---
title: "OfflineRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- OfflineRoutingEngine.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.OfflineRoutingEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">OfflineRoutingEngine</span>
<span class="extends-implements">extends <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a>
implements <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></span></div>
<div class="block"><p>Use this class to calculate a route offline from A to B with
 a number of waypoints in between.
 </p><p>Route calculation is done asynchronously, and requires map data that is
 available offline. This can be temporarily cached map data or downloaded
 offline map data stored in the persisted storage via <code>MapDownloader</code>.
 Note that when using the cache there is a risk of missing data and this may
 reduce the overall quality of the route or can result in a
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error.
 </p><p>The resulting route contains various information such as the polyline,
 route length in meters, estimated time to traverse along the route
 and maneuver data, but it does not contain traffic information.
 </p><p>Unlike the <code>RoutingEngine</code> (which requires an online connection), this engine
 allows to use an unlimited number of waypoints.
 </p><p>As an alternative to this engine, consider to use the <code>RoutingEngine</code> for online
 route calculations to get fresher traffic, maneuver, route handles and street
 information, and to use a more elaborate algorithms to calculate the fastest route.
 </p><p>For offline bus routing, enable "OFFLINE_BUS_ROUTING" as feature configuration.
 For more details, please look at <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>. If this feature is not
 enabled, the engine may not be able to find bus routes.
 </p><p><strong>Note:</strong> EV routing is available when calculating a route using the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>, by setting
 the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions#evOptions"><code>RoutingOptions.evOptions</code></a>.
 </p><p><strong>Note:</strong> Traffic related information is completely excluded.
 No historic traffic patterns are taking into consideration for the ETA.
 Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e.
 the road may pass through such road.
 Only seasonal road closures are considered based on the departure time, if given.
 Traffic information is only considered for online route calculation with the <code>RoutingEngine</code>.
 </p><p><strong>Note:</strong> Route handles produced by this engine are not compatible with those created by
 the <code>RoutingEngine</code>. Importing, refreshing, or returning to a route via a route
 handle is supported only when the route was calculated with the same engine. However,
 this engine supports returning to a route calculated with the <code>RoutingEngine</code> when
 the route object is provided.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E()">OfflineRoutingEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">OfflineRoutingEngine</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of OfflineRoutingEngine.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.OfflineRoutingEngineOptions)">OfflineRoutingEngine</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlineroutingengineoptions" title="class in com.here.sdk.routing">OfflineRoutingEngineOptions</a> options)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of OfflineRoutingEngine.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab6" onclick="show('method-summary-table', 'method-summary-table-tab6', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Deprecated Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates a route from one point to another,
 passing through the given waypoints in the given order.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Cancels pending requests and closes the background worker thread.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#getTrafficDataProvider()">getTrafficDataProvider</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the traffic data provider that provides internal traffic information considering in routing.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously recreates a route from the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#refreshRoute(com.here.sdk.routing.RefreshRouteParameters,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">refreshRoute</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a> refreshRouteParameters,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously refreshes a previously calculated route from the provided <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">returnToRoute</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> route,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates a new route that leads back to the original route.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#setInternalOption(java.lang.String,java.lang.String)">setInternalOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This method sets internal options that controls offline route calculation behavior.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#setTrafficDataProvider(com.here.sdk.traffic.TrafficDataProvider)">setTrafficDataProvider</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets the traffic data provider that provides internal traffic information considering in routing.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>OfflineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OfflineRoutingEngine</span>()
                     throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>OfflineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OfflineRoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                     throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of OfflineRoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.OfflineRoutingEngineOptions)">
<h3>OfflineRoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">OfflineRoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-offlineroutingengineoptions" title="class in com.here.sdk.routing">OfflineRoutingEngineOptions</a> options)</span>
                     throws <span class="exceptions"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of OfflineRoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dd><code>options</code> - <p>Options to configure offline routing engine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="refreshRoute(com.here.sdk.routing.RefreshRouteParameters,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a> refreshRouteParameters,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>. The route shape from the new
 starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
 delays are updated.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>refreshRouteParameters</code> - <p>The parameters used to refresh the route</p></dd>
<dd><code>routingOptions</code> - <p>The options define the vehicle and route options used to calculate the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> method with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously recreates a route from the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e. refreshes a previously
 calculated route, with the specified <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>.
 </p><p>A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
 Therefore, the route handle is not meant to be persisted for a longer time.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>refreshRouteOptions</code> - <p>Options to import the route from handle.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously recreates a route from the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e. refreshes a previously
 calculated route, with the specified <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>.
 </p><p>A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
 Therefore, the route handle is not meant to be persisted for a longer time.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>options</code> - <p>Options to import the route from handle.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setInternalOption(java.lang.String,java.lang.String)">
<h3>setInternalOption</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setInternalOption</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>This method sets internal options that controls offline route calculation behavior.
 Unsupported options will be logged as warnings.
 Undocumented options can change their meaning without going through deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>Option name</p></dd>
<dd><code>value</code> - <p>New option value</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficDataProvider()">
<h3>getTrafficDataProvider</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></span> <span class="element-name">getTrafficDataProvider</span>()</div>
<div class="block"><p>Gets the traffic data provider that provides internal traffic information considering in routing.
 </p><p>If the traffic data provider is <code>null</code>, traffic is not considered in routing.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The traffic data provider that gets internal traffic information considering in routing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setTrafficDataProvider(com.here.sdk.traffic.TrafficDataProvider)">
<h3>setTrafficDataProvider</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTrafficDataProvider</span><wbr/><span class="parameters">(@Nullable
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a> value)</span></div>
<div class="block"><p>Sets the traffic data provider that provides internal traffic information considering in routing.
 </p><p>If the traffic data provider is <code>null</code>, traffic is not considered in routing.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The traffic data provider that gets internal traffic information considering in routing.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates a route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>options</code> - <p>Options describing routing options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a car route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>carOptions</code> - <p>Options specific for car route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a pedestrian route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>pedestrianOptions</code> - <p>Options specific for pedestrian route calculation, along with
     common route options. Note that <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for pedestrians and converted to
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a truck route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>truckOptions</code> - <p>Options specific for truck route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a scooter route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>scooterOptions</code> - <p>Options specific for scooter route calculation, along with
     common route options. Note that <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for scooters and converted to
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a bicycle route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>bicycleOptions</code> - <p>Options specific for bicycle route calculation, along with
     common route options. Note that <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for bicycles and converted to
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a taxi route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>taxiOptions</code> - <p>Options specific for taxi route calculation, along with
     common route options. Note that <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for taxis and converted to
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates an electric car route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>evCarOptions</code> - <p>Options specific for an electric car route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates an electic truck route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>evTruckOptions</code> - <p>Options specific for an electric truck route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a bus route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>busOptions</code> - <p>Options specific for a bus route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a private bus route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     </p><p>An <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>privateBusOptions</code> - <p>Options specific for a private bus route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">
<h3>returnToRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">returnToRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route" title="class in com.here.sdk.routing">Route</a> route,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates a new route that leads back to the original route. The part of
 the original route which was already traveled by the user is ignored.
 </p><p><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
 be ignored.
 Additionally, the following route options are ignored:
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routeoptions#alternatives"><code>RouteOptions.alternatives</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routeoptions#arrivalTime"><code>RouteOptions.arrivalTime</code></a>, and
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routeoptions#optimizationMode"><code>RouteOptions.optimizationMode</code></a>.
 Most route options are only applied to the newly calculated part back to the route.
 </p><p>An application may use this method to submit a new
 starting point for a previously calculated route. This method tries to avoid a costly
 route re-calculation as much as possible. In case returning to the route without
 re-calculation is not possible, a new route is calculated, while trying to salvage
 the previous route as much as possible. However, a completely new route
 containing no part of the previous route is possible, too.
 </p><p>Note that this function uses only a limited amount of map data around the new origin.
 Therefore, it may also work fine with temporarily cached map data. It may also copy some of the
 original route data into the new route.
 </p><p>A typical use case is to await at least 3 <code>RouteDeviation</code> events before calling this method.
 <ul>
<li>Or alternatively, wait at least 10 seconds after getting the first deviation event.</li>
<li>On top, the user experience can be improved by checking if the vehicle has moved at least
 50 meters since calling this method for the last time.</li>
<li>Optionally, it may make sense to verify if the vehicle was ever following the route by checking if
 <code>RouteDeviation.lastLocationOnRoute</code> is set.</li>
</ul>
</p><p>Note that deviation events are sent each time a deviation is detected, i.e. for each new location
 update, regardless if the location has changed or not.
 More information can be found in the Developer Guide in the "Handle route deviations" section.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">returnToRoute</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>route</code> - <p>A <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route" title="class in com.here.sdk.routing"><code>Route</code></a> calculated using the online or offline route engine. For the offline case, It
     should not contain an indoor <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-section" title="class in com.here.sdk.routing"><code>Section</code></a> as such routes will fail. For the online case, it
     should have <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.</p></dd>
<dd><code>startingPoint</code> - <p>The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
     type <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise, an <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a>
     error is generated.</p></dd>
<dd><code>lastTraveledSectionIndex</code> - <p>Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p></dd>
<dd><code>traveledDistanceOnLastSectionInMeters</code> - <p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="dispose()">
<h3>dispose</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()</div>
<div class="block"><p>Cancels pending requests and closes the background worker thread.
 <strong>Note:</strong> This method should be called from main thread.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface#dispose()">dispose</a></code> in interface <code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
