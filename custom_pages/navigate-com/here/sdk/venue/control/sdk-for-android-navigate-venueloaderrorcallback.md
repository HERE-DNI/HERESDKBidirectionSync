---
title: "VenueLoadErrorCallback (API Reference)"
slug: "sdk-for-android-navigate-venueloaderrorcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueLoadErrorCallback.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.control</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Functional Interface:</dt>
<dd>This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.</dd>
</dl>
<hr/>
<div class="type-signature"><span class="annotations"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html" title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueLoadErrorCallback</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onVenueLoadError(com.here.sdk.venue.control.VenueErrorCode)">onVenueLoadError</a><wbr/>(<a href="sdk-for-android-navigate-venueerrorcode" title="enum class in com.here.sdk.venue.control">VenueErrorCode</a> error)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</div>
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
<section class="detail" id="onVenueLoadError(com.here.sdk.venue.control.VenueErrorCode)">
<h3>onVenueLoadError</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onVenueLoadError</span><wbr/><span class="parameters">(@Nullable
 <a href="sdk-for-android-navigate-venueerrorcode" title="enum class in com.here.sdk.venue.control">VenueErrorCode</a> error)</span></div>
<div class="block"><p>A method which is called on the main thread when <a href="sdk-for-android-navigate-venuemap#selectVenueAsync(java.lang.String,com.here.sdk.venue.control.VenueLoadErrorCallback)"><code>VenueMap.selectVenueAsync(String, VenueLoadErrorCallback)</code></a> has been completed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>error</code> - <p>Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p></dd>
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
