---
title: "MapUpdaterConstructionCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdaterconstructioncallback"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapUpdaterConstructionCallback.html -->






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
</span><span className="modifiers">public interface </span><span className="element-name type-name-label">MapUpdaterConstructionCallback</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapupdater#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)"><code>MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback)</code></a> has been completed.
 Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
 When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p></div>
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
<section className="detail" id="onMapUpdaterConstructe(com.here.sdk.maploader.MapUpdater)">
<h3>onMapUpdaterConstructe</h3>
<div className="member-signature"><span className="return-type">void</span> <span className="element-name">onMapUpdaterConstructe</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a> mapUpdater)</span></div>
<div className="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapupdater#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)"><code>MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback)</code></a> has been completed.
 Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
 When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>mapUpdater</code> - <p>Represents a constructed <code>MapUpdater</code> object.</p></dd>
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
