---
title: "RoutingError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-routingerror"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoutingError.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a>&gt;
<div class="inheritance">com.here.sdk.routing.RoutingError</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">RoutingError</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a>&gt;</span></div>
<div class="block"><p>Specifies possible errors that may result from the calculation of a route.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#ACTIVE_MAP_UPDATE">ACTIVE_MAP_UPDATE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route cannot be calculated due to active map update.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#AUTHENTICATION_FAILED">AUTHENTICATION_FAILED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Routing operation is not authenticated.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_DESTINATION">COULD_NOT_MATCH_DESTINATION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Destination waypoint could not be matched to a road network.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#COULD_NOT_MATCH_ORIGIN">COULD_NOT_MATCH_ORIGIN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Origin waypoint could not be matched to a road network.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#EXCEEDED_USAGE_LIMIT">EXCEEDED_USAGE_LIMIT</a></code></div>
<div class="col-last even-row-color">
<div class="block">Credentials exceeded the allowed requests limit.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#FAILED_ROUTE_HANDLE_CREATION">FAILED_ROUTE_HANDLE_CREATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">No RouteHandle was created.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#FORBIDDEN">FORBIDDEN</a></code></div>
<div class="col-last even-row-color">
<div class="block">The provided credentials don't give access to the requested resource.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#HTTP_ERROR">HTTP_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A general network request error.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#IMPORT_FAILED">IMPORT_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">No route section was found for imported waypoints.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INTERNAL_ERROR">INTERNAL_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Generic internal error.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#INVALID_PARAMETER">INVALID_PARAMETER</a></code></div>
<div class="col-last even-row-color">
<div class="block">An invalid input parameter.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#NO_ISOLINE_FOUND">NO_ISOLINE_FOUND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">No isoline can be calculated for the given input.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#NO_REACHABLE_CHARGING_STATION_FOUND">NO_REACHABLE_CHARGING_STATION_FOUND</a></code></div>
<div class="col-last even-row-color">
<div class="block">Initial charge is not enough to reach any known charging stations.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#NO_ROUTE_FOUND">NO_ROUTE_FOUND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">No route can be calculated for the given input.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#NO_ROUTE_HANDLE">NO_ROUTE_HANDLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">The route has no <a href="sdk-for-android-navigate-route#getRouteHandle()"><code>Route.getRouteHandle()</code></a>, but it was used for a feature that requires one.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#OFFLINE">OFFLINE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The device has no internet connection.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#OPERATION_CANCELLED">OPERATION_CANCELLED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Operation cancelled.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#PARSING_ERROR">PARSING_ERROR</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Error while parsing route data.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#PROXY_AUTHENTICATION_FAILED">PROXY_AUTHENTICATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Proxy is not authenticated.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#PROXY_SERVER_UNREACHABLE">PROXY_SERVER_UNREACHABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Proxy server unreachable.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#ROUTE_CALCULATION_FAILED">ROUTE_CALCULATION_FAILED</a></code></div>
<div class="col-last even-row-color">
<div class="block">Calculation did not succeed.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#ROUTE_LENGTH_LIMIT_EXCEEDED">ROUTE_LENGTH_LIMIT_EXCEEDED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Distance between waypoints is too large for current options.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#SERVER_UNREACHABLE">SERVER_UNREACHABLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Routing server is unreachable.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#TIMED_OUT">TIMED_OUT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The request timed out.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING">VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route handle decoding failed due to forbidden segments for the specified transport mode.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-routingerror#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="INTERNAL_ERROR">
<h3>INTERNAL_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">INTERNAL_ERROR</span></div>
<div class="block"><p>Generic internal error.</p></div>
</section>
</li>
<li>
<section class="detail" id="INVALID_PARAMETER">
<h3>INVALID_PARAMETER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">INVALID_PARAMETER</span></div>
<div class="block"><p>An invalid input parameter.</p></div>
</section>
</li>
<li>
<section class="detail" id="SERVER_UNREACHABLE">
<h3>SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">SERVER_UNREACHABLE</span></div>
<div class="block"><p>Routing server is unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="HTTP_ERROR">
<h3>HTTP_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">HTTP_ERROR</span></div>
<div class="block"><p>A general network request error.</p></div>
</section>
</li>
<li>
<section class="detail" id="AUTHENTICATION_FAILED">
<h3>AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Routing operation is not authenticated. Check your credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="FORBIDDEN">
<h3>FORBIDDEN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">FORBIDDEN</span></div>
<div class="block"><p>The provided credentials don't give access to the requested resource.</p></div>
</section>
</li>
<li>
<section class="detail" id="EXCEEDED_USAGE_LIMIT">
<h3>EXCEEDED_USAGE_LIMIT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">EXCEEDED_USAGE_LIMIT</span></div>
<div class="block"><p>Credentials exceeded the allowed requests limit.</p></div>
</section>
</li>
<li>
<section class="detail" id="PARSING_ERROR">
<h3>PARSING_ERROR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">PARSING_ERROR</span></div>
<div class="block"><p>Error while parsing route data. This is not expected to happen. Try updating to the newest
 version of the SDK. If the problem persists, please report a bug in the SDK.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_ROUTE_FOUND">
<h3>NO_ROUTE_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">NO_ROUTE_FOUND</span></div>
<div class="block"><p>No route can be calculated for the given input.</p></div>
</section>
</li>
<li>
<section class="detail" id="TIMED_OUT">
<h3>TIMED_OUT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">TIMED_OUT</span></div>
<div class="block"><p>The request timed out.</p></div>
</section>
</li>
<li>
<section class="detail" id="OFFLINE">
<h3>OFFLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">OFFLINE</span></div>
<div class="block"><p>The device has no internet connection.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_ISOLINE_FOUND">
<h3>NO_ISOLINE_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">NO_ISOLINE_FOUND</span></div>
<div class="block"><p>No isoline can be calculated for the given input.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_ROUTE_HANDLE">
<h3>NO_ROUTE_HANDLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">NO_ROUTE_HANDLE</span></div>
<div class="block"><p>The route has no <a href="sdk-for-android-navigate-route#getRouteHandle()"><code>Route.getRouteHandle()</code></a>, but it was used for a feature that requires one.
 Consider to recalculate the route with a route handle. See <a href="sdk-for-android-navigate-routeoptions#enableRouteHandle"><code>RouteOptions.enableRouteHandle</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="OPERATION_CANCELLED">
<h3>OPERATION_CANCELLED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">OPERATION_CANCELLED</span></div>
<div class="block"><p>Operation cancelled.</p></div>
</section>
</li>
<li>
<section class="detail" id="COULD_NOT_MATCH_DESTINATION">
<h3>COULD_NOT_MATCH_DESTINATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">COULD_NOT_MATCH_DESTINATION</span></div>
<div class="block"><p>Destination waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded.
 When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.</p></div>
</section>
</li>
<li>
<section class="detail" id="COULD_NOT_MATCH_ORIGIN">
<h3>COULD_NOT_MATCH_ORIGIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">COULD_NOT_MATCH_ORIGIN</span></div>
<div class="block"><p>Origin waypoint could not be matched to a road network. Either this waypoint is far from road network or not enough data has been downloaded.
 When both, origin and destination, cannot be matched, then the origin waypoint error will take precedence.</p></div>
</section>
</li>
<li>
<section class="detail" id="FAILED_ROUTE_HANDLE_CREATION">
<h3>FAILED_ROUTE_HANDLE_CREATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">FAILED_ROUTE_HANDLE_CREATION</span></div>
<div class="block"><p>No RouteHandle was created.</p></div>
</section>
</li>
<li>
<section class="detail" id="IMPORT_FAILED">
<h3>IMPORT_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">IMPORT_FAILED</span></div>
<div class="block"><p>No route section was found for imported waypoints.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_REACHABLE_CHARGING_STATION_FOUND">
<h3>NO_REACHABLE_CHARGING_STATION_FOUND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">NO_REACHABLE_CHARGING_STATION_FOUND</span></div>
<div class="block"><p>Initial charge is not enough to reach any known charging stations.</p></div>
</section>
</li>
<li>
<section class="detail" id="ROUTE_CALCULATION_FAILED">
<h3>ROUTE_CALCULATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">ROUTE_CALCULATION_FAILED</span></div>
<div class="block"><p>Calculation did not succeed.</p></div>
</section>
</li>
<li>
<section class="detail" id="ROUTE_LENGTH_LIMIT_EXCEEDED">
<h3>ROUTE_LENGTH_LIMIT_EXCEEDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">ROUTE_LENGTH_LIMIT_EXCEEDED</span></div>
<div class="block"><p>Distance between waypoints is too large for current options.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING">
<h3>VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">VIOLATED_TRANSPORT_MODE_IN_ROUTE_HANDLE_DECODING</span></div>
<div class="block"><p>Route handle decoding failed due to forbidden segments for the specified transport mode.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_AUTHENTICATION_FAILED">
<h3>PROXY_AUTHENTICATION_FAILED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">PROXY_AUTHENTICATION_FAILED</span></div>
<div class="block"><p>Proxy is not authenticated. Check your proxy credentials.</p></div>
</section>
</li>
<li>
<section class="detail" id="PROXY_SERVER_UNREACHABLE">
<h3>PROXY_SERVER_UNREACHABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">PROXY_SERVER_UNREACHABLE</span></div>
<div class="block"><p>Proxy server unreachable.</p></div>
</section>
</li>
<li>
<section class="detail" id="ACTIVE_MAP_UPDATE">
<h3>ACTIVE_MAP_UPDATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">ACTIVE_MAP_UPDATE</span></div>
<div class="block"><p>Route cannot be calculated due to active map update. Please, repeat the request after map update is finished successfully.</p></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-routingerror" title="enum class in com.here.sdk.routing">RoutingError</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
