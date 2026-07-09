---
title: "RoutingInterface (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routinginterface"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- RoutingInterface.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine" title="class in com.here.sdk.routing">OfflineRoutingEngine</a></code>, <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routingengine" title="class in com.here.sdk.routing">RoutingEngine</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">RoutingInterface</span></div>
<div className="block"><p>Provides the interface for the online and offline
 routing engines.
 <strong>Note</strong>: Clients need to explicitly call <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface#dispose()"><code>dispose()</code></a> in order to prevent a possible, though
 unlikely, deadlock on destruction.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously calculates a route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>options</code> - <p>Options describing routing options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a car route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a pedestrian route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>pedestrianOptions</code> - <p>Options specific for pedestrian route calculation, along with
     common route options. Note that <a href="sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for pedestrians and converted to
     <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a truck route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a scooter route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>scooterOptions</code> - <p>Options specific for scooter route calculation, along with
     common route options. Note that <a href="sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for scooters and converted to
     <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a bicycle route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>bicycleOptions</code> - <p>Options specific for bicycle route calculation, along with
     common route options. Note that <a href="sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for bicycles and converted to
     <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a taxi route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
<dd><code>taxiOptions</code> - <p>Options specific for taxi route calculation, along with
     common route options. Note that <a href="sdk-for-android-navigate-optimizationmode#SHORTEST"><code>OptimizationMode.SHORTEST</code></a> is
     is not supported for taxis and converted to
     <a href="sdk-for-android-navigate-optimizationmode#FASTEST"><code>OptimizationMode.FASTEST</code></a> automatically.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates an electric car route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates an electic truck route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a bus route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>calculate_route()</code> methods with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously calculates a private bus route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>waypoints</code> - <p>The list of waypoints used to calculate the route.
     The first element marks the starting position, the last marks the destination.
     Waypoints in between are interpreted as intermediate.
     An <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated when the waypoint list
     contains less than two elements or when the first and the last waypoints are not of type
     <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.</p></dd>
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
<section className="detail" id="returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">
<h3>returnToRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">returnToRoute</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int lastTraveledSectionIndex,
 int traveledDistanceOnLastSectionInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously calculates a new route that leads back to the original route. The part of
 the original route which was already traveled by the user is ignored.
 <strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
 be ignored.
 Additionally, the following route options are ignored:
 <a href="sdk-for-android-navigate-routeoptions#alternatives"><code>RouteOptions.alternatives</code></a>, <a href="sdk-for-android-navigate-routeoptions#arrivalTime"><code>RouteOptions.arrivalTime</code></a>, and
 <a href="sdk-for-android-navigate-routeoptions#optimizationMode"><code>RouteOptions.optimizationMode</code></a>.
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
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>A <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> calculated using the online or offline route engine. For the offline case, It
     should not contain an indoor <a href="sdk-for-android-navigate-com-here-sdk-routing-section" title="class in com.here.sdk.routing"><code>Section</code></a> as such routes will fail. For the online case, it
     should have <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.</p></dd>
<dd><code>startingPoint</code> - <p>The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
     type <a href="sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>. Otherwise, an <a href="sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a>
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
<section className="detail" id="dispose()">
<h3>dispose</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">dispose</span>()</div>
<div className="block"><p>Cancels pending requests and closes the background worker thread.
 <strong>Note:</strong> This method should be called from main thread.</p></div>
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
