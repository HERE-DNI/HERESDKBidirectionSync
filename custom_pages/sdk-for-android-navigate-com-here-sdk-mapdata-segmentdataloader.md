---
title: "SegmentDataLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SegmentDataLoader.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapdata.SegmentDataLoader</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">SegmentDataLoader</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Provides the interface for the access to the
 segments data available in the local OCM map. Please be aware that the methods within this class
 load map data synchronously. In the event of absent data in the disk cache, the data will be
 retrieved from the remote server. To mitigate the potential freezing of the calling thread,
 it is advisable to proactively prefetch map data around the working area.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#%3Cinit%3E()">SegmentDataLoader</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">SegmentDataLoader</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;byte[]&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#downloadFile(java.util.List,com.here.sdk.mapdata.DownloadingFileOptions)">downloadFile</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-filereference" title="class in com.here.sdk.mapdata">FileReference</a>&gt; fileReferences,
 <a href="sdk-for-android-navigate-downloadingfileoptions" title="class in com.here.sdk.mapdata">DownloadingFileOptions</a> downloadingOptions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Synchronously load the optional image providing guidance of a directed or non directed segment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#getSegmentsAroundCoordinates(com.here.sdk.core.GeoCoordinates,double)">getSegmentsAroundCoordinates</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 double radiusInMeters)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Loads the segments around a certain coordinates.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)">loadData</a><wbr/>(<a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a> segment,
 <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Synchronously load the data for the given map segment.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)">loadDirectedSegmentData</a><wbr/>(<a href="sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segment,
 <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Synchronously load the data for the given map directed segment.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>SegmentDataLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentDataLoader</span>()
                  throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>SegmentDataLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">SegmentDataLoader</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                  throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p>Indicates what went wrong when the instantiation was attempted.</p></dd>
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
<section class="detail" id="getSegmentsAroundCoordinates(com.here.sdk.core.GeoCoordinates,double)">
<h3>getSegmentsAroundCoordinates</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a>&gt;</span> <span class="element-name">getSegmentsAroundCoordinates</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 double radiusInMeters)</span>
                                                throws <span class="exceptions"><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div class="block"><p>Loads the segments around a certain coordinates.
 Returns an empty list in case no segments could be found around the coordinates.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The location to explore</p></dd>
<dd><code>radiusInMeters</code> - <p>The radius of the search. Only values between 1m and 5000m are accepted.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of segments around the given position. The segments are sorted by distance
     from the point.
     Throws if it's not possible to return list of a list of segments.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of a list of segments is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)">
<h3>loadData</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></span> <span class="element-name">loadData</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a> segment,
 @NonNull
 <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</span>
                     throws <span class="exceptions"><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div class="block"><p>Synchronously load the data for the given map segment.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segment</code> - <p>The segment to load.</p></dd>
<dd><code>options</code> - <p>Request options</p></dd>
<dt>Returns:</dt>
<dd><p>Requested data of a segment.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of data of a segment is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)">
<h3>loadDirectedSegmentData</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></span> <span class="element-name">loadDirectedSegmentData</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segment,
 @NonNull
 <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</span>
                                    throws <span class="exceptions"><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div class="block"><p>Synchronously load the data for the given map directed segment.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segment</code> - <p>The directed segment to load.</p></dd>
<dd><code>options</code> - <p>Request options</p></dd>
<dt>Returns:</dt>
<dd><p>Requested data of a segment.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of data of a segment is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="downloadFile(java.util.List,com.here.sdk.mapdata.DownloadingFileOptions)">
<h3>downloadFile</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;byte[]&gt;</span> <span class="element-name">downloadFile</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-filereference" title="class in com.here.sdk.mapdata">FileReference</a>&gt; fileReferences,
 @NonNull
 <a href="sdk-for-android-navigate-downloadingfileoptions" title="class in com.here.sdk.mapdata">DownloadingFileOptions</a> downloadingOptions)</span>
                          throws <span class="exceptions"><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div class="block"><p>Synchronously load the optional image providing guidance of a directed or non directed segment.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fileReferences</code> - <p>Provides information for a file reference.</p></dd>
<dd><code>downloadingOptions</code> - <p>Provides information regarding downloading configuration.</p></dd>
<dt>Returns:</dt>
<dd><p>Requested data of a segment.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of data of a segment is not returned.</p></dd>
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
