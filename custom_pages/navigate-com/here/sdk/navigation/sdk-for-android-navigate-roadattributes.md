---
title: "RoadAttributes (API Reference)"
slug: "sdk-for-android-navigate-roadattributes"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadAttributes.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.navigation</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.navigation.RoadAttributes</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoadAttributes</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Road attributes, including usage and physical characteristics.
 Note that a road can have more than one attribute at the same time.</p></div>
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
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isBridge">isBridge</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isBuiltUpArea">isBuiltUpArea</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates if the navigable segment is a built up area.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isControlledAccess">isControlledAccess</a></code></div>
<div class="col-last even-row-color">
<div class="block">Controlled access roads are roads with limited entrances and exits
 that allow uninterrupted high-speed traffic flow.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isDirtRoad">isDirtRoad</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates whether the navigable segment is paved.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isDividedRoad">isDividedRoad</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates if there is a physical structure or painted road marking intended to legally
 prohibit left turns in right-side driving countries, right turns in left-side driving
 countries, and U-turns at divided intersections or in the middle of divided segments.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isNoThrough">isNoThrough</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identifies a no through road.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isPrivate">isPrivate</a></code></div>
<div class="col-last even-row-color">
<div class="block">Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isRamp">isRamp</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Range is a ramp: connects roads that do not intersect at grade.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isRightDrivingSide">isRightDrivingSide</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isRoundabout">isRoundabout</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the presence of a roundabout.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isTollway">isTollway</a></code></div>
<div class="col-last even-row-color">
<div class="block">Identifies a road for which a fee must be paid to use the road.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isTunnel">isTunnel</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Identifies an enclosed (on all sides) passageway through or under an obstruction.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">RoadAttributes</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
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
<section class="detail" id="isDirtRoad">
<h3>isDirtRoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDirtRoad</span></div>
<div class="block"><p>Indicates whether the navigable segment is paved.
 Paved is primarily used for map display and routing by assigning
 higher penalties to unpaved roads.
 Paved roads are made of concrete, asphalt, cobblestone or brick.
 Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTunnel">
<h3>isTunnel</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTunnel</span></div>
<div class="block"><p>Identifies an enclosed (on all sides) passageway through or under an obstruction.
 This attribute can be used for display or route guidance.</p></div>
</section>
</li>
<li>
<section class="detail" id="isBridge">
<h3>isBridge</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBridge</span></div>
<div class="block"><p>Identifies a structure that allows a road, railway, or walkway
 to pass over another road, railway, waterway, or valley serving
 map display and route guidance functionalities.
 Bridge is published on segments that represent significant
 bridges and/or overpasses; elevated roads are not published as bridge.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRamp">
<h3>isRamp</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRamp</span></div>
<div class="block"><p>Range is a ramp: connects roads that do not intersect at grade.
 Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”)
 and for route guidance when determining if sign text should be used.</p></div>
</section>
</li>
<li>
<section class="detail" id="isControlledAccess">
<h3>isControlledAccess</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isControlledAccess</span></div>
<div class="block"><p>Controlled access roads are roads with limited entrances and exits
 that allow uninterrupted high-speed traffic flow.
 For example, the Interstate/Freeway network in the United States or
 the Motorway network in Europe.
 Controlled Access can be used for map display, avoidance of freeway/motorway,
 publishing speed limits, and route guidance timing.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPrivate">
<h3>isPrivate</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrivate</span></div>
<div class="block"><p>Private identifies roads that are not maintained by an organization
 responsible for maintenance of public roads.
 Allows for unique cartographic representation of roads that restrict public use.
 May be used to avoid routing through a private road.</p></div>
</section>
</li>
<li>
<section class="detail" id="isNoThrough">
<h3>isNoThrough</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isNoThrough</span></div>
<div class="block"><p>Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTollway">
<h3>isTollway</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTollway</span></div>
<div class="block"><p>Identifies a road for which a fee must be paid to use the road.
 Tollway may be used for map display (e.g., different rendering of toll roads) and routing.
 Tollway is flagged on roads that require a fee for traversal.</p></div>
</section>
</li>
<li>
<section class="detail" id="isDividedRoad">
<h3>isDividedRoad</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isDividedRoad</span></div>
<div class="block"><p>Indicates if there is a physical structure or painted road marking intended to legally
 prohibit left turns in right-side driving countries, right turns in left-side driving
 countries, and U-turns at divided intersections or in the middle of divided segments.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRightDrivingSide">
<h3>isRightDrivingSide</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRightDrivingSide</span></div>
<div class="block"><p>Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.
 For example, in New York it is always <code>true</code> and in London always <code>false</code> as the United Kingdom is
 a left-hand driving country.</p></div>
</section>
</li>
<li>
<section class="detail" id="isRoundabout">
<h3>isRoundabout</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isRoundabout</span></div>
<div class="block"><p>Indicates the presence of a roundabout.</p></div>
</section>
</li>
<li>
<section class="detail" id="isBuiltUpArea">
<h3>isBuiltUpArea</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isBuiltUpArea</span></div>
<div class="block"><p>Indicates if the navigable segment is a built up area.</p></div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>RoadAttributes</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoadAttributes</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
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
