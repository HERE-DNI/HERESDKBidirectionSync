---
title: "TrafficIncidentsQueryCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsquerycallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficIncidentsQueryCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">TrafficIncidentsQueryCallback</span></div>
<div className="block"><p>Callback passed to <a href="sdk-for-android-navigate-trafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)"><code>TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)</code></a>.
 The method will be called on the main thread when a search call has been completed.
 The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
 The second argument is the list of incidents in the case of the success. It is <code>null</code> in case of an error.</p></div>
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
<section className="detail" id="onTrafficIncidentsFetched(com.here.sdk.traffic.TrafficQueryError,java.util.List)">
<h3>onTrafficIncidentsFetched</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onTrafficIncidentsFetched</span><wbr/><span className="parameters">(@Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficqueryerror" title="enum class in com.here.sdk.traffic">TrafficQueryError</a> queryError,
 @Nullable
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincident" title="class in com.here.sdk.traffic">TrafficIncident</a>&gt; result)</span></div>
<div className="block"><p>Callback passed to <a href="sdk-for-android-navigate-trafficengine#queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)"><code>TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCallback)</code></a>.
 The method will be called on the main thread when a search call has been completed.
 The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
 The second argument is the list of incidents in the case of the success. It is <code>null</code> in case of an error.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>queryError</code> - <p>The error in the case of the failure. It is <code>null</code> for an operation that succeeds.</p></dd>
<dd><code>result</code> - <p>The list of incidents in the case of the success. It is <code>null</code> in case of an error.</p></dd>
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
