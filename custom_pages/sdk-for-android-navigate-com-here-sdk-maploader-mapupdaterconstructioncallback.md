---
title: "MapUpdaterConstructionCallback (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdaterconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapUpdaterConstructionCallback.html -->
<!DOCTYPE HTML>









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MapUpdaterConstructionCallback</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapupdater#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)"><code>MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback)</code></a> has been completed.
 Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
 When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab3" onclick="show('method-summary-table', 'method-summary-table-tab3', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Abstract Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-index#onMapUpdaterConstructe(com.here.sdk.maploader.MapUpdater)">onMapUpdaterConstructe</a><wbr/>(<a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a> mapUpdater)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A method which is called on the main thread when <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapupdater#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)"><code>MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback)</code></a> has been completed.</div>
</div>
</div>
</div>
</div>
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
<section class="detail" id="onMapUpdaterConstructe(com.here.sdk.maploader.MapUpdater)">
<h3>onMapUpdaterConstructe</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onMapUpdaterConstructe</span><wbr/><span class="parameters">(@NonNull
 <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a> mapUpdater)</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="https://docs.here.com/outing-api-test/page/sdk-for-android-navigate-mapupdater#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)"><code>MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback)</code></a> has been completed.
 Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
 When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p></div>
<dl class="notes">
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
</main>





</div>
`
}</HTMLBlock>
