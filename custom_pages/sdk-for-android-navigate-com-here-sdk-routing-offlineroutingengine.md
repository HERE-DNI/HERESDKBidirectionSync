---
title: "OfflineRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- OfflineRoutingEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.routing.OfflineRoutingEngine</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">OfflineRoutingEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a>
implements <a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></span></div>
<div className="block"><p>Use this class to calculate a route offline from A to B with
 a number of waypoints in between.
 Route calculation is done asynchronously, and requires map data that is
 available offline. This can be temporarily cached map data or downloaded
 offline map data stored in the persisted storage via <code>MapDownloader</code>.
 Note that when using the cache there is a risk of missing data and this may
 reduce the overall quality of the route or can result in a
 <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error.
 The resulting route contains various information such as the polyline,
 route length in meters, estimated time to traverse along the route
 and maneuver data, but it does not contain traffic information.
 Unlike the <code>RoutingEngine</code> (which requires an online connection), this engine
 allows to use an unlimited number of waypoints.
 As an alternative to this engine, consider to use the <code>RoutingEngine</code> for online
 route calculations to get fresher traffic, maneuver, route handles and street
 information, and to use a more elaborate algorithms to calculate the fastest route.
 For offline bus routing, enable "OFFLINE_BUS_ROUTING" as feature configuration.
 For more details, please look at <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdkoptions" title="class in com.here.sdk.core.engine"><code>SDKOptions</code></a>. If this feature is not
 enabled, the engine may not be able to find bus routes.
 <strong>Note:</strong> EV routing is available when calculating a route using the <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>, by setting
 the <a href="sdk-for-android-navigate-routingoptions#evOptions"><code>RoutingOptions.evOptions</code></a>.
 <strong>Note:</strong> Traffic related information is completely excluded.
 No historic traffic patterns are taking into consideration for the ETA.
 Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e.
 the road may pass through such road.
 Only seasonal road closures are considered based on the departure time, if given.
 Traffic information is only considered for online route calculation with the <code>RoutingEngine</code>.
 <strong>Note:</strong> Route handles produced by this engine are not compatible with those created by
 the <code>RoutingEngine</code>. Importing, refreshing, or returning to a route via a route
 handle is supported only when the route was calculated with the same engine. However,
 this engine supports returning to a route calculated with the <code>RoutingEngine</code> when
 the route object is provided.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine#%3Cinit%3E()">OfflineRoutingEngine</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">OfflineRoutingEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of OfflineRoutingEngine.</div>
</div>
<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.OfflineRoutingEngineOptions)">OfflineRoutingEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengineoptions" title="class in com.here.sdk.routing">OfflineRoutingEngineOptions</a> options)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of OfflineRoutingEngine.</div>
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
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section className="constructor-details" id="constructor-detail">

<ul className="member-list">
<li>
<section className="detail" id="&lt;init&gt;()">
<h3>OfflineRoutingEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">OfflineRoutingEngine</span>()
                     throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>OfflineRoutingEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">OfflineRoutingEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                     throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of OfflineRoutingEngine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.routing.OfflineRoutingEngineOptions)">
<h3>OfflineRoutingEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">OfflineRoutingEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-offlineroutingengineoptions" title="class in com.here.sdk.routing">OfflineRoutingEngineOptions</a> options)</span>
                     throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of OfflineRoutingEngine.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
<dd><code>options</code> - <p>Options to configure offline routing engine.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section className="detail" id="refreshRoute(com.here.sdk.routing.RefreshRouteParameters,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>refreshRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">refreshRoute</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteparameters" title="class in com.here.sdk.routing">RefreshRouteParameters</a> refreshRouteParameters,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>, updating
 the starting point and route metadata based on <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing"><code>RoutingOptions</code></a>. The route shape from the new
 starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
 delays are updated.</p></div>
<dl className="notes">
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
<section className="detail" id="importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">importRoute</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>import_route()</code> method with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Asynchronously recreates a route from the <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e. refreshes a previously
 calculated route, with the specified <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>.
 A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
 Therefore, the route handle is not meant to be persisted for a longer time.</p></div>
<dl className="notes">
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
<section className="detail" id="importRoute(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>importRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">importRoute</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously recreates a route from the <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> provided, i.e. refreshes a previously
 calculated route, with the specified <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing"><code>RefreshRouteOptions</code></a>.
 A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
 Therefore, the route handle is not meant to be persisted for a longer time.</p></div>
<dl className="notes">
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
<section className="detail" id="setInternalOption(java.lang.String,java.lang.String)">
<h3>setInternalOption</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setInternalOption</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> key,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> value)</span></div>
<div className="block"><p>This method sets internal options that controls offline route calculation behavior.
 Unsupported options will be logged as warnings.
 Undocumented options can change their meaning without going through deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>key</code> - <p>Option name</p></dd>
<dd><code>value</code> - <p>New option value</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficDataProvider()">
<h3>getTrafficDataProvider</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a></span> <span className="element-name">getTrafficDataProvider</span>()</div>
<div className="block"><p>Gets the traffic data provider that provides internal traffic information considering in routing.
 If the traffic data provider is <code>null</code>, traffic is not considered in routing.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The traffic data provider that gets internal traffic information considering in routing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="setTrafficDataProvider(com.here.sdk.traffic.TrafficDataProvider)">
<h3>setTrafficDataProvider</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setTrafficDataProvider</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficdataprovider" title="class in com.here.sdk.traffic">TrafficDataProvider</a> value)</span></div>
<div className="block"><p>Sets the traffic data provider that provides internal traffic information considering in routing.
 If the traffic data provider is <code>null</code>, traffic is not considered in routing.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The traffic data provider that gets internal traffic information considering in routing.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> options,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-calculateroutecallback" title="interface in com.here.sdk.routing">CalculateRouteCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously calculates a route from one point to another,
 passing through the given waypoints in the given order.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.CarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PedestrianOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.ScooterOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BicycleOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.TaxiOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVCarOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.EVTruckOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.BusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#calculateRoute(java.util.List,com.here.sdk.routing.PrivateBusOptions,com.here.sdk.routing.CalculateRouteCallback)">calculateRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">returnToRoute</span><wbr/><span className="parameters">(@NonNull
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
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#returnToRoute(com.here.sdk.routing.Route,com.here.sdk.routing.Waypoint,int,int,com.here.sdk.routing.CalculateRouteCallback)">returnToRoute</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">dispose</span>()</div>
<div className="block"><p>Cancels pending requests and closes the background worker thread.
 <strong>Note:</strong> This method should be called from main thread.</p></div>
<dl className="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-routinginterface#dispose()">dispose</a></code> in interface <code><a href="sdk-for-android-navigate-com-here-sdk-routing-routinginterface" title="interface in com.here.sdk.routing">RoutingInterface</a></code></dd>
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
