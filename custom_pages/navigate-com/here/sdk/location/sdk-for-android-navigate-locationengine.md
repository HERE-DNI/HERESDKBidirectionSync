---
title: "LocationEngine (API Reference)"
slug: "sdk-for-android-navigate-locationengine"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- LocationEngine.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.location</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.location.LocationEngine</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code>com.here.sdk.location.AppConfigListener</code>, <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public class </span><span class="element-name type-name-label">LocationEngine</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a>
implements <a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a>, com.here.sdk.location.AppConfigListener</span></div>
<div class="block">This class handles location updates received according to the desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a> or <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.
 Each instance of this class will be using internally the same client providing the actual
 location updates. For that reason, only one <a href="sdk-for-android-navigate-locationengine" title="class in com.here.sdk.location"><code>LocationEngine</code></a>
 can be started at a time. Multiple listeners can be attached, either to receive
 location updates, see <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a>, status updates, see
 <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> or location issue has occurred, see
 <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a>. When a different <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a> or <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a> is
 desired, the LocationEngine needs to be stopped and started again.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E()">LocationEngine</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Constructor of the LocationEngine</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.core.engine.SDKNativeEngine)">LocationEngine</a><wbr/>(<a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine)</code></div>
<div class="col-last odd-row-color">
<div class="block">Constructor of the LocationEngine</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">addLocationIssueListener</a><wbr/>(<a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> to the engine to get notified when a location issue
 has occurred</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLocationListener(com.here.sdk.core.LocationListener)">addLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a> to the engine to get notified when there is a new
 <a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core"><code>Location</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">addLocationStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Adds a <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> to the engine to get notified when there is an
 important status change.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#confirmHEREPrivacyNoticeException()">confirmHEREPrivacyNoticeException</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">By calling this method, the application developer confirms that they have received an
 exceptional permission from HERE in written form to **not** include a reference to the HERE
 Privacy Notice.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#confirmHEREPrivacyNoticeInclusion()">confirmHEREPrivacyNoticeInclusion</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">It is the responsibility of the application developer to ensure that
 the application user is informed about the collection of characteristic information
 regarding nearby mobile and Wi-Fi network signals.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#disableVehicleSensors()">disableVehicleSensors</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Disables access to vehicle's sensor information.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">enableVehicleSensors</a><wbr/>(androidx.car.app.hardware.CarHardwareManager manager)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">This feature enables the utilization of the vehicle's GNSS and movement sensor information.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core">Location</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#getLastKnownLocation()">getLastKnownLocation</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the last known location obtained by the engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#isStarted()">isStarted</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Checks if the engine is in started state.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">removeLocationIssueListener</a><wbr/>(<a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> from the engine</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLocationListener(com.here.sdk.core.LocationListener)">removeLocationListener</a><wbr/>(<a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a> from the engine</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">removeLocationStatusListener</a><wbr/>(<a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Removes a <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> from the engine</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#setLastKnownLocationPersistent(boolean)">setLastKnownLocationPersistent</a><wbr/>(boolean persistent)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Enables or disables saving of last known location so it persists between application
 sessions.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(com.here.sdk.location.LocationAccuracy)">start</a><wbr/>(<a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the location engine with desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#start(com.here.sdk.location.LocationOptions)">start</a><wbr/>(<a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Starts the location engine with desired <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#stop()">stop</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Stops the location engine.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">updateLocationAccuracy</a><wbr/>(<a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reconfigures the location engine with desired LocationAccuracy.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="#updateLocationOptions(com.here.sdk.location.LocationOptions)">updateLocationOptions</a><wbr/>(<a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Reconfigures the location engine with desired LocationOptions.</div>
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
<section class="detail" id="&lt;init&gt;()">
<h3>LocationEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationEngine</span>()
               throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block">Constructor of the LocationEngine</div>
<dl class="notes">
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - if engine was not initialized properly</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(com.here.sdk.core.engine.SDKNativeEngine)">
<h3>LocationEngine</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">LocationEngine</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> engine)</span>
               throws <span class="exceptions"><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span></div>
<div class="block">Constructor of the LocationEngine</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>engine</code> - of the SDK holding internal services and SDK configuration</dd>
<dt>Throws:</dt>
<dd><code><a href="sdk-for-android-navigate-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></code> - if engine was not initialized properly</dd>
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
<section class="detail" id="start(com.here.sdk.location.LocationAccuracy)">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div class="block">Starts the location engine with desired <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location"><code>LocationAccuracy</code></a>.
 Make sure to call either confirmHEREPrivacyNoticeInclusion()
 or confirmHEREPrivacyNoticeException() beforehand.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationAccuracy)">start</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - Desired location accuracy</dd>
<dt>Returns:</dt>
<dd>the status of the LocationEngine</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="start(com.here.sdk.location.LocationOptions)">
<h3>start</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">start</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div class="block">Starts the location engine with desired <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location"><code>LocationOptions</code></a>.
 Make sure to call either confirmHEREPrivacyNoticeInclusion()
 or confirmHEREPrivacyNoticeException() beforehand.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationOptions)">start</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - Desired location options.</dd>
<dt>Returns:</dt>
<dd>the status of the LocationEngine</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">
<h3>updateLocationAccuracy</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationAccuracy</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span></div>
<div class="block"><p>Reconfigures the location engine with desired LocationAccuracy. This method is a faster
 way to change location accuracy for already started location engine, than calling <a href="sdk-for-android-navigate-locationenginebase#stop()"><code>LocationEngineBase.stop()</code></a> and <a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>LocationEngineBase.start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>, if called for unstarted location
 engine.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#updateLocationAccuracy(com.here.sdk.location.LocationAccuracy)">updateLocationAccuracy</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationAccuracy</code> - <p>Desired location accuracy. Requested accuracy is not
 guaranteed.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="updateLocationOptions(com.here.sdk.location.LocationOptions)">
<h3>updateLocationOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">updateLocationOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationoptions" title="class in com.here.sdk.location">LocationOptions</a> locationOptions)</span></div>
<div class="block"><p>Reconfigures the location engine with desired LocationOptions. This method is a faster way
 to change location options for already started location engine, than calling <a href="sdk-for-android-navigate-locationenginebase#stop()"><code>LocationEngineBase.stop()</code></a> and <a href="sdk-for-android-navigate-locationenginebase#start(com.here.sdk.location.LocationOptions)"><code>LocationEngineBase.start(LocationOptions)</code></a> in sequence. Returns <a href="sdk-for-android-navigate-locationenginestatus#NOT_READY"><code>LocationEngineStatus.NOT_READY</code></a>, if called for unstarted location
 engine.</p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#updateLocationOptions(com.here.sdk.location.LocationOptions)">updateLocationOptions</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>locationOptions</code> - <p>Desired location options.</p></dd>
<dt>Returns:</dt>
<dd><p>Engine status. Valid values are defined in <a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location"><code>LocationEngineStatus</code></a></p></dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the argument is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="stop()">
<h3>stop</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">stop</span>()</div>
<div class="block">Stops the location engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#stop()">stop</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="isStarted()">
<h3>isStarted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isStarted</span>()</div>
<div class="block">Checks if the engine is in started state.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#isStarted()">isStarted</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd>true if started, false otherwise</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="confirmHEREPrivacyNoticeInclusion()">
<h3>confirmHEREPrivacyNoticeInclusion</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeInclusion</span>()</div>
<div class="block"><p>It is the responsibility of the application developer to ensure that
 the application user is informed about the collection of characteristic information
 regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related
 <a href="https://legal.here.com/here-network-positioning-via-sdk">HERE Privacy Notice</a>
 must be made available to the user.
 <p>This information can be included in the application's Terms &amp; Conditions,
 Privacy Policy, or otherwise made accessible to the user.
 <p>An example text for informing users about the data collection:
 "This application uses location services provided by HERE Technologies.
 To maintain, improve, and provide these services, HERE Technologies occasionally collects
 characteristic information about nearby mobile and Wi-Fi network signals.
 For more information, please refer to the HERE Privacy Notice at:
 https://legal.here.com/here-network-positioning-via-sdk"

 <p>By calling this method, the application developer confirms that
 this information is made available to the end user.

 For example, it is sufficient to inform users once that using the app requires
 acceptance of its terms (if any). Then, in the terms include the
 above mentioned data collection information and a link to the related HERE Privacy Notice.
 The user is not required to open the terms to acknowledge the data collection details.
 The "Positioning" example app on
 <a href="https://github.com/heremaps/here-sdk-examples">GitHub</a>
 provides an example of this.

 When the above criteria are met, it is recommended to silently execute this
 method each time before starting the <code>LocationEngine</code>, as failure to do so
 will result in the engine being non-functional.</p></p></p></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#confirmHEREPrivacyNoticeInclusion()">confirmHEREPrivacyNoticeInclusion</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd><p>Immediately returns with <a href="sdk-for-android-navigate-confirmationstatus#OK"><code>ConfirmationStatus.OK</code></a>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="confirmHEREPrivacyNoticeException()">
<h3>confirmHEREPrivacyNoticeException</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location">ConfirmationStatus</a></span> <span class="element-name">confirmHEREPrivacyNoticeException</span>()</div>
<div class="block"><p>By calling this method, the application developer confirms that they have received an
 exceptional permission from HERE in written form to **not** include a reference to the HERE
 Privacy Notice. As a result, the <code>LocationEngine</code> will not collect characteristic
 information about the nearby mobile and Wi-Fi network signals. However, the engine will still
 be fully functional and it will deliver location updates when the exception can be confirmed.
 <p>Note that this call should not involve user interaction and it should be executed silently
 by the application before starting the <code>LocationEngine</code>.
 <p>The permission for exceptional use will be verified asynchronously using your HERE SDK
 credentials. A missing permission will lead to stopping of the <code>LocationEngine</code>
 and
 <a href="sdk-for-android-navigate-locationenginestatus#PRIVACY_NOTICE_UNCONFIRMED"><code>LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED</code></a> is delivered to
 <code>LocationStatusListener</code>.</p></p></p></div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#confirmHEREPrivacyNoticeException()">confirmHEREPrivacyNoticeException</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd>Confirmation action status. Valid values are defined in <a href="sdk-for-android-navigate-confirmationstatus" title="enum class in com.here.sdk.location"><code>ConfirmationStatus</code></a>.
         A first-time call may result in <a href="sdk-for-android-navigate-confirmationstatus#PENDING"><code>ConfirmationStatus.PENDING</code></a>, make sure to use the
         <code>LocationStatusListener</code> to get notified on an unconfirmed permission.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">
<h3>enableVehicleSensors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">enableVehicleSensors</span><wbr/><span class="parameters">(@NonNull
 androidx.car.app.hardware.CarHardwareManager manager)</span></div>
<div class="block">This feature enables the utilization of the vehicle's GNSS and movement sensor information.
 It is recommended to always enable this feature by default when the application supports
 Android Auto. This allows the phone's positioning sensor information to be augmented with the
 vehicle's sensor data, resulting in the best possible positioning estimates. However, given
 the varying quality of car sensor implementations, it is also advisable to provide
 application users with the option to disable the usage of vehicle sensor information - this
 would be helpful in case the vehicle reports information that is clearly misleading or
 contradictory. Furthermore, users should be able to re-enable this feature if the vehicle's
 capability improves.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#enableVehicleSensors(androidx.car.app.hardware.CarHardwareManager)">enableVehicleSensors</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>manager</code> - Android Auto car hardware manager.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="disableVehicleSensors()">
<h3>disableVehicleSensors</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">disableVehicleSensors</span>()</div>
<div class="block">Disables access to vehicle's sensor information.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#disableVehicleSensors()">disableVehicleSensors</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getLastKnownLocation()">
<h3>getLastKnownLocation</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core">Location</a></span> <span class="element-name">getLastKnownLocation</span>()</div>
<div class="block">Gets the last known location obtained by the engine.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#getLastKnownLocation()">getLastKnownLocation</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Returns:</dt>
<dd>last known <a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core"><code>Location</code></a> if available, null if never
         obtained.</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLocationListener(com.here.sdk.core.LocationListener)">
<h3>addLocationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLocationListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div class="block">Adds a <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a> to the engine to get notified when there is a new
 <a href="sdk-for-android-navigate-core-location" title="class in com.here.sdk.core"><code>Location</code></a>.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#addLocationListener(com.here.sdk.core.LocationListener)">addLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be added</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLocationListener(com.here.sdk.core.LocationListener)">
<h3>removeLocationListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLocationListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core">LocationListener</a> listener)</span></div>
<div class="block">Removes a <a href="sdk-for-android-navigate-core-locationlistener" title="interface in com.here.sdk.core"><code>LocationListener</code></a> from the engine</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#removeLocationListener(com.here.sdk.core.LocationListener)">removeLocationListener</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be removed</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>addLocationStatusListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLocationStatusListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div class="block">Adds a <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> to the engine to get notified when there is an
 important status change.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#addLocationStatusListener(com.here.sdk.location.LocationStatusListener)">addLocationStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be added</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">
<h3>removeLocationStatusListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLocationStatusListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location">LocationStatusListener</a> listener)</span></div>
<div class="block">Removes a <a href="sdk-for-android-navigate-locationstatuslistener" title="interface in com.here.sdk.location"><code>LocationStatusListener</code></a> from the engine</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#removeLocationStatusListener(com.here.sdk.location.LocationStatusListener)">removeLocationStatusListener</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be removed</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>addLocationIssueListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addLocationIssueListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div class="block">Adds a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> to the engine to get notified when a location issue
 has occurred</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#addLocationIssueListener(com.here.sdk.location.LocationIssueListener)">addLocationIssueListener</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be added</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">
<h3>removeLocationIssueListener</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">removeLocationIssueListener</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location">LocationIssueListener</a> listener)</span></div>
<div class="block">Removes a <a href="sdk-for-android-navigate-locationissuelistener" title="interface in com.here.sdk.location"><code>LocationIssueListener</code></a> from the engine</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#removeLocationIssueListener(com.here.sdk.location.LocationIssueListener)">removeLocationIssueListener</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>listener</code> - The listener to be removed</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if the listener is null</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setLastKnownLocationPersistent(boolean)">
<h3>setLastKnownLocationPersistent</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-locationenginestatus" title="enum class in com.here.sdk.location">LocationEngineStatus</a></span> <span class="element-name">setLastKnownLocationPersistent</span><wbr/><span class="parameters">(boolean persistent)</span></div>
<div class="block">Enables or disables saving of last known location so it persists between application
 sessions. Defaults to enabled.</div>
<dl class="notes">
<dt>Specified by:</dt>
<dd><code><a href="sdk-for-android-navigate-locationenginebase#setLastKnownLocationPersistent(boolean)">setLastKnownLocationPersistent</a></code> in interface <code><a href="sdk-for-android-navigate-locationenginebase" title="interface in com.here.sdk.location">LocationEngineBase</a></code></dd>
<dt>Parameters:</dt>
<dd><code>persistent</code> - If true enables last known location to be saved persistently, or if false
         disables it.</dd>
<dt>Returns:</dt>
<dd>LocationEngineStatus.OK always.</dd>
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
