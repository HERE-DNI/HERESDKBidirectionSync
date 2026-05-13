---
title: "CategoryQuery.Area (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-search-categoryquery-area"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- CategoryQuery.Area.html -->
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
<li><a href="#field-summary">Field</a> | </li>
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#field-detail">Field</a> | </li>
<li><a href="#constructor-detail">Constr</a> | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.search.CategoryQuery.Area</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-categoryquery" title="class in com.here.sdk.search">CategoryQuery</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">CategoryQuery.Area</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Area to perform search on.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#areaCenter">areaCenter</a></code></div>
<div class="col-last even-row-color">
<div class="block">Geographic coordinates of the center around which to provide the most relevant places.</div>
</div>
<div class="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-..-core-geobox" title="class in com.here.sdk.core">GeoBox</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#boxArea">boxArea</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Geographic rectangle area in which to provide the most relevant places.</div>
</div>
<div class="col-first even-row-color"><code>final <a href="sdk-for-android-navigate-..-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#circleArea">circleArea</a></code></div>
<div class="col-last even-row-color">
<div class="block">Geographic circle area in which to provide the most relevant places.</div>
</div>
<div class="col-first odd-row-color"><code>final <a href="sdk-for-android-navigate-..-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#corridorArea">corridorArea</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Geographic corridor area in which to provide the most relevant places.</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCoordinates)">Area</a><wbr/>(<a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoBox)">Area</a><wbr/>(<a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter,
 <a href="sdk-for-android-navigate-..-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCircle)">Area</a><wbr/>(<a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter,
 <a href="sdk-for-android-navigate-..-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates)">Area</a><wbr/>(<a href="sdk-for-android-navigate-..-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea,
 <a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a new instance of this class from provided parameters.</div>
</div>
</div>
</section>
</li>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="areaCenter">
<h3>areaCenter</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">areaCenter</span></div>
<div class="block"><p>Geographic coordinates of the center around which to provide the most relevant places.</p></div>
</section>
</li>
<li>
<section class="detail" id="boxArea">
<h3>boxArea</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-geobox" title="class in com.here.sdk.core">GeoBox</a></span> <span class="element-name">boxArea</span></div>
<div class="block"><p>Geographic rectangle area in which to provide the most relevant places.</p></div>
</section>
</li>
<li>
<section class="detail" id="circleArea">
<h3>circleArea</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a></span> <span class="element-name">circleArea</span></div>
<div class="block"><p>Geographic circle area in which to provide the most relevant places.</p></div>
</section>
</li>
<li>
<section class="detail" id="corridorArea">
<h3>corridorArea</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public final</span> <span class="return-type"><a href="sdk-for-android-navigate-..-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a></span> <span class="element-name">corridorArea</span></div>
<div class="block"><p>Geographic corridor area in which to provide the most relevant places.
 The contained polyline and half-width define the area that will be used in a search query.
 </p><p>When used with <code>SearchEngine</code>, the polyline is compressed and sent.
 More complex polylines with large amounts of coordinates and with smaller
 half-width may have the less relevant part removed, such as the one far away from the
 search center. This usually makes no difference, because there will be enough POIs near
 the search center. For use cases where it is important to search the entire polyline,
 half-width can be increased or not set.
 For example: Route between New York and Chicago with half-width 800 will be added to request
 without removing the far away part, but route of the same length (around 360km) between
 Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.
 </p><p>When <a href="#corridorArea"><code>corridorArea</code></a> is provided,
 <a href="#areaCenter"><code>areaCenter</code></a> has to be within it, otherwise
 <a href="#areaCenter"><code>areaCenter</code></a> is ignored when searching.</p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates)">
<h3>Area</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Area</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the center around which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoBox)">
<h3>Area</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Area</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-geobox" title="class in com.here.sdk.core">GeoBox</a> boxArea)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the center around which to provide the most relevant places.</p></dd>
<dd><code>boxArea</code> - <p>Geographic rectangle area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCircle)">
<h3>Area</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Area</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-geocircle" title="class in com.here.sdk.core">GeoCircle</a> circleArea)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the center around which to provide the most relevant places.</p></dd>
<dd><code>circleArea</code> - <p>Geographic circle area in which to provide the most relevant places.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates)">
<h3>Area</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">Area</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-core-geocorridor" title="class in com.here.sdk.core">GeoCorridor</a> corridorArea,
 @NonNull
 <a href="sdk-for-android-navigate-..-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> areaCenter)</span></div>
<div class="block"><p>Constructs a new instance of this class from provided parameters.
 The given corridor and center define the area that will be used in the search query.
 </p><p>When used with <code>SearchEngine</code>, the polyline is compressed and sent.
 More complex polylines with large amounts of coordinates and with smaller
 half-width may have the less relevant part removed, such as the one far away from the
 search center. This usually makes no difference, because there will be enough POIs near
 the search center. For use cases where it is important to search the entire polyline,
 half-width can be increased or not set.
 For example: Route between New York and Chicago with half-width 800 will be added to request
 without removing the far away part, but route of the same length (around 360km) between
 Milan (Italy) and Konstanz (Germany) will have the far away part removed due to its complexity.
 </p><p>The area center has to be within the corridor, otherwise it is ignored.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>corridorArea</code> - <p>Geographic corridor area in which to provide the most relevant places.</p></dd>
<dd><code>areaCenter</code> - <p>Geographic coordinates of the prioritized area center.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
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
