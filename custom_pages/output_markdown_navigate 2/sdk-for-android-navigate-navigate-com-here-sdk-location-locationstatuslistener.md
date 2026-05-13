---
title: "LocationStatusListener (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-location-locationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationStatusListener.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">LocationStatusListener</span></div>
<div class="block"><p>Interface for listening the
 LocationEngine status updates.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onFeaturesNotAvailable(java.util.List)">onFeaturesNotAvailable</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-locationfeature" title="enum class in com.here.sdk.location">LocationFeature</a>&gt; features)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called after start() if any requested location feature is not available
 for the application.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onStatusChanged(com.here.sdk.location.LocationEngineStatus)">onStatusChanged</a><wbr/>(<a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a> locationEngineStatus)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called each time the status of the LocationEngine has changed.</div>
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
<section class="detail" id="onStatusChanged(com.here.sdk.location.LocationEngineStatus)">
<h3>onStatusChanged</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onStatusChanged</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a> locationEngineStatus)</span></div>
<div class="block"><p>Called each time the status of the LocationEngine has changed.
 Invoked on the main thread.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>locationEngineStatus</code> - <p>The new status.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onFeaturesNotAvailable(java.util.List)">
<h3>onFeaturesNotAvailable</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onFeaturesNotAvailable</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-locationfeature" title="enum class in com.here.sdk.location">LocationFeature</a>&gt; features)</span></div>
<div class="block"><p>Called after start() if any requested location feature is not available
 for the application. Typically all features are enabled by default, but in
 certain variants some features may be disabled, e.g. to reduce binary size.
 If a feature that you need is not available, contact your HERE representative
 for more information.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>features</code> - <p>List of unavailable location features.</p></dd>
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
