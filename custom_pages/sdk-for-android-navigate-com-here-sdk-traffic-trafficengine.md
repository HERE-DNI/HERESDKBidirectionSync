---
title: "TrafficEngine (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-traffic-trafficengine"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- TrafficEngine.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.traffic</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.traffic.TrafficEngine</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">TrafficEngine</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Use the TrafficEngine to get information about current traffic flow and incidents in an area
 specified by <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core"><code>GeoBox</code></a>, <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core"><code>GeoCircle</code></a>, or <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core"><code>GeoCorridor</code></a>.
 Provides optional parameters given in <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsqueryoptions" title="class in com.here.sdk.traffic"><code>TrafficIncidentsQueryOptions</code></a> and <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowqueryoptions" title="class in com.here.sdk.traffic"><code>TrafficFlowQueryOptions</code></a> to filter the result.
 By default, incidents are localized based on their geographical
 location. You can override that behavior by specifying the
 desired language that should be used for the incidents description and summary.
 The resulting traffic data contains information on incident
 types such as congestion, construction for road works, road hazard,
 road closure, weather updates for road condition, lane restriction
 and others.
 Traffic data is fetched online to get the most precise and freshest data available.
 In offline mode, live traffic data can be fetched using the traffic pass-through features.
 See <a href="sdk-for-android-navigate-sdknativeengine#getPassThroughFeatures()"><code>SDKNativeEngine.getPassThroughFeatures()</code></a></p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficengine#%3Cinit%3E()">TrafficEngine</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-traffic-trafficengine#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">TrafficEngine</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
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
<section className="detail" id="&lt;init&gt;()">
<h3>TrafficEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TrafficEngine</span>()
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
<h3>TrafficEngine</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">TrafficEngine</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
              throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>An SDKEngine instance.</p></dd>
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
<section className="detail" id="queryForIncidents(com.here.sdk.core.GeoBox,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)">
<h3>queryForIncidents</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">queryForIncidents</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsqueryoptions" title="class in com.here.sdk.traffic">TrafficIncidentsQueryOptions</a> queryOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsquerycallback" title="interface in com.here.sdk.traffic">TrafficIncidentsQueryCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic incidents using a bounding box as a filter.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>boxArea</code> - <p>The bounding box area to search for traffic incidents.
     The maximum width and height for a bounding box filter is 1 degree.</p></dd>
<dd><code>queryOptions</code> - <p>The options which are specific for incidents query.</p></dd>
<dd><code>callback</code> - <p>It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="queryForIncidents(com.here.sdk.core.GeoCircle,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)">
<h3>queryForIncidents</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">queryForIncidents</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsqueryoptions" title="class in com.here.sdk.traffic">TrafficIncidentsQueryOptions</a> queryOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsquerycallback" title="interface in com.here.sdk.traffic">TrafficIncidentsQueryCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic incidents using a circle as a filter.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>circleArea</code> - <p>The circle area to search for traffic incidents.
     The maximum radius of the circle filter is 50000 meters.</p></dd>
<dd><code>queryOptions</code> - <p>The options which are specific for incidents query.</p></dd>
<dd><code>callback</code> - <p>It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="queryForIncidents(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficIncidentsQueryOptions,com.here.sdk.traffic.TrafficIncidentsQueryCallback)">
<h3>queryForIncidents</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">queryForIncidents</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsqueryoptions" title="class in com.here.sdk.traffic">TrafficIncidentsQueryOptions</a> queryOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentsquerycallback" title="interface in com.here.sdk.traffic">TrafficIncidentsQueryCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic incidents by a corridor as a filter.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>corridorArea</code> - <p>The corridor box to search for traffic incidents.
     The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.
     If the number of points in corridor is greater than 300 then request is split into smaller ones and results are
     aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.
     To reduce number of points in the corridor use <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier" title="class in com.here.sdk.core"><code>PolylineSimplifier</code></a>.
     If no <code>GeoCorridor.half_width_in_meters</code> is specified, the default value is used. The default value is 30 meters.</p></dd>
<dd><code>queryOptions</code> - <p>The options which are specific for incidents query.</p></dd>
<dd><code>callback</code> - <p>It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="lookupIncident(java.lang.String,com.here.sdk.traffic.TrafficIncidentLookupOptions,com.here.sdk.traffic.TrafficIncidentLookupCallback)">
<h3>lookupIncident</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">lookupIncident</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> originalId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentlookupoptions" title="class in com.here.sdk.traffic">TrafficIncidentLookupOptions</a> lookupOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficincidentlookupcallback" title="interface in com.here.sdk.traffic">TrafficIncidentLookupCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic incident by the original id.
 See <a href="sdk-for-android-navigate-trafficincident#getOriginalId()"><code>TrafficIncident.getOriginalId()</code></a> for more information.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>originalId</code> - <p>The requested incident original id.</p></dd>
<dd><code>lookupOptions</code> - <p>The options which are specific for the incident lookup query.</p></dd>
<dd><code>callback</code> - <p>The callback object that will be invoked after the incident lookup query.
     It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="queryForFlow(com.here.sdk.core.GeoBox,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)">
<h3>queryForFlow</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">queryForFlow</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowqueryoptions" title="class in com.here.sdk.traffic">TrafficFlowQueryOptions</a> queryOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowquerycallback" title="interface in com.here.sdk.traffic">TrafficFlowQueryCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic flow using a bounding box as a filter.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>boxArea</code> - <p>The bounding box area to search for traffic flow.</p></dd>
<dd><code>queryOptions</code> - <p>The options which are specific for flow query.</p></dd>
<dd><code>callback</code> - <p>It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="queryForFlow(com.here.sdk.core.GeoCircle,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)">
<h3>queryForFlow</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">queryForFlow</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowqueryoptions" title="class in com.here.sdk.traffic">TrafficFlowQueryOptions</a> queryOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowquerycallback" title="interface in com.here.sdk.traffic">TrafficFlowQueryCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic flow using a circle as a filter.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>circleArea</code> - <p>The circle area to search for traffic flow.
     The maximum radius of the circle filter is 50000 meters.</p></dd>
<dd><code>queryOptions</code> - <p>The options which are specific for flow query.</p></dd>
<dd><code>callback</code> - <p>It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="queryForFlow(com.here.sdk.core.GeoCorridor,com.here.sdk.traffic.TrafficFlowQueryOptions,com.here.sdk.traffic.TrafficFlowQueryCallback)">
<h3>queryForFlow</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">queryForFlow</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowqueryoptions" title="class in com.here.sdk.traffic">TrafficFlowQueryOptions</a> queryOptions,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-traffic-trafficflowquerycallback" title="interface in com.here.sdk.traffic">TrafficFlowQueryCallback</a> callback)</span></div>
<div className="block"><p>Asynchronously queries for traffic flow by a corridor as a filter.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>corridorArea</code> - <p>The corridor box to search for traffic flow.
     The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.
     Maximum number of points in the corridor is 300.
     To reduce number of points in the corridor use <a href="sdk-for-android-navigate-com-here-sdk-core-polylinesimplifier" title="class in com.here.sdk.core"><code>PolylineSimplifier</code></a>.
     If no <code>GeoCorridor.half_width_in_meters</code> is specified, the default value is used. The default value is 30 meters.</p></dd>
<dd><code>queryOptions</code> - <p>The options which are specific for flow query.</p></dd>
<dd><code>callback</code> - <p>It is always invoked on the main thread.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
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
