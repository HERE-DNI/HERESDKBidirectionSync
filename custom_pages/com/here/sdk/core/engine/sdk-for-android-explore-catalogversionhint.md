---
title: "Untitled"
slug: "sdk-for-android-explore-catalogversionhint"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CatalogVersionHint.html -->
<!DOCTYPE HTML>

<html lang="en">

<body class="class-declaration-page">


<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-explore-index">Overview</a></li>
<li><a href="sdk-for-android-explore-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-explore-package-tree">Tree</a></li>
<li><a href="sdk-for-android-explore-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-explore-index-all">Index</a></li>
<li><a href="sdk-for-android-explore-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.core.engine</a></div>
<h1 class="title" title="Class CatalogVersionHint">Class CatalogVersionHint</h1>
</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.core.engine.CatalogVersionHint</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">CatalogVersionHint</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>This is a class for capturing user's intent for the
 desired catalog version to use in <a href="sdk-for-android-explore-desiredcatalog" title="class in com.here.sdk.core.engine"><code>DesiredCatalog</code></a> class.
 <p>You can request a specific or latest version of a catalog by calling the
 static functions <a href="#specific(long)"><code>specific(long)</code></a> and
 <a href="#latest(boolean)"><code>latest(boolean)</code></a> respectively. The HERE platform will make the
 best effort to provide an appropriate version for the catalog based on this
 version hint.
 Please take note that for the API <a href="#specific(long)"><code>specific(long)</code></a> to function properly,
 it is essential that the mutable and persistent storage should be cleaned.</p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">
<h2>Method Summary</h2>
<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#latest(boolean)">latest</a><wbr/>(boolean ignoreCachedData)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">This static method can be called when you are interested in getting the most latest version of
 a catalog when initializing the HERE SDK with <code>SDKOptions</code> where you can specify the
 catalog(s) you want to use.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-explore-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#specific(long)">specific</a><wbr/>(long version)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">This static method is used when you are interested in a
 specific version of a catalog, that you want to specify manually.</div>
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
<h2>Method Details</h2>
<ul class="member-list">
<li>
<section class="detail" id="specific(long)">
<h3>specific</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></span> <span class="element-name">specific</span><wbr/><span class="parameters">(long version)</span></div>
<div class="block"><p>This static method is used when you are interested in a
 specific version of a catalog, that you want to specify manually.
 To ensure proper functioning of this API, it is essential to clean the mutable and persistent storage.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>version</code> - <p>An integer value indicating the version of catalog desired.
     If the desired version does not exist, the HERE platform will make the
     best effort to provide an appropriate version or result in error logs
     about invalid version.</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-explore-catalogversionhint" title="class in com.here.sdk.core.engine"><code>CatalogVersionHint</code></a> with specified version.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="latest(boolean)">
<h3>latest</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-explore-catalogversionhint" title="class in com.here.sdk.core.engine">CatalogVersionHint</a></span> <span class="element-name">latest</span><wbr/><span class="parameters">(boolean ignoreCachedData)</span></div>
<div class="block"><p>This static method can be called when you are interested in getting the most latest version of
 a catalog when initializing the HERE SDK with <code>SDKOptions</code> where you can specify the
 catalog(s) you want to use. In effect, this will auto-update the cached map data on each
 start, if possible. Use this only when you have no installed <code>Regions</code>. Since this affects
 only the map data cache, calling this at initialization time has no or only a very limited
 effect on the start-up time.
 <p>In order to auto-update cached OCM-based map data, such as for the HERE SDK (Navigate), use the
 default HRN value: "hrn:here:data::olp-here:ocm" in your <code>DesiredCatalog</code>. Note that the
 HERE SDK (Explore) cannot be used with such settings and the
 initialization of the HERE SDK may fail - since it is based on a different map
 format.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>ignoreCachedData</code> - <p>A flag to specify handling of any cached data present on a device when
     trying to update the map version.
     If set to true, the HERE SDK will auto-update to the latest catalog version when no installed
     <code>Regions</code> are present. If present, this call will have no effect - use <code>updateCatalog()</code>
     via <code>MapUpdater</code> instead to update all map data to the latest version.
     Note that cached data present on a device - for example, data in the map cache or data cached
     by <code>PrefetchAroundLocationWithRadius</code> or <code>PrefetchAroundRouteOnIntervals</code> - will be become obsolete if
     a newer map version is available. Such data will be evicted using a LRU strategy over time.
     If set to false, the HERE SDK will auto-update to use the latest version, only
     when there is no cached map data at all (for example, at first install or after
     clearing the cache) <em>and</em> no installed map data. Otherwise, this call will have no effect.</p></dd>
<dt>Returns:</dt>
<dd><p>Instance of <a href="sdk-for-android-explore-catalogversionhint" title="class in com.here.sdk.core.engine"><code>CatalogVersionHint</code></a>.</p></dd>
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
</body>
</html>

</div>
`
}</HTMLBlock>
