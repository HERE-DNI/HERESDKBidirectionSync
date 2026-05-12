---
title: "PolygonDataAccessor (API Reference)"
slug: "sdk-for-android-explore-polygondataaccessor"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- PolygonDataAccessor.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview.datasource</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.datasource.PolygonDataAccessor</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">PolygonDataAccessor</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.
 <p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-dataattributesaccessor" title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getAttributes()">getAttributes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets polygon attributes accessor.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometry()">getGeometry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets polygon geometry.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setAttributes(com.here.sdk.mapview.datasource.DataAttributes)">setAttributes</a><wbr/>(<a href="sdk-for-android-explore-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replaces polygon attributes.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setGeometry(com.here.sdk.core.GeoPolygon)">setGeometry</a><wbr/>(<a href="sdk-for-android-explore-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Replaces polygon geometry.</div>
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

<ul class="member-list">
<li>
<section class="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a></span> <span class="element-name">getGeometry</span>()</div>
<div class="block"><p>Gets polygon geometry.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The polygon geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getAttributes()">
<h3>getAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-dataattributesaccessor" title="class in com.here.sdk.mapview.datasource">DataAttributesAccessor</a></span> <span class="element-name">getAttributes</span>()</div>
<div class="block"><p>Gets polygon attributes accessor.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The polygon attributes accessor.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setGeometry(com.here.sdk.core.GeoPolygon)">
<h3>setGeometry</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeometry</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry)</span></div>
<div class="block"><p>Replaces polygon geometry.
 The outer boundary has to be ordered clockwise and closed.
 <p>Altitude of the vertices is ignored.
 <p>The visual behaviour for self-intersecting outer boundary is undefined.</p></p></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>geometry</code> - <p>Geometry of the polygon. The outer boundary has to be ordered clockwise and closed.
     Altitude of the vertices is ignored.
     The visual behaviour for self-intersecting outer boundary is undefined.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setAttributes(com.here.sdk.mapview.datasource.DataAttributes)">
<h3>setAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setAttributes</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-dataattributes" title="class in com.here.sdk.mapview.datasource">DataAttributes</a> attributes)</span></div>
<div class="block"><p>Replaces polygon attributes.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>attributes</code> - <p>The attributes.</p></dd>
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
