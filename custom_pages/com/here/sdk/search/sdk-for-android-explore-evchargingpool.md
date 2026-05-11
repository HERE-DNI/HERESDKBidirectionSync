---
title: "EVChargingPool (API Reference)"
slug: "sdk-for-android-explore-evchargingpool"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- EVChargingPool.html -->
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
<li><a href="../../../../index.html">Overview</a></li>
<li><a href="package-summary.html">Package</a></li>
<li class="nav-bar-cell1-rev">Class</li>
<li><a href="package-tree.html">Tree</a></li>
<li><a href="../../../../deprecated-list.html">Deprecated</a></li>
<li><a href="../../../../index-all.html">Index</a></li>
<li><a href="../../../../help-doc.html#class">Help</a></li>
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="package-summary.html">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.search.EVChargingPool</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">EVChargingPool</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>A charging pool for electric vehicles is an area equipped with one or more charging stations.
 <p>Use <a href="PlaceCategory.html#BUSINESS_AND_SERVICES_EV_CHARGING_STATION"><code>PlaceCategory.BUSINESS_AND_SERVICES_EV_CHARGING_STATION</code></a> to find stations.
 In the <code>Details</code> of a <code>Place</code> result you can find the list of found pools containing stations,
 if any.
 <p>For offline EV rich attributes, also enable <a href="../core/engine/LayerConfiguration.Feature.html#EV"><code>LayerConfiguration.Feature.EV</code></a>
 in <a href="../core/engine/SDKOptions.html#layerConfiguration"><code>SDKOptions.layerConfiguration</code></a>.</p></p></p></div>
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
<div class="col-first even-row-color"><code><a href="EVAccessType.html" title="enum class in com.here.sdk.search">EVAccessType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#access">access</a></code></div>
<div class="col-last even-row-color">
<div class="block">The accessibility level of the charging pool, or <code>null</code> if unknown.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVAccessRestrictionReason.html" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#accessRestrictionReasons">accessRestrictionReasons</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Contains the list of reasons for restriction.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVChargingStation.html" title="class in com.here.sdk.search">EVChargingStation</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#chargingStations">chargingStations</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of charging stations.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#cpoId">cpoId</a></code></div>
<div class="col-last odd-row-color">
<div class="block">CPO (Charge Point Operator) id for charging pool.</div>
</div>
<div class="col-first even-row-color"><code><a href="EVChargingPoolDetails.html" title="class in com.here.sdk.search">EVChargingPoolDetails</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#details">details</a></code></div>
<div class="col-last even-row-color">
<div class="block">EV charging station attributes details.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EMobilityServiceProvider.html" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#eMobilityServiceProviders">eMobilityServiceProviders</a></code></div>
<div class="col-last odd-row-color">
<div class="block">List of e-Mobility Service Providers.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Evse.html" title="class in com.here.sdk.search">Evse</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#evseInfo">evseInfo</a></code></div>
<div class="col-last even-row-color">
<div class="block">Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#id">id</a></code></div>
<div class="col-last odd-row-color">
<div class="block">HERE ID of the charging pool.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(java.util.List,java.util.List,java.util.List)">EVChargingPool</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVChargingStation.html" title="class in com.here.sdk.search">EVChargingStation</a>&gt; chargingStations,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EMobilityServiceProvider.html" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt; eMobilityServiceProviders,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVAccessRestrictionReason.html" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt; accessRestrictionReasons)</code></div>
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
<section class="detail" id="chargingStations">
<h3>chargingStations</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVChargingStation.html" title="class in com.here.sdk.search">EVChargingStation</a>&gt;</span> <span class="element-name">chargingStations</span></div>
<div class="block"><p>List of charging stations.</p></div>
</section>
</li>
<li>
<section class="detail" id="eMobilityServiceProviders">
<h3>eMobilityServiceProviders</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EMobilityServiceProvider.html" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt;</span> <span class="element-name">eMobilityServiceProviders</span></div>
<div class="block"><p>List of e-Mobility Service Providers.
 Only online search fills this field.</p></div>
</section>
</li>
<li>
<section class="detail" id="access">
<h3>access</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="EVAccessType.html" title="enum class in com.here.sdk.search">EVAccessType</a></span> <span class="element-name">access</span></div>
<div class="block"><p>The accessibility level of the charging pool, or <code>null</code> if unknown.</p></div>
</section>
</li>
<li>
<section class="detail" id="accessRestrictionReasons">
<h3>accessRestrictionReasons</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVAccessRestrictionReason.html" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt;</span> <span class="element-name">accessRestrictionReasons</span></div>
<div class="block"><p>Contains the list of reasons for restriction.
 Populated only for offline search and when access is <a href="EVAccessType.html#RESTRICTED_ACCESS"><code>EVAccessType.RESTRICTED_ACCESS</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="details">
<h3>details</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="EVChargingPoolDetails.html" title="class in com.here.sdk.search">EVChargingPoolDetails</a></span> <span class="element-name">details</span></div>
<div class="block"><p>EV charging station attributes details. It is available only for a place that has charging station
 for electric vehicles. Only offline search fills this field.
 <p><strong>Note:</strong> Not available as part of <a href="Suggestion.html" title="class in com.here.sdk.search"><code>Suggestion</code></a> results.</p></p></div>
</section>
</li>
<li>
<section class="detail" id="id">
<h3>id</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">id</span></div>
<div class="block"><p>HERE ID of the charging pool.
 Only online search fills this field.</p></div>
</section>
</li>
<li>
<section class="detail" id="cpoId">
<h3>cpoId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">cpoId</span></div>
<div class="block"><p>CPO (Charge Point Operator) id for charging pool.
 Only online search fills this field.</p></div>
</section>
</li>
<li>
<section class="detail" id="evseInfo">
<h3>evseInfo</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="Evse.html" title="class in com.here.sdk.search">Evse</a>&gt;</span> <span class="element-name">evseInfo</span></div>
<div class="block"><p>Charge Point Operator (CPO) ID uses the Electric Vehicle Supply Equipment ID (EVSE ID) for an exact identification of the charging infrastructure and charging point.
 Only online search fills this field.</p></div>
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
<section class="detail" id="&lt;init&gt;(java.util.List,java.util.List,java.util.List)">
<h3>EVChargingPool</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">EVChargingPool</span><wbr/><span class="parameters">(@NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVChargingStation.html" title="class in com.here.sdk.search">EVChargingStation</a>&gt; chargingStations,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EMobilityServiceProvider.html" title="class in com.here.sdk.search">EMobilityServiceProvider</a>&gt; eMobilityServiceProviders,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="EVAccessRestrictionReason.html" title="enum class in com.here.sdk.search">EVAccessRestrictionReason</a>&gt; accessRestrictionReasons)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>chargingStations</code> - <p>List of charging stations.</p></dd>
<dd><code>eMobilityServiceProviders</code> - <p>List of e-Mobility Service Providers.
 Only online search fills this field.</p></dd>
<dd><code>accessRestrictionReasons</code> - <p>Contains the list of reasons for restriction.
 Populated only for offline search and when access is <a href="EVAccessType.html#RESTRICTED_ACCESS"><code>EVAccessType.RESTRICTED_ACCESS</code></a>.</p></dd>
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
