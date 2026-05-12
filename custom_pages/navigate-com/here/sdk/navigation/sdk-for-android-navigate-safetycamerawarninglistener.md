---
title: "SafetyCameraWarningListener (API Reference)"
slug: "sdk-for-android-navigate-safetycamerawarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SafetyCameraWarningListener.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">SafetyCameraWarningListener</span></div>
<div class="block"><p>This interface
 should be implemented in order to receive notifications on safety cameras.
 A <code>SafetyCameraWarning</code> will not be given until the previous warning of that type has been passed.
 For example, a route with <code>SafetyCameraWarning</code> 120 meters and <code>SafetyCameraWarning</code> 160 meters ahead,
 the first <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is 120 meters
 and the next <code>SafetyCameraWarning.distance_to_camera_in_meters</code> is then 40 meters,
 since that is the distance between the first and second warnings.
 </p><p>When <code>SafetyCameraWarningListener</code> is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled.
 The updates for the same safety camera appear in order of the initial <code>DistanceType.AHEAD</code> event.
 That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onSafetyCameraWarningUpdated(com.here.sdk.navigation.SafetyCameraWarning)">onSafetyCameraWarningUpdated</a><wbr/>(<a href="sdk-for-android-navigate-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a> safetyCameraWarning)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called whenever a new <code>SafetyCameraWarning</code> is available.</div>
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
<section class="detail" id="onSafetyCameraWarningUpdated(com.here.sdk.navigation.SafetyCameraWarning)">
<h3>onSafetyCameraWarningUpdated</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onSafetyCameraWarningUpdated</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a> safetyCameraWarning)</span></div>
<div class="block"><p>Called whenever a new <code>SafetyCameraWarning</code> is available.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>safetyCameraWarning</code> - <p>The object that contains details on the safety camera warning.</p></dd>
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
