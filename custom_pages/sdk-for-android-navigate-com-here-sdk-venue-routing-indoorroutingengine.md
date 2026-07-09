---
title: "IndoorRoutingEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutingengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- IndoorRoutingEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.routing</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.venue.routing.IndoorRoutingEngine</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">IndoorRoutingEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Use the IndoorRoutingEngine to calculate a route inside a venue.
 <br/>
 Route calculation is done asynchronously and requires an
 internet connection. The resulting route contains various
 information such as the polyline, route length in meters,
 estimated time to traverse along the route and maneuver data.
 <br/>
 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.
 Currently, the indoor route calculation may not be accurate so that e.g. a pedestrian
 end user might be routed via a vehicle access and route or similar. Therefore end users
 must use this feature with caution and always be aware of the surroundings. The signs
 and instructions given at the premises must be observed. You are required to inform
 the end user about this in an appropriate manner, whether in the UI of your application,
 your end user terms or similar.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorroutingengine#%3Cinit%3E(com.here.sdk.venue.service.VenueService)">IndoorRoutingEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a> venueService)</code></div>
<div className="col-last even-row-color">
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.venue.service.VenueService)">
<h3>IndoorRoutingEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">IndoorRoutingEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-service-venueservice" title="class in com.here.sdk.venue.service">VenueService</a> venueService)</span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>venueService</code> - <p>A venue service instance.</p></dd>
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
<section className="detail" id="calculateRoute(com.here.sdk.venue.routing.IndoorWaypoint,com.here.sdk.venue.routing.IndoorWaypoint,com.here.sdk.venue.routing.IndoorRouteOptions,com.here.sdk.venue.routing.CalculateIndoorRouteCallback)">
<h3>calculateRoute</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">calculateRoute</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> from,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorwaypoint" title="class in com.here.sdk.venue.routing">IndoorWaypoint</a> to,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-indoorrouteoptions" title="class in com.here.sdk.venue.routing">IndoorRouteOptions</a> routeOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-venue-routing-calculateindoorroutecallback" title="interface in com.here.sdk.venue.routing">CalculateIndoorRouteCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously calculates a route inside a venue.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>from</code> - <p>A starting position of the route to calculate.</p></dd>
<dd><code>to</code> - <p>A destination position of the route to calculate.</p></dd>
<dd><code>routeOptions</code> - <p>Options specific for indoor route calculation, along with
     common route options.</p></dd>
<dd><code>callback</code> - <p>Callback object that will be invoked after route calculation.
     It is always invoked on the main thread.</p></dd>
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
