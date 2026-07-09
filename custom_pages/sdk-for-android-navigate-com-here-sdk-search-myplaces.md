---
title: "MyPlaces (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-myplaces"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MyPlaces.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.search.MyPlaces</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MyPlaces</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Provides means to populate personal places data source. Also acts as a
 owner of the collection of personal places. MyPlaces is
 memory-only object: nothing is persisted and/or sent over the network.
 Client has full control on how to store personal places.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section className="constructor-summary" id="constructor-summary">

<div className="caption"><span>Constructors</span></div>
<div className="summary-table two-column-summary">


<div className="col-constructor-name even-row-color"><code><a className="member-name-link" href="sdk-for-android-navigate-com-here-sdk-search-myplaces#%3Cinit%3E()">MyPlaces</a>()</code></div>
<div className="col-last even-row-color">
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
<h3>MyPlaces</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="element-name">MyPlaces</span>()</div>
<div className="block"><p>Creates a new instance of this class.</p></div>
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
<section className="detail" id="addPlace(com.here.sdk.search.GeoPlace,com.here.sdk.core.threading.OnTaskCompleted)">
<h3>addPlace</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">addPlace</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-search-geoplace" title="class in com.here.sdk.search">GeoPlace</a> place,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span></div>
<div className="block"><p>Adds a place to this data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>place</code> - <p>The place.</p></dd>
<dd><code>callback</code> - <p>The callback to be called when task is completed.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="addPlaces(java.util.List,com.here.sdk.core.threading.OnTaskCompleted)">
<h3>addPlaces</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">addPlaces</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-geoplace" title="class in com.here.sdk.search">GeoPlace</a>&gt; places,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span></div>
<div className="block"><p>Adds a list of places to this data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>places</code> - <p>Places</p></dd>
<dd><code>callback</code> - <p>The callback to be called when task is completed.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removePlace(java.lang.String,com.here.sdk.core.threading.OnTaskCompleted)">
<h3>removePlace</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">removePlace</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> placeId,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span></div>
<div className="block"><p>Removes a place from this data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>placeId</code> - <p>The place id</p></dd>
<dd><code>callback</code> - <p>The callback to be called when task is completed.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removePlaces(java.util.List,com.here.sdk.core.threading.OnTaskCompleted)">
<h3>removePlaces</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">removePlaces</span><wbr/><span className="parameters">(@NonNull
 <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a>&gt; placeIds,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span></div>
<div className="block"><p>Removes a list of places from this data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>placeIds</code> - <p>Place ids</p></dd>
<dd><code>callback</code> - <p>The callback to be called when task is completed.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="removeAll(com.here.sdk.core.threading.OnTaskCompleted)">
<h3>removeAll</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span className="element-name">removeAll</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-core-threading-ontaskcompleted" title="interface in com.here.sdk.core.threading">OnTaskCompleted</a> callback)</span></div>
<div className="block"><p>Removes all places from this data source.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>callback</code> - <p>The callback to be called when task is completed.</p></dd>
<dt>Returns:</dt>
<dd><p>Handle that will be used to manipulate the execution of the task.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPlaces()">
<h3>getPlaces</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-geoplace" title="class in com.here.sdk.search">GeoPlace</a>&gt;</span> <span className="element-name">getPlaces</span>()</div>
<div className="block"><p>Gets the list of places which currently belongs to this data source. The returned list is
 a clone of the internal list and thus changing it has no effect on the data source.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The list of places which currently belong to this data source. This list is
     a clone of the internal list and thus changing it has no effect on the data source.</p></dd>
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
