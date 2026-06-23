---
title: "SegmentData (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SegmentData.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapdata.SegmentData</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentData</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Contains the requested information for a segment
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getLengthInMeters()">getLengthInMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of this segment in meters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getOcmSegmentId()">getOcmSegmentId</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata"><code>OCMSegmentId</code></a> object representing the the segment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getPolyline()">getPolyline</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this segment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-railwaycrossing" title="class in com.here.sdk.mapdata">RailwayCrossing</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRailwayCrossings()">getRailwayCrossings</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of <a href="sdk-for-android-navigate-railwaycrossing" title="class in com.here.sdk.mapdata"><code>RailwayCrossing</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-roadsign" title="class in com.here.sdk.navigation">RoadSign</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getRoadSigns()">getRoadSigns</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of <a href="sdk-for-android-navigate-roadsign" title="class in com.here.sdk.navigation"><code>RoadSign</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSegmentReference()">getSegmentReference</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> object representing the the segment.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-segmentspandata" title="class in com.here.sdk.mapdata">SegmentSpanData</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSpans()">getSpans</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of <a href="sdk-for-android-navigate-segmentspandata" title="class in com.here.sdk.mapdata"><code>SegmentSpanData</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-tollpoint" title="class in com.here.sdk.mapdata">TollPoint</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTollPoints()">getTollPoints</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of <a href="sdk-for-android-navigate-tollpoint" title="class in com.here.sdk.mapdata"><code>TollPoint</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-trafficsignal" title="class in com.here.sdk.mapdata">TrafficSignal</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getTrafficSignals()">getTrafficSignals</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of <a href="sdk-for-android-navigate-trafficsignal" title="class in com.here.sdk.mapdata"><code>TrafficSignal</code></a>.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getOcmSegmentId()">
<h3>getOcmSegmentId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a></span> <span class="element-name">getOcmSegmentId</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata"><code>OCMSegmentId</code></a> object representing the the segment.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata"><code>OCMSegmentId</code></a> object representing the segment</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSegmentReference()">
<h3>getSegmentReference</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">getSegmentReference</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> object representing the the segment.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-segmentreference" title="class in com.here.sdk.routing"><code>SegmentReference</code></a> object representing the segment</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPolyline()">
<h3>getPolyline</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getPolyline</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this segment.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-navigate-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()</div>
<div class="block"><p>Gets the length of this segment in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of this segment in meters. This information is based on map data.
     It can differ from the length of <a href="sdk-for-android-navigate-index#getPolyline()"><code>getPolyline()</code></a> due to
     approximations of the polyline.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpans()">
<h3>getSpans</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-segmentspandata" title="class in com.here.sdk.mapdata">SegmentSpanData</a>&gt;</span> <span class="element-name">getSpans</span>()</div>
<div class="block"><p>Gets the list of <a href="sdk-for-android-navigate-segmentspandata" title="class in com.here.sdk.mapdata"><code>SegmentSpanData</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-segmentspandata" title="class in com.here.sdk.mapdata"><code>SegmentSpanData</code></a> of the given segment for the
     requested attributes
     <strong>Note:</strong> If no span attributes is requested, the list will be empty.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficSignals()">
<h3>getTrafficSignals</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-trafficsignal" title="class in com.here.sdk.mapdata">TrafficSignal</a>&gt;</span> <span class="element-name">getTrafficSignals</span>()</div>
<div class="block"><p>Gets the list of <a href="sdk-for-android-navigate-trafficsignal" title="class in com.here.sdk.mapdata"><code>TrafficSignal</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-trafficsignal" title="class in com.here.sdk.mapdata"><code>TrafficSignal</code></a> of the given segment.
     Returns an empty list if no data is found.
     Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTrafficSignals"><code>SegmentDataLoaderOptions.loadTrafficSignals</code></a> is set to <code>false</code>.
     The <a href="sdk-for-android-navigate-trafficsignallocation" title="enum class in com.here.sdk.mapdata"><code>TrafficSignalLocation</code></a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead.
     The <a href="sdk-for-android-navigate-trafficsignal#offsetInMeters"><code>TrafficSignal.offsetInMeters</code></a> is the location along the segment,
     while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadSigns()">
<h3>getRoadSigns</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-roadsign" title="class in com.here.sdk.navigation">RoadSign</a>&gt;</span> <span class="element-name">getRoadSigns</span>()</div>
<div class="block"><p>Gets the list of <a href="sdk-for-android-navigate-roadsign" title="class in com.here.sdk.navigation"><code>RoadSign</code></a>.
 </p><p>Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRoadSigns"><code>SegmentDataLoaderOptions.loadRoadSigns</code></a> is set to <code>false</code>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-roadsign" title="class in com.here.sdk.navigation"><code>RoadSign</code></a> of the given segment.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRailwayCrossings()">
<h3>getRailwayCrossings</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-railwaycrossing" title="class in com.here.sdk.mapdata">RailwayCrossing</a>&gt;</span> <span class="element-name">getRailwayCrossings</span>()</div>
<div class="block"><p>Gets the list of <a href="sdk-for-android-navigate-railwaycrossing" title="class in com.here.sdk.mapdata"><code>RailwayCrossing</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-railwaycrossing" title="class in com.here.sdk.mapdata"><code>RailwayCrossing</code></a> of the given segment.
     Returns an empty list if no data is found.
     Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadRailwayCrossings"><code>SegmentDataLoaderOptions.loadRailwayCrossings</code></a> is set to <code>false</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTollPoints()">
<h3>getTollPoints</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-tollpoint" title="class in com.here.sdk.mapdata">TollPoint</a>&gt;</span> <span class="element-name">getTollPoints</span>()</div>
<div class="block"><p>Gets the list of <a href="sdk-for-android-navigate-tollpoint" title="class in com.here.sdk.mapdata"><code>TollPoint</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of <a href="sdk-for-android-navigate-tollpoint" title="class in com.here.sdk.mapdata"><code>TollPoint</code></a> of the given segment.
     Returns an empty list if no data is found.
     Returns <code>null</code> if <a href="sdk-for-android-navigate-segmentdataloaderoptions#loadTollPoints"><code>SegmentDataLoaderOptions.loadTollPoints</code></a> is set to <code>false</code>
     or the <a href="sdk-for-android-navigate-segmentdata" title="class in com.here.sdk.mapdata"><code>SegmentData</code></a> is not initialized using <a href="sdk-for-android-navigate-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)"><code>SegmentDataLoader.loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId, com.here.sdk.mapdata.SegmentDataLoaderOptions)</code></a>.</p></dd>
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
