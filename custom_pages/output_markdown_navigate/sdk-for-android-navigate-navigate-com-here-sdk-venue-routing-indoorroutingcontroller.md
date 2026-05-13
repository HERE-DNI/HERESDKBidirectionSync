---
title: "IndoorRoutingController (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-venue-routing-indoorroutingcontroller"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- IndoorRoutingController.html -->
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
<li><a href="#constructor-summary">Constr</a> | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li>Field | </li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.venue.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-navigate-..-..-..-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.venue.routing.IndoorRoutingController</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">IndoorRoutingController</span>
<span class="extends-implements">extends <a href="sdk-for-android-navigate-..-..-..-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>This class controls the rendering of indoor routes on the map.
 <br/>
 Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
 Related APIs may change for new releases without a deprecation process.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.venue.control.VenueMap,com.here.sdk.mapview.MapViewBase)">IndoorRoutingController</a><wbr/>(<a href="sdk-for-android-navigate-..-control-venuemap" title="class in com.here.sdk.venue.control">VenueMap</a> venueMap,
 <a href="sdk-for-android-navigate-..-..-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance of this class.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#hideRoute()">hideRoute</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Hides an indoor route, visible on the map.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#showRoute(com.here.sdk.routing.Route,com.here.sdk.venue.routing.IndoorRouteStyle)">showRoute</a><wbr/>(<a href="sdk-for-android-navigate-..-..-routing-route" title="class in com.here.sdk.routing">Route</a> route,
 <a href="sdk-for-android-navigate-indoorroutestyle" title="class in com.here.sdk.venue.routing">IndoorRouteStyle</a> style)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Shows an indoor route on the map.</div>
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
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.venue.control.VenueMap,com.here.sdk.mapview.MapViewBase)">
<h3>IndoorRoutingController</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">IndoorRoutingController</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-control-venuemap" title="class in com.here.sdk.venue.control">VenueMap</a> venueMap,
 @NonNull
 <a href="sdk-for-android-navigate-..-..-mapview-mapviewbase" title="interface in com.here.sdk.mapview">MapViewBase</a> mapView)</span></div>
<div class="block"><p>Creates a new instance of this class.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>venueMap</code> - <p>A venue map instance.</p></dd>
<dd><code>mapView</code> - <p>A map scene where routes should be shown.</p></dd>
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
<section class="detail" id="showRoute(com.here.sdk.routing.Route,com.here.sdk.venue.routing.IndoorRouteStyle)">
<h3>showRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">showRoute</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-..-..-routing-route" title="class in com.here.sdk.routing">Route</a> route,
 @NonNull
 <a href="sdk-for-android-navigate-indoorroutestyle" title="class in com.here.sdk.venue.routing">IndoorRouteStyle</a> style)</span></div>
<div class="block"><p>Shows an indoor route on the map. The previously visible indoor route will be hidden.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>route</code> - <p>A route to show</p></dd>
<dd><code>style</code> - <p>A route style for the given route.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hideRoute()">
<h3>hideRoute</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">hideRoute</span>()</div>
<div class="block"><p>Hides an indoor route, visible on the map.</p></div>
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
