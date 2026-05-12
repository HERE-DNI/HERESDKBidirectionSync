---
title: "VenueLevelSelectionListener (API Reference)"
slug: "sdk-for-android-navigate-venuelevelselectionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- VenueLevelSelectionListener.html -->
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
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">VenueLevelSelectionListener</span></div>
<div class="block"><p>The interface for listeners for
 the <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> selection event. Use the <a href="sdk-for-android-navigate-venuemap" title="class in com.here.sdk.venue.control"><code>VenueMap</code></a>
 to add and remove the <a href="sdk-for-android-navigate-venuelevelselectionlistener" title="interface in com.here.sdk.venue.control"><code>VenueLevelSelectionListener</code></a>.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onLevelSelected(com.here.sdk.venue.control.Venue,com.here.sdk.venue.data.VenueDrawing,com.here.sdk.venue.data.VenueLevel,com.here.sdk.venue.data.VenueLevel)">onLevelSelected</a><wbr/>(<a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue,
 <a href="sdk-for-android-navigate-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> drawing,
 <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> deselectedLevel,
 <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> selectedLevel)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Indicates that the selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> of a venue changed.</div>
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
<section class="detail" id="onLevelSelected(com.here.sdk.venue.control.Venue,com.here.sdk.venue.data.VenueDrawing,com.here.sdk.venue.data.VenueLevel,com.here.sdk.venue.data.VenueLevel)">
<h3>onLevelSelected</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onLevelSelected</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control">Venue</a> venue,
 @NonNull
 <a href="sdk-for-android-navigate-data-venuedrawing" title="class in com.here.sdk.venue.data">VenueDrawing</a> drawing,
 @Nullable
 <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> deselectedLevel,
 @NonNull
 <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data">VenueLevel</a> selectedLevel)</span></div>
<div class="block"><p>Indicates that the selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> of a venue changed.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venue</code> - <p>The <a href="sdk-for-android-navigate-venue" title="class in com.here.sdk.venue.control"><code>Venue</code></a> where the selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> changed.</p></dd>
<dd><code>drawing</code> - <p>The <a href="sdk-for-android-navigate-data-venuedrawing" title="class in com.here.sdk.venue.data"><code>VenueDrawing</code></a> where the selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> changed.</p></dd>
<dd><code>deselectedLevel</code> - <p>The previously selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a> or <code>null</code>
     if there was no selected level before.</p></dd>
<dd><code>selectedLevel</code> - <p>The new selected <a href="sdk-for-android-navigate-data-venuelevel" title="class in com.here.sdk.venue.data"><code>VenueLevel</code></a>.</p></dd>
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
