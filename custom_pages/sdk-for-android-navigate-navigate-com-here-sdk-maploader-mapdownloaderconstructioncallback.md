---
title: "MapDownloaderConstructionCallback (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-maploader-mapdownloaderconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapDownloaderConstructionCallback.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-help-doc#class">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Summary: </li>
<li>Nested | </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
<li>Constr | </li>
<li><a href="#method-detail">Method</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.maploader</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">MapDownloaderConstructionCallback</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a> has been completed.
 The <code>MapDownloader</code> instance is created on a background thread to not block the calling
 thread.
 </p><p>During construction an online connection is established to fetch configuration data for
 internal use. If no online connection is available, cached or default values will be used.
 This is only for internal reasons and has no effect on the operability of the resulting
 instance. When configuration data is available from the cache, construction can still take
 a reasonable amount of time. Applications should consider to show a loading indicator.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onMapDownloaderConstructedCompleted(com.here.sdk.maploader.MapDownloader)">onMapDownloaderConstructedCompleted</a><wbr/>(<a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader">MapDownloader</a> mapDownloader)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a> has been completed.</div>
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
<section class="detail" id="onMapDownloaderConstructedCompleted(com.here.sdk.maploader.MapDownloader)">
<h3>onMapDownloaderConstructedCompleted</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onMapDownloaderConstructedCompleted</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader">MapDownloader</a> mapDownloader)</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a> has been completed.
 The <code>MapDownloader</code> instance is created on a background thread to not block the calling
 thread.
 </p><p>During construction an online connection is established to fetch configuration data for
 internal use. If no online connection is available, cached or default values will be used.
 This is only for internal reasons and has no effect on the operability of the resulting
 instance. When configuration data is available from the cache, construction can still take
 a reasonable amount of time. Applications should consider to show a loading indicator.</p></div>
<dl class="notes">
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
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
