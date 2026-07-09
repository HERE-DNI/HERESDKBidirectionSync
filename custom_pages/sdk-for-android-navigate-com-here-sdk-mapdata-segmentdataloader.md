---
title: "SegmentDataLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- SegmentDataLoader.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapdata.SegmentDataLoader</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">SegmentDataLoader</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Provides the interface for the access to the
 segments data available in the local OCM map. Please be aware that the methods within this class
 load map data synchronously. In the event of absent data in the disk cache, the data will be
 retrieved from the remote server. To mitigate the potential freezing of the calling thread,
 it is advisable to proactively prefetch map data around the working area.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#%3Cinit%3E()">SegmentDataLoader</a>()</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of this class.</div>
</div>
<div className="col-constructor-name odd-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloader#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">SegmentDataLoader</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</code></div>
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
<h3>SegmentDataLoader</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentDataLoader</span>()
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
<h3>SegmentDataLoader</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">SegmentDataLoader</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine)</span>
                  throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of this class.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>A SDKEngine instance.</p></dd>
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
<section className="detail" id="getSegmentsAroundCoordinates(com.here.sdk.core.GeoCoordinates,double)">
<h3>getSegmentsAroundCoordinates</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a>&gt;</span> <span className="element-name">getSegmentsAroundCoordinates</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> coordinates,
 double radiusInMeters)</span>
                                                throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div className="block"><p>Loads the segments around a certain coordinates.
 Returns an empty list in case no segments could be found around the coordinates.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>coordinates</code> - <p>The location to explore</p></dd>
<dd><code>radiusInMeters</code> - <p>The radius of the search. Only values between 1m and 5000m are accepted.</p></dd>
<dt>Returns:</dt>
<dd><p>The list of segments around the given position. The segments are sorted by distance
     from the point.
     Throws if it's not possible to return list of a list of segments.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of a list of segments is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="loadData(com.here.sdk.mapdata.OCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)">
<h3>loadData</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></span> <span className="element-name">loadData</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-ocmsegmentid" title="class in com.here.sdk.mapdata">OCMSegmentId</a> segment,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</span>
                     throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div className="block"><p>Synchronously load the data for the given map segment.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segment</code> - <p>The segment to load.</p></dd>
<dd><code>options</code> - <p>Request options</p></dd>
<dt>Returns:</dt>
<dd><p>Requested data of a segment.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of data of a segment is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="loadDirectedSegmentData(com.here.sdk.mapdata.DirectedOCMSegmentId,com.here.sdk.mapdata.SegmentDataLoaderOptions)">
<h3>loadDirectedSegmentData</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a></span> <span className="element-name">loadDirectedSegmentData</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segment,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options)</span>
                                    throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div className="block"><p>Synchronously load the data for the given map directed segment.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segment</code> - <p>The directed segment to load.</p></dd>
<dd><code>options</code> - <p>Request options</p></dd>
<dt>Returns:</dt>
<dd><p>Requested data of a segment.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of data of a segment is not returned.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="downloadFile(java.util.List,com.here.sdk.mapdata.DownloadingFileOptions)">
<h3>downloadFile</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a><byte[]></byte[]></span> <span className="element-name">downloadFile</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-mapdata-filereference" title="class in com.here.sdk.mapdata">FileReference</a>&gt; fileReferences,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-downloadingfileoptions" title="class in com.here.sdk.mapdata">DownloadingFileOptions</a> downloadingOptions)</span>
                          throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></span></div>
<div className="block"><p>Synchronously load the optional image providing guidance of a directed or non directed segment.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>fileReferences</code> - <p>Provides information for a file reference.</p></dd>
<dd><code>downloadingOptions</code> - <p>Provides information regarding downloading configuration.</p></dd>
<dt>Returns:</dt>
<dd><p>Requested data of a segment.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-mapdata-mapdataloaderexception" title="class in com.here.sdk.mapdata">MapDataLoaderException</a></code> - <p>Specifies reason, why list of data of a segment is not returned.</p></dd>
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
