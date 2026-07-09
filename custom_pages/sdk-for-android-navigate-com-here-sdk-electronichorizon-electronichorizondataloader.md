---
title: "ElectronicHorizonDataLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- ElectronicHorizonDataLoader.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.electronichorizon</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonDataLoader</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">ElectronicHorizonDataLoader</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Loads map data for segments that belong to the <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a> paths.
 <strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.
 Offline availability: This property is available online and offline.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapdata.SegmentDataLoaderOptions,int)">ElectronicHorizonDataLoader</a><wbr/>(<a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options,
 int segmentDataCacheSize)</code></div>
<div className="col-last even-row-color">
<div className="block">Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</div>
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
<section className="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapdata.SegmentDataLoaderOptions,int)">
<h3>ElectronicHorizonDataLoader</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">ElectronicHorizonDataLoader</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options,
 int segmentDataCacheSize)</span>
                            throws <span className="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div className="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.
 The constructor accepts options to configure the data loader. For more information, see <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata"><code>SegmentDataLoaderOptions</code></a>.
 The cache size limits the number of segments that the loader can keep in memory at the same time.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> instance that provides shared services, such as networking and map data.</p></dd>
<dd><code>options</code> - <p>The <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdataloaderoptions" title="class in com.here.sdk.mapdata"><code>SegmentDataLoaderOptions</code></a> instance that configures how segment data is requested.</p></dd>
<dd><code>segmentDataCacheSize</code> - <p>The maximum number of segments that the loader can cache.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> If the data loader cannot be created.</p></dd>
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
<section className="detail" id="loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">
<h3>loadData</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">loadData</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> electronicHorizonUpdate)</span></div>
<div className="block"><p>Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonUpdate</code> - <p>The update that contains the segments to add to the cache and the segments to remove from the cache.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getSegment(com.here.sdk.mapdata.DirectedOCMSegmentId)">
<h3>getSegment</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderResult</a></span> <span className="element-name">getSegment</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapdata-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segmentId)</span></div>
<div className="block"><p>Returns loaded data for the given segment identifier.
 The result contains either the loaded data or an error code.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>The segment identifier for which to return the loaded data from the cache.</p></dd>
<dt>Returns:</dt>
<dd><p>The result object that contains either the loaded segment data or an error code.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addElectronicHorizonDataLoaderStatusListener(com.here.sdk.electronichorizon.ElectronicHorizonDataLoaderStatusListener)">
<h3>addElectronicHorizonDataLoaderStatusListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">addElectronicHorizonDataLoaderStatusListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</span></div>
<div className="block"><p>Adds an <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoaderStatusListener</code></a> to the subscription list.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that receives data loader status updates.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeElectronicHorizonDataLoaderStatusListener(com.here.sdk.electronichorizon.ElectronicHorizonDataLoaderStatusListener)">
<h3>removeElectronicHorizonDataLoaderStatusListener</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">removeElectronicHorizonDataLoaderStatusListener</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</span></div>
<div className="block"><p>Removes an <a href="sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoaderStatusListener</code></a> from the subscription list.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that should no longer receive data loader status updates.</p></dd>
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
