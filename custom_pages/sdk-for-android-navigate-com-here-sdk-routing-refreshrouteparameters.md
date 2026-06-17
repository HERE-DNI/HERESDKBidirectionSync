---
title: "RefreshRouteParameters (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-refreshrouteparameters"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RefreshRouteParameters.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.RefreshRouteParameters</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RefreshRouteParameters</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>This class provides the necessary information for refreshing a route from a
 specific location on it.</p></div>
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
<div class="col-first even-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#routeHandle">routeHandle</a></code></div>
<div class="col-last even-row-color">
<div class="block">The route handle holding the route to be refreshed.</div>
</div>
<div class="col-first odd-row-color"><code><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#startingPoint">startingPoint</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identify the new starting point of the route.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#startingSectionIndex">startingSectionIndex</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the index of the last traveled route section.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#traveledDistanceOnStartingSectionInMeters">traveledDistanceOnStartingSectionInMeters</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Provides an indication on how much of the starting section is already traveled.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.RouteHandle,int,int)">RefreshRouteParameters</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 int startingSectionIndex,
 int traveledDistanceOnStartingSectionInMeters)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a new instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing"><code>RefreshRouteParameters</code></a> with the point on the section of the route as a new starting point.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint)">RefreshRouteParameters</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint)</code></div>
<div class="col-last odd-row-color">
<div class="block">Create a new instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing"><code>RefreshRouteParameters</code></a> with the new starting point on the route.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,int,int)">RefreshRouteParameters</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int startingSectionIndex,
 int traveledDistanceOnStartingSectionInMeters)</code></div>
<div class="col-last even-row-color">
<div class="block">Create a new instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing"><code>RefreshRouteParameters</code></a> with the new starting point and the section position on the route.</div>
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
<section class="detail" id="routeHandle">
<h3>routeHandle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a></span> <span class="element-name">routeHandle</span></div>
<div class="block"><p>The route handle holding the route to be refreshed.</p></div>
</section>
</li>
<li>
<section class="detail" id="startingPoint">
<h3>startingPoint</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a></span> <span class="element-name">startingPoint</span></div>
<div class="block"><p>Identify the new starting point of the route. It should be of type <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypointtype#STOPOVER"><code>WaypointType.STOPOVER</code></a>.
 Otherwise, an <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated. Moreover, it should be very close to the
 original route specified with the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>. The location of this waypoint may by provided,
 for example, by a <code>RouteProgress</code> event. Since the new starting point is expected to be
 along the original route, the original route geometry is used to reach the remaining waypoints. The new route
 will not include the <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing"><code>Waypoint</code></a> items that lie behind the new starting point (i.e. the path that
 was already traveled). Plus, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getLengthInMeters()"><code>Route.getLengthInMeters()</code></a>, <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-route#getDuration()"><code>Route.getDuration()</code></a>, and similar
 values are from the new starting point to the destination. If the new waypoint is too far off the original
 route, the route refresh may fail and an <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#COULD_NOT_MATCH_ORIGIN"><code>RoutingError.COULD_NOT_MATCH_ORIGIN</code></a> error is triggered.
 In that case, an application may decide to calculate a new route from scratch.</p></div>
</section>
</li>
<li>
<section class="detail" id="startingSectionIndex">
<h3>startingSectionIndex</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">startingSectionIndex</span></div>
<div class="block"><p>Indicates the index of the last traveled route section. When it is provided, the previous sections are discarded
 from the refreshed route and the starting point is searched in the provided section. If the starting point
 is not found in that section an <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#COULD_NOT_MATCH_ORIGIN"><code>RoutingError.COULD_NOT_MATCH_ORIGIN</code></a> error is triggered.</p></div>
</section>
</li>
<li>
<section class="detail" id="traveledDistanceOnStartingSectionInMeters">
<h3>traveledDistanceOnStartingSectionInMeters</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a></span> <span class="element-name">traveledDistanceOnStartingSectionInMeters</span></div>
<div class="block"><p>Provides an indication on how much of the starting section is already traveled. The refresh route function
 would ignore the first part of the section. If it is provided with an invalid starting section index, an
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routingerror#INVALID_PARAMETER"><code>RoutingError.INVALID_PARAMETER</code></a> error is generated.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint)">
<h3>RefreshRouteParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteParameters</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint)</span></div>
<div class="block"><p>Create a new instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing"><code>RefreshRouteParameters</code></a> with the new starting point on the route.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingPoint</code> - <p>Identify the new starting point of the route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.RouteHandle,int,int)">
<h3>RefreshRouteParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteParameters</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 int startingSectionIndex,
 int traveledDistanceOnStartingSectionInMeters)</span></div>
<div class="block"><p>Create a new instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing"><code>RefreshRouteParameters</code></a> with the point on the section of the route as a new starting point.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingSectionIndex</code> - <p>Indicates the index of the last traveled route section.</p></dd>
<dd><code>traveledDistanceOnStartingSectionInMeters</code> - <p>Provides an indication on how much of the starting section is already traveled.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.routing.RouteHandle,com.here.sdk.routing.Waypoint,int,int)">
<h3>RefreshRouteParameters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RefreshRouteParameters</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing">RouteHandle</a> routeHandle,
 @NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-waypoint" title="class in com.here.sdk.routing">Waypoint</a> startingPoint,
 int startingSectionIndex,
 int traveledDistanceOnStartingSectionInMeters)</span></div>
<div class="block"><p>Create a new instance of <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-refreshrouteparameters" title="class in com.here.sdk.routing"><code>RefreshRouteParameters</code></a> with the new starting point and the section position on the route.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>routeHandle</code> - <p>The route handle holding the route to be refreshed.</p></dd>
<dd><code>startingPoint</code> - <p>Identify the new starting point of the route.</p></dd>
<dd><code>startingSectionIndex</code> - <p>Indicates the index of the last traveled route section.</p></dd>
<dd><code>traveledDistanceOnStartingSectionInMeters</code> - <p>Provides an indication on how much of the starting section is already traveled.</p></dd>
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
