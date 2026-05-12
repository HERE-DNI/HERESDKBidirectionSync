---
title: "TwoFingerPanListener (API Reference)"
slug: "sdk-for-android-explore-twofingerpanlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- TwoFingerPanListener.html -->
<!DOCTYPE HTML>






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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.gestures</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">TwoFingerPanListener</span></div>
<div class="block"><p>Interface for handling two finger pan gestures.
 Two finger pan gesture occurs when two fingers are on the screen
 and both of them are moving vertically.</p></div>
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
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#onTwoFingerPan(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double)">onTwoFingerPan</a><wbr/>(<a href="sdk-for-android-explore-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state,
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin,
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> translation,
 double velocity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Called when the two finger pan gesture occurs.</div>
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
<section class="detail" id="onTwoFingerPan(com.here.sdk.gestures.GestureState,com.here.sdk.core.Point2D,com.here.sdk.core.Point2D,double)">
<h3>onTwoFingerPan</h3>
<div class="member-signature"><span class="return-type">void</span> <span class="element-name">onTwoFingerPan</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-gesturestate" title="enum class in com.here.sdk.gestures">GestureState</a> state,
 @NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> origin,
 @NonNull
 <a href="sdk-for-android-explore-core-point2d" title="class in com.here.sdk.core">Point2D</a> translation,
 double velocity)</span></div>
<div class="block"><p>Called when the two finger pan gesture occurs.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>state</code> - <p>Determines in which state the gesture is.</p></dd>
<dd><code>origin</code> - <p>Position halfway between two touch points relative to the MapView in pixels.</p></dd>
<dd><code>translation</code> - <p>Translation offset since the last position in pixels.</p></dd>
<dd><code>velocity</code> - <p>Velocity of panning in pixels per millisecond.</p></dd>
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
