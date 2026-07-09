---
title: "TrafficQueryError (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficQueryError.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>&gt;
<div className="inheritance">com.here.sdk.traffic.TrafficQueryError</div>
</div>
</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>&gt;</code>, <code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div className="type-signature"><span className="modifiers">public enum </span><span className="element-name type-name-label">TrafficQueryError</span>
<span className="extends-implements">extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>&gt;</span></div>
<div className="block"><p>Represents various errors that could occur from a traffic queries.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="inherited-list">

<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section className="constants-summary" id="enum-constant-summary">

<div className="caption"><span>Enum Constants</span></div>
<div className="summary-table two-column-summary">


<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#AUTHENTICATION_FAILED">AUTHENTICATION_FAILED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Incident query/flow operation is not authenticated.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#BAD_REQUEST">BAD_REQUEST</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Bad request.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#FAILED_TO_RETRIEVE_RESULT">FAILED_TO_RETRIEVE_RESULT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Failed to retrieve result since the server has returned an error or invalid result
 that couldn't be processed correctly.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#FORBIDDEN">FORBIDDEN</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The provided credentials don't give access to the requested resource.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#HTTP_ERROR">HTTP_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Network request error.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INCIDENT_ID_NOT_FOUND">INCIDENT_ID_NOT_FOUND</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Incident ID is not found in the system.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INTERNAL_ERROR">INTERNAL_ERROR</a></code></div>
<div className="col-last even-row-color">
<div className="block">Internal error.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INVALID_FILTER_OPTIONS">INVALID_FILTER_OPTIONS</a></code></div>
<div className="col-last odd-row-color">
<div className="block">One or several filter options are invalid.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INVALID_GEOMETRY">INVALID_GEOMETRY</a></code></div>
<div className="col-last even-row-color">
<div className="block">Invalid geometry: bounding box, circle, or corridor.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INVALID_IN">INVALID_IN</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Invalid "in" parameter: wrong type, missing or invalid "in".</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INVALID_INCIDENT">INVALID_INCIDENT</a></code></div>
<div className="col-last even-row-color">
<div className="block">Invalid incident ID, type, earliestStartTime or latestEndTime.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#INVALID_PARAMETER">INVALID_PARAMETER</a></code></div>
<div className="col-last odd-row-color">
<div className="block">One or more input parameters in the query is not valid.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#OFFLINE">OFFLINE</a></code></div>
<div className="col-last even-row-color">
<div className="block">The device has no internet connection.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#OPERATION_CANCELLED">OPERATION_CANCELLED</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Operation cancelled.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#PROXY_AUTHENTICATION_FAILED">PROXY_AUTHENTICATION_FAILED</a></code></div>
<div className="col-last even-row-color">
<div className="block">Proxy is not authenticated.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#PROXY_SERVER_UNREACHABLE">PROXY_SERVER_UNREACHABLE</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Proxy server unreachable.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#SERVER_UNREACHABLE">SERVER_UNREACHABLE</a></code></div>
<div className="col-last even-row-color">
<div className="block">Server unreachable.</div>
</div>
<div className="col-first odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#TIMED_OUT">TIMED_OUT</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The request timed out.</div>
</div>
<div className="col-first even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror#TOO_MANY_REQUESTS">TOO_MANY_REQUESTS</a></code></div>
<div className="col-last even-row-color">
<div className="block">Server has received an excessive number of requests from client within a specific timeframe
 and client should slow down or wait before sending more requests.</div>
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
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section className="constant-details" id="enum-constant-detail">

<ul className="member-list">
<li>
<section className="detail" id="FAILED_TO_RETRIEVE_RESULT">
<h3>FAILED_TO_RETRIEVE_RESULT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">FAILED_TO_RETRIEVE_RESULT</span></div>
<div className="block"><p>Failed to retrieve result since the server has returned an error or invalid result
 that couldn't be processed correctly.</p></div>
</section>
</li>
<li>
<section className="detail" id="AUTHENTICATION_FAILED">
<h3>AUTHENTICATION_FAILED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">AUTHENTICATION_FAILED</span></div>
<div className="block"><p>Incident query/flow operation is not authenticated. Check your credentials.</p></div>
</section>
</li>
<li>
<section className="detail" id="FORBIDDEN">
<h3>FORBIDDEN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">FORBIDDEN</span></div>
<div className="block"><p>The provided credentials don't give access to the requested resource.</p></div>
</section>
</li>
<li>
<section className="detail" id="SERVER_UNREACHABLE">
<h3>SERVER_UNREACHABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">SERVER_UNREACHABLE</span></div>
<div className="block"><p>Server unreachable.</p></div>
</section>
</li>
<li>
<section className="detail" id="TIMED_OUT">
<h3>TIMED_OUT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">TIMED_OUT</span></div>
<div className="block"><p>The request timed out.</p></div>
</section>
</li>
<li>
<section className="detail" id="OFFLINE">
<h3>OFFLINE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">OFFLINE</span></div>
<div className="block"><p>The device has no internet connection.</p></div>
</section>
</li>
<li>
<section className="detail" id="HTTP_ERROR">
<h3>HTTP_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">HTTP_ERROR</span></div>
<div className="block"><p>Network request error.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_IN">
<h3>INVALID_IN</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INVALID_IN</span></div>
<div className="block"><p>Invalid "in" parameter: wrong type, missing or invalid "in".</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_GEOMETRY">
<h3>INVALID_GEOMETRY</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INVALID_GEOMETRY</span></div>
<div className="block"><p>Invalid geometry: bounding box, circle, or corridor.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_INCIDENT">
<h3>INVALID_INCIDENT</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INVALID_INCIDENT</span></div>
<div className="block"><p>Invalid incident ID, type, earliestStartTime or latestEndTime.</p></div>
</section>
</li>
<li>
<section className="detail" id="INCIDENT_ID_NOT_FOUND">
<h3>INCIDENT_ID_NOT_FOUND</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INCIDENT_ID_NOT_FOUND</span></div>
<div className="block"><p>Incident ID is not found in the system.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_FILTER_OPTIONS">
<h3>INVALID_FILTER_OPTIONS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INVALID_FILTER_OPTIONS</span></div>
<div className="block"><p>One or several filter options are invalid.</p></div>
</section>
</li>
<li>
<section className="detail" id="INVALID_PARAMETER">
<h3>INVALID_PARAMETER</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INVALID_PARAMETER</span></div>
<div className="block"><p>One or more input parameters in the query is not valid.</p></div>
</section>
</li>
<li>
<section className="detail" id="INTERNAL_ERROR">
<h3>INTERNAL_ERROR</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">INTERNAL_ERROR</span></div>
<div className="block"><p>Internal error.</p></div>
</section>
</li>
<li>
<section className="detail" id="OPERATION_CANCELLED">
<h3>OPERATION_CANCELLED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">OPERATION_CANCELLED</span></div>
<div className="block"><p>Operation cancelled.</p></div>
</section>
</li>
<li>
<section className="detail" id="PROXY_AUTHENTICATION_FAILED">
<h3>PROXY_AUTHENTICATION_FAILED</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">PROXY_AUTHENTICATION_FAILED</span></div>
<div className="block"><p>Proxy is not authenticated. Check your proxy credentials.</p></div>
</section>
</li>
<li>
<section className="detail" id="PROXY_SERVER_UNREACHABLE">
<h3>PROXY_SERVER_UNREACHABLE</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">PROXY_SERVER_UNREACHABLE</span></div>
<div className="block"><p>Proxy server unreachable. Error indicates a problem with a proxy server's accessibility or connectivity.</p></div>
</section>
</li>
<li>
<section className="detail" id="BAD_REQUEST">
<h3>BAD_REQUEST</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">BAD_REQUEST</span></div>
<div className="block"><p>Bad request. Error indicates server could not understand or process the request made by the client because
 the request itself was malformed or incorrect.</p></div>
</section>
</li>
<li>
<section className="detail" id="TOO_MANY_REQUESTS">
<h3>TOO_MANY_REQUESTS</h3>
<div className="member-signature"><span className="modifiers">public static final</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">TOO_MANY_REQUESTS</span></div>
<div className="block"><p>Server has received an excessive number of requests from client within a specific timeframe
 and client should slow down or wait before sending more requests.</p></div>
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
<section className="detail" id="values()">
<h3>values</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a>[]</span> <span className="element-name">values</span>()</div>
<div className="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl className="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div className="member-signature"><span className="modifiers">public static</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a></span> <span className="element-name">valueOf</span><wbr/><span className="parameters">(<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div className="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
