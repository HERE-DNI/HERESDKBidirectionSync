---
title: "SegmentData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SegmentData.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapdata.SegmentData</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SegmentData</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Contains the requested information for a segment
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
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
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getOcmSegmentId()">
<h3>getOcmSegmentId</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a></span> <span className="element-name">getOcmSegmentId</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata"><code>OCMSegmentId</code></a> object representing the the segment.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata"><code>OCMSegmentId</code></a> object representing the segment</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSegmentReference()">
<h3>getSegmentReference</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span className="element-name">getSegmentReference</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> object representing the the segment.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-routing-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> object representing the segment</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPolyline()">
<h3>getPolyline</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span className="element-name">getPolyline</span>()</div>
<div className="block"><p>Gets the <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this segment.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-com-here-sdk-core-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">int</span> <span className="element-name">getLengthInMeters</span>()</div>
<div className="block"><p>Gets the length of this segment in meters.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The length of this segment in meters. This information is based on map data.
     It can differ from the length of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata#getPolyline()"><code>getPolyline()</code></a> due to
     approximations of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSpans()">
<h3>getSpans</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata" title="class in com.here.sdk.mapdata">SegmentSpanData</a>&gt;</span> <span className="element-name">getSpans</span>()</div>
<div className="block"><p>Gets the list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata" title="class in com.here.sdk.mapdata"><code>SegmentSpanData</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentspandata" title="class in com.here.sdk.mapdata"><code>SegmentSpanData</code></a> of the given segment for the
     requested attributes
     <strong>Note:</strong> If no span attributes is requested, the list will be empty.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTrafficSignals()">
<h3>getTrafficSignals</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal" title="class in com.here.sdk.mapdata">TrafficSignal</a>&gt;</span> <span className="element-name">getTrafficSignals</span>()</div>
<div className="block"><p>Gets the list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal" title="class in com.here.sdk.mapdata"><code>TrafficSignal</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignal" title="class in com.here.sdk.mapdata"><code>TrafficSignal</code></a> of the given segment.
     Returns an empty list if no data is found.
     Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTrafficSignals"><code>SegmentDataLoaderOptions.loadTrafficSignals</code></a> is set to <code>false</code>.
     The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-trafficsignallocation" title="enum class in com.here.sdk.mapdata"><code>TrafficSignalLocation</code></a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead.
     The <a href="sdk-for-android-navigate-trafficsignal#offsetInMeters"><code>TrafficSignal.offsetInMeters</code></a> is the location along the segment,
     while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRoadSigns()">
<h3>getRoadSigns</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign" title="class in com.here.sdk.navigation">RoadSign</a>&gt;</span> <span className="element-name">getRoadSigns</span>()</div>
<div className="block"><p>Gets the list of <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign" title="class in com.here.sdk.navigation"><code>RoadSign</code></a>.
 Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRoadSigns"><code>SegmentDataLoaderOptions.loadRoadSigns</code></a> is set to <code>false</code>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsign" title="class in com.here.sdk.navigation"><code>RoadSign</code></a> of the given segment.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getRailwayCrossings()">
<h3>getRailwayCrossings</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing" title="class in com.here.sdk.mapdata">RailwayCrossing</a>&gt;</span> <span className="element-name">getRailwayCrossings</span>()</div>
<div className="block"><p>Gets the list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing" title="class in com.here.sdk.mapdata"><code>RailwayCrossing</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-railwaycrossing" title="class in com.here.sdk.mapdata"><code>RailwayCrossing</code></a> of the given segment.
     Returns an empty list if no data is found.
     Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRailwayCrossings"><code>SegmentDataLoaderOptions.loadRailwayCrossings</code></a> is set to <code>false</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTollPoints()">
<h3>getTollPoints</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollpoint" title="class in com.here.sdk.mapdata">TollPoint</a>&gt;</span> <span className="element-name">getTollPoints</span>()</div>
<div className="block"><p>Gets the list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollpoint" title="class in com.here.sdk.mapdata"><code>TollPoint</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-com-here-sdk-mapdata-tollpoint" title="class in com.here.sdk.mapdata"><code>TollPoint</code></a> of the given segment.
     Returns an empty list if no data is found.
     Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTollPoints"><code>SegmentDataLoaderOptions.loadTollPoints</code></a> is set to <code>false</code>
     or the <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata"><code>SegmentData</code></a> is not initialized using <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a>.</p></dd>
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
