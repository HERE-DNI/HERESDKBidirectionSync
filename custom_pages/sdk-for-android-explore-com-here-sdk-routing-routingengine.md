---
title: "RoutingEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-routingengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoutingEngine.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.RoutingEngine</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoutingEngine</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></span></div>
<div class="block"><p>Use the RoutingEngine to calculate a route from A to B with
 a number of waypoints in between.
 Route calculation is done asynchronously and requires an
 online connection. The resulting route contains various
 information such as the polyline, route length in meters,
 estimated time to traverse along the route and maneuver data.
 <strong>Note:</strong> The engine does not support an unlimited number of waypoints.
 The limit is defined by the HERE backend services and may change. For now,
 the maximum number of waypoints should be below 200. This value may change
 and it is not guaranteed to be stable. If you need to support very large lists
 of waypoints, consider to import a route (see <code>importRoute()</code> method) or use
 the <code>OfflineRoutingEngine</code> which supports an unlimited number of waypoints.
 The <code>OfflineRoutingEngine</code> is only available for Navigate licence.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#%3Cinit%3E()">RoutingEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">RoutingEngine</a><wbr/>(<a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of RoutingEngine.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)">RoutingEngine</a><wbr/>(<a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of RoutingEngine.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#%3Cinit%3E(com.here.sdk.routing.RoutingConnectionSettings)">RoutingEngine</a><wbr/>(<a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of RoutingEngine.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates a route from one point to another,
 passing through the given waypoints in the given order.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 <a href="sdk-for-android-explore-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)">calculateTrafficOnRoute</a><wbr/>(<a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 double currentChargeInKilowattHours,
 <a href="sdk-for-android-explore-calculatetrafficonroutecallback" title="interface in com.here.sdk.routing">CalculateTrafficOnRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates the traffic along an EV car route starting from the index of the
 last traveled route section and an offset in meters from the last visited position on the
 section.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,com.here.sdk.routing.CalculateTrafficOnRouteCallback)">calculateTrafficOnRoute</a><wbr/>(<a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 <a href="sdk-for-android-explore-calculatetrafficonroutecallback" title="interface in com.here.sdk.routing">CalculateTrafficOnRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates the traffic along a route starting from the index of the last
 traveled route section and an offset (in meters) from the last visited position on the
 section.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#dispose()">dispose</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Cancels pending requests and closes the background worker thread.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously recreates a route from the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously creates a route from a sequence of geographic coordinates very close to each other.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a href="sdk-for-android-explore-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously creates a route from a sequence of geographic coordinates very close to each other.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#importRoute(java.util.List,java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">importRoute</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 <a href="sdk-for-android-explore-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#refreshRoute(com.here.sdk.routing.RefreshRouteParameters,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">refreshRoute</a><wbr/>(<a href="sdk-for-android-explore-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a> refreshRouteParameters,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">refreshRoute</a><wbr/>(<a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">refreshRoute</a><wbr/>(<a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">refreshRoute</a><wbr/>(<a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lastTraveledSectionIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> traveledDistanceOnLastSectionInMeters,
 <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">refreshRoute</a><wbr/>(<a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lastTraveledSectionIndex,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> traveledDistanceOnLastSectionInMeters,
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">
<div class="block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment">Will be removed in v4.28.0.</div>
</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">returnToRoute</a><wbr/>(<a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route,
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Asynchronously calculates a new route that leads back to the original route.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-routing-routingengine#setCustomOption(java.lang.String,java.lang.String)">setCustomOption</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets a custom option for routing backend queries.</div>
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
<h3>RoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutingEngine</span>()
              throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>RoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
              throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of RoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.RoutingConnectionSettings)">
<h3>RoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</span>
              throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of RoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>connectionSettings</code> - <p>Settings for the route calculation.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.RoutingConnectionSettings)">
<h3>RoutingEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoutingEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-explore-routingconnectionsettings" title="class in com.here.sdk.routing">RoutingConnectionSettings</a> connectionSettings)</span>
              throws <span class="exceptions"><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of RoutingEngine.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dd><code>connectionSettings</code> - <p>Settings for the route calculation.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-explore-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 @NonNull
 <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>refresh_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>. The route shape from the new
 starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
 delays are updated. If you only want to refresh the contained traffic information or retrieve updated ETA duration,
 consider using <a href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)"><code>calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)</code></a> instead.
 Calling this method will trigger a new "HERE Routing" transaction, for example,
 if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingPoint</code> - <p>Updates the starting point of the route. It should be of type <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise,
     an <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated. Moreover, it should be very close to the
     original route specified with the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Since the new starting point is expected to be
     along the original route, the original route geometry is used to reach the remaining waypoints. The new route
     will not include the <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that
     was already travelled). Plus, <a href="sdk-for-android-explore-route#getLengthInMeters()"><code>Route.getLengthInMeters()</code></a> and <a href="sdk-for-android-explore-route#getDuration()"><code>Route.getDuration()</code></a>
     values are from the new starting point to the destination. If the new waypoint is too far off the original
     route, the route refresh may fail and an <a href="sdk-for-android-explore-routingerror#COULD_NOT_MATCH_ORIGIN"><code>RoutingError.COULD_NOT_MATCH_ORIGIN</code></a> error is triggered.
     In that case, an application may decide to calculate a new route from scratch.</p></dd>
<dd><code>refreshRouteOptions</code> - <p>Options to refresh the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @Nullable
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lastTraveledSectionIndex,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>refresh_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>. The route shape from the new
 starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
 delays are updated. If you only want to refresh the contained traffic information, consider to use
 <a href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)"><code>calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)</code></a> instead.
 Calling this method will trigger a new "HERE Routing" transaction, for example,
 if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingPoint</code> - <p>Updates the starting point of the route. It should be of type <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise,
     an <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated. Moreover, it should be very close to the
     original route specified with the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Since the new starting point is expected to be
     along the original route, the original route geometry is used to reach the remaining waypoints. The new route
     will not include the <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that
     was already travelled). Plus, <a href="sdk-for-android-explore-route#getLengthInMeters()"><code>Route.getLengthInMeters()</code></a> and <a href="sdk-for-android-explore-route#getDuration()"><code>Route.getDuration()</code></a>
     values are from the new starting point to the destination. If the new waypoint is too far off the original
     route, the route refresh may fail and an <a href="sdk-for-android-explore-routingerror#COULD_NOT_MATCH_ORIGIN"><code>RoutingError.COULD_NOT_MATCH_ORIGIN</code></a> error is triggered.
     In that case, an application may decide to calculate a new route from scratch.</p></dd>
<dd><code>lastTraveledSectionIndex</code> - <p>Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p></dd>
<dd><code>traveledDistanceOnLastSectionInMeters</code> - <p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></dd>
<dd><code>refreshRouteOptions</code> - <p>Options to refresh the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,java.lang.Integer,java.lang.Integer,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @Nullable
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> lastTraveledSectionIndex,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a> traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>refresh_route()</code> methods with RefreshRouteParameters parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>. The route shape from the new
 starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
 delays are updated. If you only want to refresh the contained traffic information, consider to use
 <a href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)"><code>calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)</code></a> instead.
 Calling this method will trigger a new "HERE Routing" transaction, for example,
 if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingPoint</code> - <p>Updates the starting point of the route. It should be of type <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise,
     an <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated. Moreover, it should be very close to the
     original route specified with the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Since the new starting point is expected to be
     along the original route, the original route geometry is used to reach the remaining waypoints. The new route
     will not include the <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that
     was already traveled). Plus, <a href="sdk-for-android-explore-route#getLengthInMeters()"><code>Route.getLengthInMeters()</code></a> and <a href="sdk-for-android-explore-route#getDuration()"><code>Route.getDuration()</code></a>
     values are from the new starting point to the destination. If the new waypoint is too far off the original
     route, the route refresh may fail and an <a href="sdk-for-android-explore-routingerror#COULD_NOT_MATCH_ORIGIN"><code>RoutingError.COULD_NOT_MATCH_ORIGIN</code></a> error is triggered.
     In that case, an application may decide to calculate a new route from scratch.</p></dd>
<dd><code>lastTraveledSectionIndex</code> - <p>Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p></dd>
<dd><code>traveledDistanceOnLastSectionInMeters</code> - <p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p></dd>
<dd><code>options</code> - <p>The options define the vehicle and route options to calculate the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refreshRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>refresh_route()</code> methods with RefreshRouteParameters parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>. The route shape from the new
 starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
 delays are updated. If you only want to refresh the contained traffic information, consider to use
 <a href="sdk-for-android-explore-com-here-sdk-routing-routingengine#calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)"><code>calculateTrafficOnRoute(Route, int, int, double, CalculateTrafficOnRouteCallback)</code></a> instead.
 Calling this method will trigger a new "HERE Routing" transaction, for example,
 if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingPoint</code> - <p>Updates the starting point of the route. It should be of type <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise,
     an <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated. Moreover, it should be very close to the
     original route specified with the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Since the new starting point is expected to be
     along the original route, the original route geometry is used to reach the remaining waypoints. The new route
     will not include the <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that
     was already traveled). Plus, <a href="sdk-for-android-explore-route#getLengthInMeters()"><code>Route.getLengthInMeters()</code></a> and <a href="sdk-for-android-explore-route#getDuration()"><code>Route.getDuration()</code></a>
     values are from the new starting point to the destination. If the new waypoint is too far off the original
     route, the route refresh may fail and an <a href="sdk-for-android-explore-routingerror#COULD_NOT_MATCH_ORIGIN"><code>RoutingError.COULD_NOT_MATCH_ORIGIN</code></a> error is triggered.
     In that case, an application may decide to calculate a new route from scratch.</p></dd>
<dd><code>options</code> - <p>The options define the vehicle and route options to calculate the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="refreshRoute(com.here.sdk.routing.RefreshRouteParameters,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">refreshRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a> refreshRouteParameters,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>. The route shape from the new
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously recreates a route from the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e. refreshes a previously
 calculated route, with the specified <a href="sdk-for-android-explore-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>.
 A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly.
 Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service.
 For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>refreshRouteOptions</code> - <p>The options define the vehicle and route options to calculate the route.
     <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.ElectricVehicleOptions.ensure_reachability] option is set to <code>true</code>.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
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
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>pedestrianOptions</code> - <p>Options specific for pedestrian route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a>
     is not supported for pedestrians and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>bicycleOptions</code> - <p>Options specific for bicycle route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>scooterOptions</code> - <p>Options specific for scooter route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a>
     is not supported for scooters and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>pedestrianOptions</code> - <p>Options specific for pedestrian route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a>
     is not supported for pedestrians and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>bicycleOptions</code> - <p>Options specific for bicycle route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>scooterOptions</code> - <p>Options specific for scooter route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a>
     is not supported for scooters and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
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
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>taxiOptions</code> - <p>Options specific for taxi route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a>
     is not supported for taxis and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>busOptions</code> - <p>Options specific for bus route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>privateBusOptions</code> - <p>Options specific for private bus route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>evCarOptions</code> - <p>Options specific for an electric car route calculation, along with
     common route options.
     <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.EVCarOptions.ensure_reachability] option is set to <code>true</code>.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
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
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
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
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
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
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>taxiOptions</code> - <p>Options specific for taxi route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a>
     is not supported for taxis and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>busOptions</code> - <p>Options specific for bus route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>privateBusOptions</code> - <p>Options specific for private bus route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>evCarOptions</code> - <p>Options specific for an electric car route calculation, along with
     common route options.
     <strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.EVCarOptions.ensure_reachability] option is set to <code>true</code>.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
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
<section class="detail" id="importRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>options</code> - <p>The options define the vehicle and route options to calculate the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="importRoute(java.util.List,java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-location" title="class in com.here.sdk.core">Location</a>&gt; locations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-routestop" title="class in com.here.sdk.routing">RouteStop</a>&gt; routeStops,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will
 be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
 or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
 be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.
 <strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
 discarded and reported as violations in <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> .</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locations</code> - <p>The list of locations used to calculate the route. Note that only the <a href="sdk-for-android-explore-location#coordinates"><code>Location.coordinates</code></a> of a location are used to import the route.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the location list
     size is not in the range [2,50000].</p></dd>
<dd><code>routeStops</code> - <p>The list of RouteStop's which contains index of location from locations list used for route stop and duration in seconds spent on stop.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the route stops list
     size is not in the range [1,locations.size()-2], any of location_index is &lt; 1 or location_indexes are not unique.</p></dd>
<dd><code>options</code> - <p>The options define the vehicle and route options to calculate the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">importRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously recreates a route from the <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e. refreshes a previously
 calculated route, with the specified <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>.
 A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
 Therefore, the route handle is not meant to be persisted for a longer time.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>options</code> - <p>The options define the vehicle and route options to calculate the route.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after refreshing the route.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,com.here.sdk.routing.CalculateTrafficOnRouteCallback)">
<h3>calculateTrafficOnRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateTrafficOnRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-explore-calculatetrafficonroutecallback" title="interface in com.here.sdk.routing">CalculateTrafficOnRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates the traffic along a route starting from the index of the last
 traveled route section and an offset (in meters) from the last visited position on the
 section. Call this when only the contained traffic information or the latest ETA duration
 is needed. This can be called periodically to retrieve updated ETA values during navigation.
 <strong>Note:</strong> Calling this method will trigger a new "HERE Traffic" transaction, for example,
 if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>A <a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing"><code>Route</code></a> calculated using the online routing engine. Its
     <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> and the original route calculation options will be used to
     compute the traffic on the route. The original route remains untouched.</p></dd>
<dd><code>lastTraveledSectionIndex</code> - <p>Indicates the index of the last traveled route section. Traveled part of the route won't
     be reused.</p></dd>
<dd><code>traveledDistanceOnLastSectionInMeters</code> - <p>Offset, in meters, to the last visited position on the route section defined by the last
     traveled section index.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route traffic has been calculated.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateTrafficOnRoute(com.here.sdk.routing.Route,int,int,double,com.here.sdk.routing.CalculateTrafficOnRouteCallback)">
<h3>calculateTrafficOnRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateTrafficOnRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 double currentChargeInKilowattHours,
 @NonNull
 <a href="sdk-for-android-explore-calculatetrafficonroutecallback" title="interface in com.here.sdk.routing">CalculateTrafficOnRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates the traffic along an EV car route starting from the index of the
 last traveled route section and an offset in meters from the last visited position on the
 section.
 The field <a href="sdk-for-android-explore-trafficonspan#consumptionInKilowattHours"><code>TrafficOnSpan.consumptionInKilowattHours</code></a> will contain the power consumption
 in kilowatt-hours (kWh) necessary to traverse the span, and
 <a href="sdk-for-android-explore-routeplace#chargeInKilowattHours"><code>RoutePlace.chargeInKilowattHours</code></a>, inside <a href="sdk-for-android-explore-trafficonsection#departurePlace"><code>TrafficOnSection.departurePlace</code></a> and
 <a href="sdk-for-android-explore-trafficonsection#arrivalPlace"><code>TrafficOnSection.arrivalPlace</code></a>, the estimated battery charge in kilowatt-hours (kWh) when
 leaving/arriving to a section.
 <strong>Note:</strong> Only EV cars are supported.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>A <a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing"><code>Route</code></a> calculated using the online routing engine. Its
     <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> and the original route calculation options, along with EV
     related information like <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a>, will be used to
     compute the traffic on the route. The original route remains untouched.</p></dd>
<dd><code>lastTraveledSectionIndex</code> - <p>Indicates the index of the last traveled route section. Traveled part of the route won't
     be reused.</p></dd>
<dd><code>traveledDistanceOnLastSectionInMeters</code> - <p>Offset, in meters, to the last visited position on the route section defined by the last
     traveled section index.</p></dd>
<dd><code>currentChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the current location (in kWh).
     It must be non-negative and less than or equal to the value of
     <a href="sdk-for-android-explore-batteryspecifications#totalCapacityInKilowattHours"><code>BatterySpecifications.totalCapacityInKilowattHours</code></a>,
     otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
     Sets <a href="sdk-for-android-explore-batteryspecifications#initialChargeInKilowattHours"><code>BatterySpecifications.initialChargeInKilowattHours</code></a> to the given value.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route traffic has been calculated.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setCustomOption(java.lang.String,java.lang.String)">
<h3>setCustomOption</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">setCustomOption</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div class="block"><p>Sets a custom option for routing backend queries.
 The custom option is applied to all the queries that <code>RoutingEngine</code> performs.
 For a complete list of available parameter names and their valid values, refer to
 <a href="https://www.here.com/docs/bundle/routing-api-v8-api-reference/page/index.html">HERE Routing API v8</a>.
 <strong>Note:</strong> It's easy to set a wrong option that makes queries invalid,
 so make sure you read and understand the backend documentation.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - <p>An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.</p></dd>
<dd><code>value</code> - <p>An option value. If the value is <code>null</code>, the option will be removed. The option value must be a non-empty string.</p></dd>
<dt>Returns:</dt>
<dd><p>An optional error of setting the option. It's <code>null</code> if the option has been set successfully.
     It's <code>RoutingError.INVALID_PARAMETER</code> if the input name and/or value haven't passed internal validation.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates a route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a car route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a pedestrian route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>pedestrianOptions</code> - <p>Options specific for pedestrian route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for pedestrians and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a truck route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a scooter route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>scooterOptions</code> - <p>Options specific for scooter route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for scooters and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a bicycle route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>bicycleOptions</code> - <p>Options specific for bicycle route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for bicycles and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a taxi route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>taxiOptions</code> - <p>Options specific for taxi route calculation, along with
     common route options. Note that <a href="sdk-for-android-explore-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for taxis and converted to
     <a href="sdk-for-android-explore-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates an electric car route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates an electic truck route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a bus route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">calculateRoute</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-explore-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div class="block"><p>Asynchronously calculates a private bus route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">returnToRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing">Route</a> route,
 @NonNull
 <a href="sdk-for-android-explore-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-explore-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div class="block"><p>Asynchronously calculates a new route that leads back to the original route. The part of
 the original route which was already traveled by the user is ignored.
 <strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
 be ignored.
 Additionally, the following route options are ignored:
 <a href="sdk-for-android-explore-routeoptions#alternatives"><code>RouteOptions.alternatives</code></a>, <a href="sdk-for-android-explore-routeoptions#arrivalTime"><code>RouteOptions.arrivalTime</code></a>, and
 <a href="sdk-for-android-explore-routeoptions#optimizationMode"><code>RouteOptions.optimizationMode</code></a>.
 Most route options are only applied to the newly calculated part back to the route.
 An application may use this method to submit a new
 starting point for a previously calculated route. This method tries to avoid a costly
 route re-calculation as much as possible. In case returning to the route without
 re-calculation is not possible, a new route is calculated, while trying to salvage
 the previous route as much as possible. However, a completely new route
 containing no part of the previous route is possible, too.
 Note that this function uses only a limited amount of map data around the new origin.
 Therefore, it may also work fine with temporarily cached map data. It may also copy some of the
 original route data into the new route.
 A typical use case is to await at least 3 <code>RouteDeviation</code> events before calling this method.
 <ul>
<li>Or alternatively, wait at least 10 seconds after getting the first deviation event.</li>
<li>On top, the user experience can be improved by checking if the vehicle has moved at least
 50 meters since calling this method for the last time.</li>
<li>Optionally, it may make sense to verify if the vehicle was ever following the route by checking if
 <code>RouteDeviation.lastLocationOnRoute</code> is set.</li>
</ul>
Note that deviation events are sent each time a deviation is detected, i.e. for each new location
 update, regardless if the location has changed or not.
 More information can be found in the Developer Guide in the "Handle route deviations" section.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-explore-routinginterface#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">returnToRoute</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
<dt>Parameters:</dt>
<dd><code>route</code> - <p>A <a href="sdk-for-android-explore-route" title="class in com.here.sdk.routing"><code>Route</code></a> calculated using the online or offline route engine. For the offline case, It
     should not contain an indoor <a href="sdk-for-android-explore-section" title="class in com.here.sdk.routing"><code>Section</code></a> as such routes will fail. For the online case, it
     should have <a href="sdk-for-android-explore-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.</p></dd>
<dd><code>startingPoint</code> - <p>The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
     type <a href="sdk-for-android-explore-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise, an <a href="sdk-for-android-explore-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a>
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
<dd><code><a href="sdk-for-android-explore-routinginterface#dispose()">dispose</a></code> in interface <code><a href="sdk-for-android-explore-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
