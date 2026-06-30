---
title: "RefreshRouteOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RefreshRouteOptions.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.RefreshRouteOptions</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" title="class or interface in java.lang">@Deprecated</a>
</span><span class="modifiers">public final class </span><span class="element-name type-name-label">RefreshRouteOptions</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span>
<div class="deprecation-comment"><p>Will be removed in v4.28.0. Use the <code>RoutingOptions</code> class instead.</p></div>
</div>
<div class="block"><p>The options to specify how to refresh an already calculated route identified by a <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. All the
 options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that
 accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored:
 <a href="sdk-for-android-navigate-routeoptions#alternatives"><code>RouteOptions.alternatives</code></a>, <a href="sdk-for-android-navigate-routeoptions#arrivalTime"><code>RouteOptions.arrivalTime</code></a>, and <a href="sdk-for-android-navigate-routeoptions#optimizationMode"><code>RouteOptions.optimizationMode</code></a>.
 If new <a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a> are specified, they are ignored as well and instead new <a href="sdk-for-android-navigate-com-here-sdk-routing-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a>'s
 are generated that indicate where the requested <a href="sdk-for-android-navigate-com-here-sdk-routing-avoidanceoptions" title="class in com.here.sdk.routing"><code>AvoidanceOptions</code></a> are violated. Note that when
 <a href="sdk-for-android-navigate-evcaroptions#ensureReachability"><code>EVCarOptions.ensureReachability</code></a> is set to true, the route refresh request will fail as this option
 is incompatible with a fixed route shape.
 If any of the ignored options are important, consider calculating a new route instead.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.BicycleOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing"><code>BicycleOptions</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.BusOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing"><code>BusOptions</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.CarOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing"><code>CarOptions</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.EVCarOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing"><code>EVCarOptions</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.EVTruckOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing"><code>EVTruckOptions</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.PedestrianOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing"><code>PedestrianOptions</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.PrivateBusOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing"><code>PrivateBusOptions</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.ScooterOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing"><code>ScooterOptions</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.TaxiOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing"><code>TaxiOptions</code></a>.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.routing.TruckOptions)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions)</code></div>
<div class="col-last odd-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing"><code>TruckOptions</code></a>.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-refreshrouteoptions#%3Cinit%3E(com.here.sdk.transport.TransportMode)">RefreshRouteOptions</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode)</code></div>
<div class="col-last even-row-color">
<div class="block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block">Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport"><code>TransportMode</code></a>.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

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
<section class="detail" id="&lt;init&gt;(com.here.sdk.transport.TransportMode)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport">TransportMode</a> transportMode)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-transport-transportmode" title="enum class in com.here.sdk.transport"><code>TransportMode</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>transportMode</code> - <p>Updates the transport mode for the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.CarOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing">CarOptions</a> carOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-caroptions" title="class in com.here.sdk.routing"><code>CarOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>carOptions</code> - <p>Converts the route to a car route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.TruckOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing">TruckOptions</a> truckOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-truckoptions" title="class in com.here.sdk.routing"><code>TruckOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>truckOptions</code> - <p>Converts the route to a truck route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.PedestrianOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing">PedestrianOptions</a> pedestrianOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-pedestrianoptions" title="class in com.here.sdk.routing"><code>PedestrianOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>pedestrianOptions</code> - <p>Converts the route to a pedestrian route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.ScooterOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing">ScooterOptions</a> scooterOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-scooteroptions" title="class in com.here.sdk.routing"><code>ScooterOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>scooterOptions</code> - <p>Converts the route to a scooter route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.TaxiOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing">TaxiOptions</a> taxiOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-taxioptions" title="class in com.here.sdk.routing"><code>TaxiOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>taxiOptions</code> - <p>Converts the route to a taxi route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.EVCarOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing">EVCarOptions</a> evCarOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-evcaroptions" title="class in com.here.sdk.routing"><code>EVCarOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evCarOptions</code> - <p>Converts the route to an electric car route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.EVTruckOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing">EVTruckOptions</a> evTruckOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-evtruckoptions" title="class in com.here.sdk.routing"><code>EVTruckOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>evTruckOptions</code> - <p>Converts the route to an electric truck route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.BicycleOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing">BicycleOptions</a> bicycleOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-bicycleoptions" title="class in com.here.sdk.routing"><code>BicycleOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>bicycleOptions</code> - <p>Converts the route to a bicycle route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.BusOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing">BusOptions</a> busOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-busoptions" title="class in com.here.sdk.routing"><code>BusOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>busOptions</code> - <p>Converts the route to a bus route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.PrivateBusOptions)">
<h3>RefreshRouteOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing">PrivateBusOptions</a> privateBusOptions)</span></div>
<div class="deprecation-block"><span class="deprecated-label">Deprecated.</span></div>
<div class="block"><p>Constructs a RefreshRouteOptions object with <a href="sdk-for-android-navigate-com-here-sdk-routing-privatebusoptions" title="class in com.here.sdk.routing"><code>PrivateBusOptions</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>privateBusOptions</code> - <p>Converts the route to a private bus route, if a different transport mode was used for the
     <a href="sdk-for-android-navigate-com-here-sdk-routing-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. Note that in case this is not possible,
     an <a href="sdk-for-android-navigate-routingerror#NO_ROUTE_FOUND"><code>RoutingError.NO_ROUTE_FOUND</code></a> error will be triggered.</p></dd>
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
