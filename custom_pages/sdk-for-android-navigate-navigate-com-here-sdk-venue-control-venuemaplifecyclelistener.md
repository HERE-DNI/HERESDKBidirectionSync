---
title: "VenueMapLifecycleListener (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-venue-control-venuemaplifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueMapLifecycleListener.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-..-..-..-..-..-index">Overview</a></li>
<li><a href="sdk-for-android-navigate-package-summary">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-..-..-..-..-..-help-doc#class">Help</a></li>
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
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueMapLifecycleListener</span></div>
<div class="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> lifecycle events. Use the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-venuemaplifecyclelistener" title="interface in com.here.sdk.venue.control"><code>VenueMapLifecycleListener</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onVenueAdded(com.here.sdk.venue.control.Venue)">onVenueAdded</a><wbr/>(<a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was added to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onVenueRemoved(java.lang.String)">onVenueRemoved</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was removed from the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</div>
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
<section class="detail" id="onVenueAdded(com.here.sdk.venue.control.Venue)">
<h3>onVenueAdded</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onVenueAdded</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue)</span></div>
<div class="block"><p>Indicates that a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was added to the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The created <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="onVenueRemoved(java.lang.String)">
<h3>onVenueRemoved</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onVenueRemoved</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> venueIdentifier)</span></div>
<div class="block"><p>Indicates that a <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> was removed from the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueIdentifier</code> - <p>The destroyed venue id, that can be obtained from the <a href="sdk-for-android-navigate-..-data-venuemodel#getId()"><code>VenueModel.getId()</code></a>.</p></dd>
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
