---
title: "CameraBehavior (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-navigation-camerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CameraBehavior.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Known Implementing Classes:</dt>
<dd><code><a href="sdk-for-android-navigate-areacamerabehavior" title="class in com.here.sdk.navigation">AreaCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-automotivecamerabehavior" title="class in com.here.sdk.navigation">AutomotiveCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-dynamiccamerabehavior" title="class in com.here.sdk.navigation">DynamicCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-fixedcamerabehavior" title="class in com.here.sdk.navigation">FixedCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-speedbasedcamerabehavior" title="class in com.here.sdk.navigation">SpeedBasedCameraBehavior</a></code>, <code><a href="sdk-for-android-navigate-trackingcamerabehavior" title="class in com.here.sdk.navigation">TrackingCameraBehavior</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CameraBehavior</span></div>
<div class="block"><p>Interface used to change implement different
 camera behaviors.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getNormalizedPrincipalPoint()">getNormalizedPrincipalPoint</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Gets the currently set normalized principal point to be used during navigation.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">setNormalizedPrincipalPoint</a><wbr/>(<a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Sets a normalized principal point to be used during navigation.</div>
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
<section class="detail" id="getNormalizedPrincipalPoint()">
<h3>getNormalizedPrincipalPoint</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a></span> <span class="element-name">getNormalizedPrincipalPoint</span>()</div>
<div class="block"><p>Gets the currently set normalized principal point to be used during navigation.
 </p><p>Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The normalized principal point.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D)">
<h3>setNormalizedPrincipalPoint</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">setNormalizedPrincipalPoint</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> value)</span></div>
<div class="block"><p>Sets a normalized principal point to be used during navigation.
 </p><p>Normalized principal point to be used during navigation.
 Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
 of the mapview.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>value</code> - <p>The normalized principal point.</p></dd>
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
