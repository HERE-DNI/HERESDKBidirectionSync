---
title: "Span (API Reference)"
slug: "sdk-for-android-explore-span"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Span.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.routing.Span</div>
</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Span</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>A span is a part of the <a href="sdk-for-android-explore-section" title="class in com.here.sdk.routing"><code>Section</code></a> which is traversable or navigable. Each span
 usually has some geometry associated with it.</p></div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getBaseDuration()">getBaseDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the time duration necessary to traverse the span, using the speed provided
 in <a href="#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a> without taking into consideration
 the delays caused by the traffic.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCarAttributes()">getCarAttributes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of car access attributes on the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getConsumptionInKilowattHours()">getConsumptionInKilowattHours</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the power consumption in kilowatt per hour necessary to traverse the span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getCountryCode()">getCountryCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the country code of the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDuration()">getDuration</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the time duration necessary to traverse the span, using the speed provided
 in <a href="#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-dynamicspeedinfo" title="class in com.here.sdk.routing">DynamicSpeedInfo</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getDynamicSpeedInfo()">getDynamicSpeedInfo</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The dynamic speed information on the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getFunctionalRoadClass()">getFunctionalRoadClass</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the functional road class of the span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getGeometry()">getGeometry</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the <a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLengthInMeters()">getLengthInMeters</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the length of this span in meters.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoThroughRestrictionsIndexes()">getNoThroughRestrictionsIndexes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Get the list of indexes to <a href="sdk-for-android-explore-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a> the parent section owns.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getNoticeIndexes()">getNoticeIndexes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the list of indexes to <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> the parent section owns.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getRoadNumbers()">getRoadNumbers</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
 of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getScooterAttributes()">getScooterAttributes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of scooter access attributes on the span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSectionPolylineOffset()">getSectionPolylineOffset</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the position of the span inside the section's geometry, given as an offset.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSegmentReference()">getSegmentReference</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the segment reference of this span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getShieldText(com.here.sdk.routing.LocalizedRoadNumber)">getShieldText</a><wbr/>(<a href="sdk-for-android-explore-localizedroadnumber" title="class in com.here.sdk.routing">LocalizedRoadNumber</a> roadNumber)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Converts full route number to the value to be displayed on the road shield.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getSpeedLimitInMetersPerSecond()">getSpeedLimitInMetersPerSecond</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the speed limit in meters per second on the span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStateCode()">getStateCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the state code of the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-streetattributes" title="enum class in com.here.sdk.routing">StreetAttributes</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStreetAttributes()">getStreetAttributes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of street attributes on the span.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getStreetNames()">getStreetNames</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The street names on the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTrafficIncidentIndexes()">getTrafficIncidentIndexes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The indexes of traffic incidents from the field <a href="sdk-for-android-explore-section#getTrafficIncidents()"><code>Section.getTrafficIncidents()</code></a> of the parent <a href="sdk-for-android-explore-section" title="class in com.here.sdk.routing"><code>Section</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getTruckAttributes()">getTruckAttributes</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of truck access attributes on the span.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-walkattributes" title="enum class in com.here.sdk.routing">WalkAttributes</a>&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getWalkAttributes()">getWalkAttributes</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The list of walk attributes on the span.</div>
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
<section class="detail" id="getShieldText(com.here.sdk.routing.LocalizedRoadNumber)">
<h3>getShieldText</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getShieldText</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-localizedroadnumber" title="class in com.here.sdk.routing">LocalizedRoadNumber</a> roadNumber)</span></div>
<div class="block"><p>Converts full route number to the value to be displayed on the road shield.
 The results are based on country code and state code of <code>Span</code> object and route type of passed <code>road_number</code> argument.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>roadNumber</code> - <p>Route number to convert to shield text.</p></dd>
<dt>Returns:</dt>
<dd><p>Text on the road shield to display.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getGeometry()">
<h3>getGeometry</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core">GeoPolyline</a></span> <span class="element-name">getGeometry</span>()</div>
<div class="block"><p>Gets the <a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The <a href="sdk-for-android-explore-geopolyline" title="class in com.here.sdk.core"><code>GeoPolyline</code></a> object representing the polyline of this span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLengthInMeters()">
<h3>getLengthInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getLengthInMeters</span>()</div>
<div class="block"><p>Gets the length of this span in meters.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The length of this span in meters.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNoticeIndexes()">
<h3>getNoticeIndexes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">getNoticeIndexes</span>()</div>
<div class="block"><p>Gets the list of indexes to <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> the parent section owns.
 In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-explore-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a>'s
 carefully before proceeding.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of indexes to <a href="sdk-for-android-explore-section#getSectionNotices()"><code>Section.getSectionNotices()</code></a> the parent section owns.
     In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-explore-sectionnotice" title="class in com.here.sdk.routing"><code>SectionNotice</code></a>s
     carefully before proceeding.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSegmentReference()">
<h3>getSegmentReference</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-segmentreference" title="class in com.here.sdk.routing">SegmentReference</a></span> <span class="element-name">getSegmentReference</span>()</div>
<div class="block"><p>Gets the segment reference of this span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The segment reference of this span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTrafficIncidentIndexes()">
<h3>getTrafficIncidentIndexes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">getTrafficIncidentIndexes</span>()</div>
<div class="block"><p>The indexes of traffic incidents from the field <a href="sdk-for-android-explore-section#getTrafficIncidents()"><code>Section.getTrafficIncidents()</code></a> of the parent <a href="sdk-for-android-explore-section" title="class in com.here.sdk.routing"><code>Section</code></a>.
 Each matching incident takes at least a whole <a href="#getGeometry()"><code>getGeometry()</code></a>.
 The same incident can take other spans and an area out of the built route as well.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The indexes of traffic incidents from the field <a href="sdk-for-android-explore-section#getTrafficIncidents()"><code>Section.getTrafficIncidents()</code></a> of the parent <a href="sdk-for-android-explore-section" title="class in com.here.sdk.routing"><code>Section</code></a>.
     Each matching incident takes at least a whole <a href="#getGeometry()"><code>getGeometry()</code></a>.
     The same incident can take other spans and an area out of the built route as well.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSectionPolylineOffset()">
<h3>getSectionPolylineOffset</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getSectionPolylineOffset</span>()</div>
<div class="block"><p>Gets the position of the span inside the section's geometry, given as an offset. The span geometry starts from
 this offset and ends on the offset of the next span, both start offset point and end offset point being
 included in the span, because the spans' geometry share a point in the section's geometry.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The position of the span inside the section's geometry, given as an offset. The span geometry starts from
     this offset and ends on the offset of the next span, both start offset point and end offset point being
     included in the span, because the spans' geometry share a point in the section's geometry.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDynamicSpeedInfo()">
<h3>getDynamicSpeedInfo</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-dynamicspeedinfo" title="class in com.here.sdk.routing">DynamicSpeedInfo</a></span> <span class="element-name">getDynamicSpeedInfo</span>()</div>
<div class="block"><p>The dynamic speed information on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The dynamic speed information on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStreetAttributes()">
<h3>getStreetAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-streetattributes" title="enum class in com.here.sdk.routing">StreetAttributes</a>&gt;</span> <span class="element-name">getStreetAttributes</span>()</div>
<div class="block"><p>The list of street attributes on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of street attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCarAttributes()">
<h3>getCarAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</span> <span class="element-name">getCarAttributes</span>()</div>
<div class="block"><p>The list of car access attributes on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of car access attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTruckAttributes()">
<h3>getTruckAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</span> <span class="element-name">getTruckAttributes</span>()</div>
<div class="block"><p>The list of truck access attributes on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of truck access attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getScooterAttributes()">
<h3>getScooterAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-accessattributes" title="enum class in com.here.sdk.routing">AccessAttributes</a>&gt;</span> <span class="element-name">getScooterAttributes</span>()</div>
<div class="block"><p>The list of scooter access attributes on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of scooter access attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getWalkAttributes()">
<h3>getWalkAttributes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-walkattributes" title="enum class in com.here.sdk.routing">WalkAttributes</a>&gt;</span> <span class="element-name">getWalkAttributes</span>()</div>
<div class="block"><p>The list of walk attributes on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of walk attributes on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStreetNames()">
<h3>getStreetNames</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-localizedtexts" title="class in com.here.sdk.core">LocalizedTexts</a></span> <span class="element-name">getStreetNames</span>()</div>
<div class="block"><p>The street names on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The street names on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getRoadNumbers()">
<h3>getRoadNumbers</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-localizedroadnumbers" title="class in com.here.sdk.routing">LocalizedRoadNumbers</a></span> <span class="element-name">getRoadNumbers</span>()</div>
<div class="block"><p>Gets the road numbers on the span enriched with information specific to <em>route numbers</em>
 of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The road numbers on the span enriched with information specific to <em>route numbers</em>
     of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (<code>RouteType</code>).</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getSpeedLimitInMetersPerSecond()">
<h3>getSpeedLimitInMetersPerSecond</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getSpeedLimitInMetersPerSecond</span>()</div>
<div class="block"><p>Gets the speed limit in meters per second on the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The speed limit in meters per second on the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getConsumptionInKilowattHours()">
<h3>getConsumptionInKilowattHours</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">getConsumptionInKilowattHours</span>()</div>
<div class="block"><p>Gets the power consumption in kilowatt per hour necessary to traverse the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The power consumption in kilowatt per hour necessary to traverse the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getFunctionalRoadClass()">
<h3>getFunctionalRoadClass</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-functionalroadclass" title="enum class in com.here.sdk.routing">FunctionalRoadClass</a></span> <span class="element-name">getFunctionalRoadClass</span>()</div>
<div class="block"><p>Gets the functional road class of the span.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The functional road class of the span.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getDuration()">
<h3>getDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getDuration</span>()</div>
<div class="block"><p>Gets the time duration necessary to traverse the span, using the speed provided
 in <a href="#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a>. This duration takes also into
 consideration the delays caused by the traffic.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The time duration necessary to traverse the span, using the speed provided
     in <a href="#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a>. This duration takes also into
     consideration the delays caused by the traffic.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getBaseDuration()">
<h3>getBaseDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">getBaseDuration</span>()</div>
<div class="block"><p>Gets the time duration necessary to traverse the span, using the speed provided
 in <a href="#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a> without taking into consideration
 the delays caused by the traffic.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The time duration necessary to traverse the span, using the speed provided
     in <a href="#getDynamicSpeedInfo()"><code>getDynamicSpeedInfo()</code></a> without taking into consideration
     the delays caused by the traffic.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getCountryCode()">
<h3>getCountryCode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getCountryCode</span>()</div>
<div class="block"><p>Gets the country code of the span. The value is <code>null</code> when no data is available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The country code of the span. The value is <code>null</code> when no data is available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getStateCode()">
<h3>getStateCode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getStateCode</span>()</div>
<div class="block"><p>Gets the state code of the span. State code is available in some countries to denote principal
 subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
 The format of state code can vary for different countries, take the United States as example,
 it consists of two alphabet letters. The value is <code>null</code> when no data is available.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The state code of the span. State code is available in some countries to denote principal
     subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio.
     The format of state code can vary for different countries, take the United States as example,
     it consists of two alphabet letters.
     The value is <code>null</code> when no data is available.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getNoThroughRestrictionsIndexes()">
<h3>getNoThroughRestrictionsIndexes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html" title="class or interface in java.lang">Integer</a>&gt;</span> <span class="element-name">getNoThroughRestrictionsIndexes</span>()</div>
<div class="block"><p>Get the list of indexes to <a href="sdk-for-android-explore-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a> the parent section owns.
 In case the list is not empty, the user must judge all the indexed <a href="sdk-for-android-explore-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a>'s
 carefully before proceeding.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The list of indexes to <a href="sdk-for-android-explore-section#getNoThroughRestrictions()"><code>Section.getNoThroughRestrictions()</code></a> the parent section owns.
     In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's
     carefully before proceeding.</p></dd>
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
