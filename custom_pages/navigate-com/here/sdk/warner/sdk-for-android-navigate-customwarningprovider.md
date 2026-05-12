---
title: "CustomWarningProvider (API Reference)"
slug: "sdk-for-android-navigate-customwarningprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CustomWarningProvider.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.warner</a></div>

</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public interface </span><span class="element-name type-name-label">CustomWarningProvider</span></div>
<div class="block"><p>A interface representing a provider of custom warnings based on vehicle position.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
 behaviors. Related APIs may change for new releases without a deprecation process.</p></p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getCustomWarningType()">getCustomWarningType</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns the custom warning type identifier produced by this provider.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-customwarning" title="class in com.here.sdk.warner">CustomWarning</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3"><code><a class="member-name-link" href="#getWarnings(com.here.sdk.mapdata.SegmentData,com.here.sdk.mapdata.SegmentData)">getWarnings</a><wbr/>(<a href="sdk-for-android-navigate-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> currentSegment,
 <a href="sdk-for-android-navigate-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> previousSegment)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">
<div class="block">Returns a list of custom warnings for the given vehicle position.</div>
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
<section class="detail" id="getCustomWarningType()">
<h3>getCustomWarningType</h3>
<div class="member-signature"><span class="return-type">int</span> <span class="element-name">getCustomWarningType</span>()</div>
<div class="block"><p>Returns the custom warning type identifier produced by this provider.
 <p>The returned value corresponds to <a href="sdk-for-android-navigate-customwarning#customWarningType"><code>CustomWarning.customWarningType</code></a> and
 <a href="sdk-for-android-navigate-warning#customWarningType"><code>Warning.customWarningType</code></a> and is used to apply per-type configuration,
 such as notification distances.</p></p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The custom warning type identifier for this provider.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWarnings(com.here.sdk.mapdata.SegmentData,com.here.sdk.mapdata.SegmentData)">
<h3>getWarnings</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-customwarning" title="class in com.here.sdk.warner">CustomWarning</a>&gt;</span> <span class="element-name">getWarnings</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> currentSegment,
 @Nullable
 <a href="sdk-for-android-navigate-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> previousSegment)</span></div>
<div class="block"><p>Returns a list of custom warnings for the given vehicle position.
 <p>This method evaluates the custom warning provider using the current
 vehicle position on the electronic horizon and returns the resulting
 custom warnings along with corresponding payload.</p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>currentSegment</code> - <p>Segment data representing the vehicle’s current
     position on the electronic horizon.</p></dd>
<dd><code>previousSegment</code> - <p>Segment data representing the vehicle’s previous
     position on the electronic horizon. This parameter may be null if no
     previous position information is available.</p></dd>
<dt>Returns:</dt>
<dd><p>A list of <code>CustomWarning</code> instances representing all applicable
     custom warnings. The list may be empty if no warnings apply.</p></dd>
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
