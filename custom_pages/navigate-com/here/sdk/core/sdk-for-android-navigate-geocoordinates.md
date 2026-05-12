---
title: "GeoCoordinates (API Reference)"
slug: "sdk-for-android-navigate-geocoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- GeoCoordinates.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.core</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.core.GeoCoordinates</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">GeoCoordinates</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents geographical coordinates in 3D space.</p></div>
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
<div class="col-first even-row-color"><code>final <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#altitude">altitude</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional altitude in meters.</div>
</div>
<div class="col-first odd-row-color"><code>final double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#latitude">latitude</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Latitude in degrees.</div>
</div>
<div class="col-first even-row-color"><code>final double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#longitude">longitude</a></code></div>
<div class="col-last even-row-color">
<div class="block">Longitude in degrees.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(double,double)">GeoCoordinates</a><wbr/>(double latitude,
 double longitude)</code></div>
<div class="col-last even-row-color">
<div class="block">Constructs a GeoCoordinates from the provided latitude and longitude values.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(double,double,double)">GeoCoordinates</a><wbr/>(double latitude,
 double longitude,
 double altitude)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>double</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#distanceTo(com.here.sdk.core.GeoCoordinates)">distanceTo</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Computes distance (in meters) along the great circle between two coordinates.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#fromString(java.lang.String)">fromString</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Constructs GeoCoordinates from the provided string in specified format.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#interpolate(com.here.sdk.core.GeoCoordinates,double)">interpolate</a><wbr/>(<a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> towardCoords,
 double factor)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Computes the coordinates of the interpolated location along the great circle between
 the two coordinates.</div>
</div>
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
<section class="detail" id="latitude">
<h3>latitude</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">latitude</span></div>
<div class="block"><p>Latitude in degrees.</p></div>
</section>
</li>
<li>
<section class="detail" id="longitude">
<h3>longitude</h3>
<div class="member-signature"><span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">longitude</span></div>
<div class="block"><p>Longitude in degrees.</p></div>
</section>
</li>
<li>
<section class="detail" id="altitude">
<h3>altitude</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public final</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">altitude</span></div>
<div class="block"><p>Optional altitude in meters.
 By convention, on iOS devices, altitude is set as meters relative to the
 mean sea level.
 On Android devices, altitude is set as meters relative to the WGS 84
 reference ellipsoid.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,double,double)">
<h3>GeoCoordinates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoCoordinates</span><wbr/><span class="parameters">(double latitude,
 double longitude,
 double altitude)</span></div>
<div class="block"><p>Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.
 Corrects values of lat and long if they exceed the ranges.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>latitude</code> - <p>Latitude in degrees. Positive value means Northern hemisphere.
     If the value is out of range of [-90.0, 90.0] it's clamped to that range.
     NaN value is converted to 0.0.</p></dd>
<dd><code>longitude</code> - <p>Longitude in degrees. Positive value means Eastern hemisphere.
     If the value is out of range of [-180.0, 180.0] it's replaced with a value
     within the range, representing effectively the same meridian.
     NaN value is converted to 0.0.</p></dd>
<dd><code>altitude</code> - <p>Altitude in meters. NaN value is converted to <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double)">
<h3>GeoCoordinates</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">GeoCoordinates</span><wbr/><span class="parameters">(double latitude,
 double longitude)</span></div>
<div class="block"><p>Constructs a GeoCoordinates from the provided latitude and longitude values.
 Corrects values of latitude and longitude if they exceed the ranges.
 Altitude set to <code>null</code>.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>latitude</code> - <p>Latitude in degrees. Positive value means Northern hemisphere.
     If the value is out of range of [-90.0, 90.0] it's clamped to that range.
     NaN value is converted to 0.0.</p></dd>
<dd><code>longitude</code> - <p>Longitude in degrees. Positive value means Eastern hemisphere.
     If the value is out of range of [-180.0, 180.0] it's replaced with a value
     within the range, representing effectively the same meridian.
     NaN value is converted to 0.0.</p></dd>
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
<li>
<section class="detail" id="distanceTo(com.here.sdk.core.GeoCoordinates)">
<h3>distanceTo</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceTo</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</span></div>
<div class="block"><p>Computes distance (in meters) along the great circle between two coordinates.
 This method ignores altitude of both points.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>point</code> - <p>Coordinates of the point to which the distance is computed.</p></dd>
<dt>Returns:</dt>
<dd><p>distance in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="interpolate(com.here.sdk.core.GeoCoordinates,double)">
<h3>interpolate</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">interpolate</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> towardCoords,
 double factor)</span></div>
<div class="block"><p>Computes the coordinates of the interpolated location along the great circle between
 the two coordinates.
 </p><p>The interpolation factor is clamped to the range <code>[0.0, 1.0]</code> where <code>0.0</code> identifies this
 <code>GeoCoordinates</code> and <code>1.0</code> indicates the other coordinates.
 </p><p>The ratio between the distance to the interpolated coordinates and the distance to the other
 coordinates is approximately equal to the interpolation factor. When both coordinates have
 the altitude, then the altitude is interpolated as well; <code>null</code> otherwise.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>towardCoords</code> - <p>Coordinates of the point to which the interpolation is directed.</p></dd>
<dd><code>factor</code> - <p>The interpolation factor</p></dd>
<dt>Returns:</dt>
<dd><p>interpolated coordinates</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="fromString(java.lang.String)">
<h3>fromString</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">fromString</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> input)</span></div>
<div class="block"><p>Constructs GeoCoordinates from the provided string in specified format.
 Corrects values of lat and long if they exceed the ranges.
 If the latitude value is out of range of [-90.0, 90.0] it's clamped to that range.
 If the longitude value is out of range of [-180.0, 180.0] it's replaced with a value
 within the range, representing effectively the same meridian.
 Examples: <code>53.43762,-13.65468</code>.
 <code>49°59'56.948"N, 15°48'22.989"E</code>
<code>50d4m17.698N 14d24m2.826E</code>
<code>49.9991522N, 150.8063858E</code>
<code>40°26′47″N 79°58′36″W</code></p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>input</code> - <p>String representing GeoCoordinates in one of supported formats.</p></dd>
<dt>Returns:</dt>
<dd><p>Created GeoCoordinates, or 'null' if string was not in appropriate format.</p></dd>
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
