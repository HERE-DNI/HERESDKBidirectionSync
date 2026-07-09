---
title: "MapDownloaderConstructionCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapdownloaderconstructioncallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapDownloaderConstructionCallback.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section className="class-description" id="class-description">
<dl className="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>

<div className="type-signature"><span className="annotations"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">MapDownloaderConstructionCallback</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a> has been completed.
 The <code>MapDownloader</code> instance is created on a background thread to not block the calling
 thread.
 During construction an online connection is established to fetch configuration data for
 internal use. If no online connection is available, cached or default values will be used.
 This is only for internal reasons and has no effect on the operability of the resulting
 instance. When configuration data is available from the cache, construction can still take
 a reasonable amount of time. Applications should consider to show a loading indicator.</p></div>
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
<section className="detail" id="onMapDownloaderConstructedCompleted(com.here.sdk.maploader.MapDownloader)">
<h3>onMapDownloaderConstructedCompleted</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onMapDownloaderConstructedCompleted</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader" title="class in com.here.sdk.maploader">MapDownloader</a> mapDownloader)</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a> has been completed.
 The <code>MapDownloader</code> instance is created on a background thread to not block the calling
 thread.
 During construction an online connection is established to fetch configuration data for
 internal use. If no online connection is available, cached or default values will be used.
 This is only for internal reasons and has no effect on the operability of the resulting
 instance. When configuration data is available from the cache, construction can still take
 a reasonable amount of time. Applications should consider to show a loading indicator.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapDownloader</code> - <p>Represents a constructed MapDownloader object.</p></dd>
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
