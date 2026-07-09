---
title: "DynamicRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DynamicRoutingEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficawarenavigation</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.trafficawarenavigation.DynamicRoutingEngine</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">DynamicRoutingEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>This class queries the HERE routing backend
 to find routes with less traffic and therefore an earlier remaining estimated time of arrival.
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a> polls the HERE routing backend periodically to find the best new route out
 of a given initial route.
 For initial route calculation it is recommended to use the <a href="sdk-for-android-navigate-com-here-sdk-routing-routingengine" title="class in com.here.sdk.routing"><code>RoutingEngine</code></a>
 as it already requests traffic-optimized routes.
 When a better route is found, it is recommended to follow these steps to set the new route:
 <ol>
<li>Stop the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a>.</li>
<li>Update the currently active <code>Navigator</code>instance with the newly found route.</li>
<li>Restart the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a>. This should be done outside of the <code>onBetterRouteFound()</code> callback.</li>
</ol>
For both <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-routing-routingengine" title="class in com.here.sdk.routing"><code>RoutingEngine</code></a>,
 the resulting routes are optimized based on speed flow changes such as traffic jams,
 street closures or road accidents.
 To get the best result, it is recommended to not specify the
 <a href="sdk-for-android-navigate-routeoptions#departureTime"><code>RouteOptions.departureTime</code></a> as then the current time is used by default.
 The poll interval is defined by
 <a href="sdk-for-android-navigate-dynamicroutingengineoptions#pollInterval"><code>DynamicRoutingEngineOptions.pollInterval</code></a> and
 triggered by <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine#updateCurrentLocation(com.here.sdk.navigation.MapMatchedLocation,int)"><code>updateCurrentLocation(com.here.sdk.navigation.MapMatchedLocation, int)</code></a>.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-starterror" title="enum class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartError</a></code></div>
<div className="col-last even-row-color">
<div className="block">Start error</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Start exception</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.trafficawarenavigation.DynamicRoutingEngineOptions)">DynamicRoutingEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngineOptions</a> options)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine#%3Cinit%3E(com.here.sdk.trafficawarenavigation.DynamicRoutingEngineOptions)">DynamicRoutingEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngineOptions</a> options)</code></div>
<div className="col-last odd-row-color">
<div className="block">Creates a new instance of this class.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.trafficawarenavigation.DynamicRoutingEngineOptions)">
<h3>DynamicRoutingEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DynamicRoutingEngine</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngineOptions</a> options)</span>
                     throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>options</code> - <p>The options defining the behavior of the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>when the engine was not initialized properly.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.trafficawarenavigation.DynamicRoutingEngineOptions)">
<h3>DynamicRoutingEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">DynamicRoutingEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngineOptions</a> options)</span>
                     throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>Instance of an existing SDKEngine.</p></dd>
<dd><code>options</code> - <p>The options defining the behavior of the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a>.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>when the engine was not initialized properly.</p></dd>
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
<section className="detail" id="start(com.here.sdk.routing.Route,com.here.sdk.trafficawarenavigation.DynamicRoutingListener)">
<h3>start</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> route,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener" title="interface in com.here.sdk.trafficawarenavigation">DynamicRoutingListener</a> listener)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></span></div>
<div className="block"><p>Starts polling the HERE backend services to find a better route,
 as defined by the DynamicRoutingEngineOptions.
 <strong>Note:</strong> The engine will be internally stopped, if it was started before.
 Therefore, it is not necessary to stop the engine before starting it again.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>The route to be refreshed. The route must contain a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>,
     therefore the route must have been requested with
     <a href="sdk-for-android-navigate-routeoptions#enableRouteHandle"><code>RouteOptions.enableRouteHandle</code></a> set to <code>true</code>.
     The information to calculate new routes will be extracted from the provided route parameter.
     If more information from the original waypoints is important besides their location,
     consider to use one of the overloaded methods instead.</p></dd>
<dd><code>listener</code> - <p>The listener to receive the events.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></code> - <p>when the passed parameter are invalid.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="start(com.here.sdk.routing.RouteHandle,java.util.List,com.here.sdk.routing.RefreshRouteOptions,com.here.sdk.trafficawarenavigation.DynamicRoutingListener)">
<h3>start</h3>
<div className="member-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions" title="class in com.here.sdk.routing">RefreshRouteOptions</a> refreshRouteOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener" title="interface in com.here.sdk.trafficawarenavigation">DynamicRoutingListener</a> listener)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></span></div>
<div className="deprecation-block"><span className="deprecated-label">Deprecated.</span>
<div className="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>start()</code> method with RoutingOptions parameter instead.</p></div>
</div>
<div className="block"><p>Starts polling the HERE backend services to find a better route,
 as defined by the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngineOptions</code></a>.
 <strong>Note:</strong> The engine will be internally stopped, if it was started before.
 Therefore, it is not necessary to stop the engine before starting it again.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle from the HERE routing backend.</p></dd>
<dd><code>waypoints</code> - <p>Allows to specify detailed information on the waypoints of the route.
     This parameter can be useful, when additional information needs to be
     specified besides the coordinates - as the coordinates can be retrieved
     from the contained <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> that are already contained in
     the <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> parameter.</p></dd>
<dd><code>refreshRouteOptions</code> - <p>The options for the route calculation.</p></dd>
<dd><code>listener</code> - <p>The listener to receive the events.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></code> - <p>when the passed parameter are invalid.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="start(com.here.sdk.routing.RouteHandle,java.util.List,com.here.sdk.routing.RoutingOptions,com.here.sdk.trafficawarenavigation.DynamicRoutingListener)">
<h3>start</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">start</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-waypoint" title="class in com.here.sdk.routing">Waypoint</a>&gt; waypoints,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingoptions" title="class in com.here.sdk.routing">RoutingOptions</a> routingOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener" title="interface in com.here.sdk.trafficawarenavigation">DynamicRoutingListener</a> listener)</span>
           throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></span></div>
<div className="block"><p>Starts polling the HERE backend services to find a better route,
 as defined by the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngineOptions</code></a>.
 <strong>Note:</strong> The engine will be internally stopped, if it was started before.
 Therefore, it is not necessary to stop the engine before starting it again.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle from the HERE routing backend.</p></dd>
<dd><code>waypoints</code> - <p>Allows to specify detailed information on the waypoints of the route.
     This parameter can be useful, when additional information needs to be
     specified besides the coordinates - as the coordinates can be retrieved
     from the contained <a href="sdk-for-android-navigate-com-here-sdk-routing-routeplace" title="class in com.here.sdk.routing"><code>RoutePlace</code></a> that are already contained in
     the <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a> parameter.</p></dd>
<dd><code>routingOptions</code> - <p>The options for the route calculation.</p></dd>
<dd><code>listener</code> - <p>The listener to receive the events.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine-startexception" title="class in com.here.sdk.trafficawarenavigation">DynamicRoutingEngine.StartException</a></code> - <p>when the passed parameter are invalid.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="stop()">
<h3>stop</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">stop</span>()</div>
<div className="block"><p>Stops polling the HERE backend services.
 <strong>Note:</strong> The engine is not automatically stopped when the destination is reached.
 Therefore, it is recommended to stop the engine when the destination was reached.</p></div>
</section>
</li>
<li>
<section className="detail" id="updateCurrentLocation(com.here.sdk.navigation.MapMatchedLocation,int)">
<h3>updateCurrentLocation</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">updateCurrentLocation</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-navigation-mapmatchedlocation" title="class in com.here.sdk.navigation">MapMatchedLocation</a> mapMatchedLocation,
 int sectionIndex)</span></div>
<div className="block"><p>Updates the current location. This location will be used as new starting point when the next
 <a href="sdk-for-android-navigate-dynamicroutingengineoptions#pollInterval"><code>DynamicRoutingEngineOptions.pollInterval</code></a> is reached and a new route is requested.
 If an immediate route update is needed, consider to use the RoutingEngine instead.
 All subsequently calculated routes used for the ETA calculation will start from this location.
 The location needs to lie on the route or a <code>RoutingError</code> will be issued.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapMatchedLocation</code> - <p>The last known location.
     It is recommended to use a <a href="sdk-for-android-navigate-navigablelocation#mapMatchedLocation"><code>NavigableLocation.mapMatchedLocation</code></a>
     as the driver is expected to be on a road.</p></dd>
<dd><code>sectionIndex</code> - <p>The current section from <a href="sdk-for-android-navigate-routeprogress#sectionIndex"><code>RouteProgress.sectionIndex</code></a>.</p></dd>
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
