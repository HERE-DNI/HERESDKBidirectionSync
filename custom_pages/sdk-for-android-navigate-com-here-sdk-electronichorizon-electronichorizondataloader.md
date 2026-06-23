---
title: "ElectronicHorizonDataLoader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-electronichorizon-electronichorizondataloader"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- ElectronicHorizonDataLoader.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.electronichorizon.ElectronicHorizonDataLoader</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">ElectronicHorizonDataLoader</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Loads map data for segments that belong to the <a href="sdk-for-android-navigate-electronichorizonengine" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonEngine</code></a> paths.
 </p><p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.
 </p><p>Offline availability: This property is available online and offline.</p></div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-index#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapdata.SegmentDataLoaderOptions,int)">ElectronicHorizonDataLoader</a><wbr/>(<a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options,
 int segmentDataCacheSize)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#addElectronicHorizonDataLoaderStatusListener(com.here.sdk.electronichorizon.ElectronicHorizonDataLoaderStatusListener)">addElectronicHorizonDataLoaderStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds an <a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoaderStatusListener</code></a> to the subscription list.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderResult</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#getSegment(com.here.sdk.mapdata.DirectedOCMSegmentId)">getSegment</a><wbr/>(<a href="sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segmentId)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Returns loaded data for the given segment identifier.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">loadData</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> electronicHorizonUpdate)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-index#removeElectronicHorizonDataLoaderStatusListener(com.here.sdk.electronichorizon.ElectronicHorizonDataLoaderStatusListener)">removeElectronicHorizonDataLoaderStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes an <a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoaderStatusListener</code></a> from the subscription list.</div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.mapdata.SegmentDataLoaderOptions,int)">
<h3>ElectronicHorizonDataLoader</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ElectronicHorizonDataLoader</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine,
 @NonNull
 <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata">SegmentDataLoaderOptions</a> options,
 int segmentDataCacheSize)</span>
                            throws <span class="exceptions"><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block"><p>Creates a new instance of <a href="sdk-for-android-navigate-electronichorizondataloader" title="class in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoader</code></a>.
 The constructor accepts options to configure the data loader. For more information, see <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata"><code>SegmentDataLoaderOptions</code></a>.
 The cache size limits the number of segments that the loader can keep in memory at the same time.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>sdkEngine</code> - <p>The <a href="sdk-for-android-navigate-sdknativeengine" title="class in com.here.sdk.core.engine"><code>SDKNativeEngine</code></a> instance that provides shared services, such as networking and map data.</p></dd>
<dd><code>options</code> - <p>The <a href="sdk-for-android-navigate-segmentdataloaderoptions" title="class in com.here.sdk.mapdata"><code>SegmentDataLoaderOptions</code></a> instance that configures how segment data is requested.</p></dd>
<dd><code>segmentDataCacheSize</code> - <p>The maximum number of segments that the loader can cache.</p></dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - <p><a href="sdk-for-android-navigate-instantiationerrorexception" title="class in com.here.sdk.core.errors"><code>InstantiationErrorException</code></a> If the data loader cannot be created.</p></dd>
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
<section class="detail" id="loadData(com.here.sdk.electronichorizon.ElectronicHorizonUpdate)">
<h3>loadData</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">loadData</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-electronichorizonupdate" title="class in com.here.sdk.electronichorizon">ElectronicHorizonUpdate</a> electronicHorizonUpdate)</span></div>
<div class="block"><p>Requests data for all added segments and removes cached data for segments that are not part of the horizon anymore.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonUpdate</code> - <p>The update that contains the segments to add to the cache and the segments to remove from the cache.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSegment(com.here.sdk.mapdata.DirectedOCMSegmentId)">
<h3>getSegment</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-electronichorizondataloaderresult" title="class in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderResult</a></span> <span class="element-name">getSegment</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-directedocmsegmentid" title="class in com.here.sdk.mapdata">DirectedOCMSegmentId</a> segmentId)</span></div>
<div class="block"><p>Returns loaded data for the given segment identifier.
 The result contains either the loaded data or an error code.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>segmentId</code> - <p>The segment identifier for which to return the loaded data from the cache.</p></dd>
<dt>Returns:</dt>
<dd><p>The result object that contains either the loaded segment data or an error code.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addElectronicHorizonDataLoaderStatusListener(com.here.sdk.electronichorizon.ElectronicHorizonDataLoaderStatusListener)">
<h3>addElectronicHorizonDataLoaderStatusListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addElectronicHorizonDataLoaderStatusListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</span></div>
<div class="block"><p>Adds an <a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoaderStatusListener</code></a> to the subscription list.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>electronicHorizonListener</code> - <p>The listener that receives data loader status updates.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeElectronicHorizonDataLoaderStatusListener(com.here.sdk.electronichorizon.ElectronicHorizonDataLoaderStatusListener)">
<h3>removeElectronicHorizonDataLoaderStatusListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeElectronicHorizonDataLoaderStatusListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon">ElectronicHorizonDataLoaderStatusListener</a> electronicHorizonListener)</span></div>
<div class="block"><p>Removes an <a href="sdk-for-android-navigate-electronichorizondataloaderstatuslistener" title="interface in com.here.sdk.electronichorizon"><code>ElectronicHorizonDataLoaderStatusListener</code></a> from the subscription list.</p></div>
<dl class="notes">
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
`
}</HTMLBlock>
