---
title: "SpeedBasedCameraBehavior.ProfileValue (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-navigation-speedbasedcamerabehavior-profilevalue"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SpeedBasedCameraBehavior.ProfileValue.html -->
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
<li>Method</li>
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
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.SpeedBasedCameraBehavior.ProfileValue</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>Enclosing class:</dt>
<dd><a href="sdk-for-android-navigate-speedbasedcamerabehavior" title="class in com.here.sdk.navigation">SpeedBasedCameraBehavior</a></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public static final class </span><span class="element-name type-name-label">SpeedBasedCameraBehavior.ProfileValue</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A single profile value which indicates the speed range in which it applies to its zoom and
 tilt configuration.</p></div>
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
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#fromMetersPerSecond">fromMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">Start speed of the range.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#tiltInDegrees">tiltInDegrees</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Tilt configuration.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#toMetersPerSecond">toMetersPerSecond</a></code></div>
<div class="col-last even-row-color">
<div class="block">End speed of the range.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-..-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#zoom">zoom</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Zoom configuration.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(double,double,com.here.sdk.mapview.MapMeasure,double)">ProfileValue</a><wbr/>(double fromMetersPerSecond,
 double toMetersPerSecond,
 <a href="sdk-for-android-navigate-..-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double tiltInDegrees)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
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
<section class="detail" id="fromMetersPerSecond">
<h3>fromMetersPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">fromMetersPerSecond</span></div>
<div class="block"><p>Start speed of the range.</p></div>
</section>
</li>
<li>
<section class="detail" id="toMetersPerSecond">
<h3>toMetersPerSecond</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">toMetersPerSecond</span></div>
<div class="block"><p>End speed of the range.</p></div>
</section>
</li>
<li>
<section class="detail" id="zoom">
<h3>zoom</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-..-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a></span> <span class="element-name">zoom</span></div>
<div class="block"><p>Zoom configuration.
 Note: <a href="sdk-for-android-navigate-..-mapview-mapmeasure.kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></div>
</section>
</li>
<li>
<section class="detail" id="tiltInDegrees">
<h3>tiltInDegrees</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">tiltInDegrees</span></div>
<div class="block"><p>Tilt configuration.</p></div>
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
<section class="detail" id="&lt;init&gt;(double,double,com.here.sdk.mapview.MapMeasure,double)">
<h3>ProfileValue</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">ProfileValue</span><wbr/><span class="parameters">(double fromMetersPerSecond,
 double toMetersPerSecond,
 @NonNull
 <a href="sdk-for-android-navigate-..-mapview-mapmeasure" title="class in com.here.sdk.mapview">MapMeasure</a> zoom,
 double tiltInDegrees)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>fromMetersPerSecond</code> - <p>Start speed of the range.</p></dd>
<dd><code>toMetersPerSecond</code> - <p>End speed of the range.</p></dd>
<dd><code>zoom</code> - <p>Zoom configuration.
 Note: <a href="sdk-for-android-navigate-..-mapview-mapmeasure.kind#SCALE"><code>MapMeasure.Kind.SCALE</code></a> is not supported.</p></dd>
<dd><code>tiltInDegrees</code> - <p>Tilt configuration.</p></dd>
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
