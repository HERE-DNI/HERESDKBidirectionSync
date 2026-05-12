---
title: "EventText (API Reference)"
slug: "sdk-for-android-navigate-eventtext"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EventText.html -->
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
<div class="inheritance">com.here.sdk.navigation.EventText</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">EventText</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Contains all the information regarding the next text announcement.</p></div>
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
<div class="col-second even-row-color"><code><a class="member-name-link" href="#distanceInMeters">distanceInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">Distance in meters to the location of the event for which the text notification is given.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-maneuvernotificationdetails" title="class in com.here.sdk.navigation">ManeuverNotificationDetails</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#maneuverNotificationDetails">maneuverNotificationDetails</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Information about the next maneuver.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-spatialnotificationdetails" title="class in com.here.sdk.navigation">SpatialNotificationDetails</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#spatialNotificationDetails">spatialNotificationDetails</a></code></div>
<div class="col-last even-row-color">
<div class="block">Information for a spatial text notifications.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#text">text</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The text notification instruction.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#type">type</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the type of text announcement</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.navigation.TextNotificationType,double,java.lang.String)">EventText</a><wbr/>(<a href="sdk-for-android-navigate-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a> type,
 double distanceInMeters,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</code></div>
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
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
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
<section class="detail" id="type">
<h3>type</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a></span> <span class="element-name">type</span></div>
<div class="block"><p>Indicates the type of text announcement</p></div>
</section>
</li>
<li>
<section class="detail" id="distanceInMeters">
<h3>distanceInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceInMeters</span></div>
<div class="block"><p>Distance in meters to the location of the event for which the text notification is given.
 <p><strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
 greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
 during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
 are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
 3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
 Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
 are defined in the <code>UnitSystem</code> class.</p></p></div>
</section>
</li>
<li>
<section class="detail" id="text">
<h3>text</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">text</span></div>
<div class="block"><p>The text notification instruction. The text is formatted and localized as specified via
 <a href="sdk-for-android-navigate-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.
 <p><strong>Note:</strong> During navigation, the text will be always empty when the <a href="sdk-for-android-navigate-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> is
 taken from the <code>Navigator</code> or <code>VisualNavigator</code> instance via the provided index.
 The text instruction that can be accessed from the <a href="sdk-for-android-navigate-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> instance is meant
 as preview and it is not necessarily matching the more comprehensive maneuver information you
 can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
 texts that can be used for spoken text notifications during a trip.</p></p></div>
</section>
</li>
<li>
<section class="detail" id="maneuverNotificationDetails">
<h3>maneuverNotificationDetails</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-maneuvernotificationdetails" title="class in com.here.sdk.navigation">ManeuverNotificationDetails</a></span> <span class="element-name">maneuverNotificationDetails</span></div>
<div class="block"><p>Information about the next maneuver.
 Is non-<code>null</code> only for <a href="#type"><code>type</code></a> equals to <a href="sdk-for-android-navigate-textnotificationtype#MANEUVER"><code>TextNotificationType.MANEUVER</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="spatialNotificationDetails">
<h3>spatialNotificationDetails</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-spatialnotificationdetails" title="class in com.here.sdk.navigation">SpatialNotificationDetails</a></span> <span class="element-name">spatialNotificationDetails</span></div>
<div class="block"><p>Information for a spatial text notifications.
 When <a href="sdk-for-android-navigate-eventtextoptions#enableSpatialAudio"><code>EventTextOptions.enableSpatialAudio</code></a> is false,
 then this attribute will be <code>null</code>.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.navigation.TextNotificationType,double,java.lang.String)">
<h3>EventText</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EventText</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-textnotificationtype" title="enum class in com.here.sdk.navigation">TextNotificationType</a> type,
 double distanceInMeters,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> text)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>Indicates the type of text announcement</p></dd>
<dd><code>distanceInMeters</code> - <p>Distance in meters to the location of the event for which the text notification is given.
 <p><strong>Note:</strong> For greater distances, distance in kilometers is rounded to the nearest digit (0.5 or
 greater rounds up, else down) to simplify the distance phrase in <code>ManeuverNotifications</code> texts
 during navigation. Distance in miles is rounded to the nearest 0.5 step. For example, 3.5 kilometers
 are rounded to 4 kilometers and the notification will begin with <code>After 4 kilometers...</code>. However,
 3.5 miles are not rounded up and the notification will begin with <code>After three and a half miles...</code>.
 Same for 3.7 miles, whereas 3.8 miles are rounded to 4 miles. Note that the measurement units itself
 are defined in the <code>UnitSystem</code> class.</p></p></dd>
<dd><code>text</code> - <p>The text notification instruction. The text is formatted and localized as specified via
 <a href="sdk-for-android-navigate-routing-routetextoptions" title="class in com.here.sdk.routing"><code>RouteTextOptions</code></a>.
 <p><strong>Note:</strong> During navigation, the text will be always empty when the <a href="sdk-for-android-navigate-routing-maneuver" title="class in com.here.sdk.routing"><code>Maneuver</code></a> is
 taken from the <code>Navigator</code> or <code>VisualNavigator</code> instance via the provided index.
 The text instruction that can be accessed from the <a href="sdk-for-android-navigate-routing-route" title="class in com.here.sdk.routing"><code>Route</code></a> instance is meant
 as preview and it is not necessarily matching the more comprehensive maneuver information you
 can access during navigation. This information can be enhanced with real-time <code>ManeuverNotifications</code>
 texts that can be used for spoken text notifications during a trip.</p></p></dd>
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
</body>
</html>

</div>
`
}</HTMLBlock>
