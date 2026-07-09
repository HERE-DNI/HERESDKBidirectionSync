---
title: "DynamicRoutingListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutinglistener"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- DynamicRoutingListener.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.trafficawarenavigation</a></div>

</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public interface </span><span className="element-name type-name-label">DynamicRoutingListener</span></div>
<div className="block"><p>This interface should be implemented in order to
 receive notifications about the new route via the <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengine" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngine</code></a>.</p></div>
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
<section className="detail" id="onBetterRouteFound(com.here.sdk.routing.Route,int,int)">
<h3>onBetterRouteFound</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onBetterRouteFound</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-route" title="class in com.here.sdk.routing">Route</a> newRoute,
 int etaDifferenceInSeconds,
 int distanceDifferenceInMeters)</span></div>
<div className="block"><p>This event is issued when a better route could be found,
 as defined by <a href="sdk-for-android-navigate-com-here-sdk-trafficawarenavigation-dynamicroutingengineoptions" title="class in com.here.sdk.trafficawarenavigation"><code>DynamicRoutingEngineOptions</code></a>.
 To find a better route, two routes are calculated.
 The updated current route: A route that is calculated via the route specified.
 The dynamic route: A route that starts at the current position on the route specified
 and passes through the remaining waypoints.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>newRoute</code> - <p>The newly calculated route with the remaining waypoints starting from the
     current location.</p></dd>
<dd><code>etaDifferenceInSeconds</code> - <p>The difference in seconds:
     eta of the current updated route - eta of the dynamic route.</p></dd>
<dd><code>distanceDifferenceInMeters</code> - <p>The difference in meters:
     distance of the current updated route - distance of the dynamic route.
     The value can be negative in case the current updated route has
     a shorter distance, but its now assumed to be longer than the dynamic route.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="onRoutingError(com.here.sdk.routing.RoutingError)">
<h3>onRoutingError</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onRoutingError</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a> routingError)</span></div>
<div className="block"><p>This event is issued when an error occurred.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>routingError</code> - <p>Routing error</p></dd>
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
