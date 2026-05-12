---
title: "RoadSign (API Reference)"
slug: "sdk-for-android-navigate-roadsign"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadSign.html -->
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
<div class="inheritance">com.here.sdk.navigation.RoadSign</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">RoadSign</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Describes a road sign.
 <p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
 Related APIs may change for new releases without a deprecation process.</p></p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#generalWarningType">generalWarningType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies the general warning to which the road sign belongs.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isPrioritySign">isPrioritySign</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Flag indicating if the road sign is a priority sign.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#localizedDuration">localizedDuration</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional length information during which the warning is applicable.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#localizedPreWarning">localizedPreWarning</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional pre-warning in terms of distance, of the upcoming warning or regulation.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#localizedSignValue">localizedSignValue</a></code></div>
<div class="col-last even-row-color">
<div class="block">Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#localizedValidityTime">localizedValidityTime</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.</div>
</div>
<div class="col-first even-row-color"><code>int</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#offsetInMeters">offsetInMeters</a></code></div>
<div class="col-last even-row-color">
<div class="block">The offset in meters from the beginning of the segment to the location of the road sign
 in positive direction.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#roadSignCategory">roadSignCategory</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The main category to which the road sign belongs.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#roadSignType">roadSignType</a></code></div>
<div class="col-last even-row-color">
<div class="block">Type of the road sign.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#travelDirection">travelDirection</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Segment direction which the road sign is applied.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#vehicleTypes">vehicleTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Specifies a list of vehicle types for which the road sign is applicable.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#weatherType">weatherType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Specifies the weather type for which the sign is applicable.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(int,com.here.sdk.routing.TravelDirection,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,boolean,com.here.sdk.navigation.GeneralWarningRoadSignType,java.util.List,com.here.sdk.navigation.WeatherType)">RoadSign</a><wbr/>(int offsetInMeters,
 <a href="sdk-for-android-navigate-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 <a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> roadSignType,
 <a href="sdk-for-android-navigate-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> roadSignCategory,
 boolean isPrioritySign,
 <a href="sdk-for-android-navigate-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 <a href="sdk-for-android-navigate-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance with default values.</div>
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
<section class="detail" id="offsetInMeters">
<h3>offsetInMeters</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">offsetInMeters</span></div>
<div class="block"><p>The offset in meters from the beginning of the segment to the location of the road sign
 in positive direction.</p></div>
</section>
</li>
<li>
<section class="detail" id="travelDirection">
<h3>travelDirection</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a></span> <span class="element-name">travelDirection</span></div>
<div class="block"><p>Segment direction which the road sign is applied.</p></div>
</section>
</li>
<li>
<section class="detail" id="roadSignType">
<h3>roadSignType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">roadSignType</span></div>
<div class="block"><p>Type of the road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="roadSignCategory">
<h3>roadSignCategory</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a></span> <span class="element-name">roadSignCategory</span></div>
<div class="block"><p>The main category to which the road sign belongs.</p></div>
</section>
</li>
<li>
<section class="detail" id="isPrioritySign">
<h3>isPrioritySign</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isPrioritySign</span></div>
<div class="block"><p>Flag indicating if the road sign is a priority sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="generalWarningType">
<h3>generalWarningType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a></span> <span class="element-name">generalWarningType</span></div>
<div class="block"><p>Specifies the general warning to which the road sign belongs.</p></div>
</section>
</li>
<li>
<section class="detail" id="vehicleTypes">
<h3>vehicleTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt;</span> <span class="element-name">vehicleTypes</span></div>
<div class="block"><p>Specifies a list of vehicle types for which the road sign is applicable.
 The list will be empty when the road sign is applicable for all vehicles including cars.</p></div>
</section>
</li>
<li>
<section class="detail" id="weatherType">
<h3>weatherType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a></span> <span class="element-name">weatherType</span></div>
<div class="block"><p>Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.</p></div>
</section>
</li>
<li>
<section class="detail" id="localizedSignValue">
<h3>localizedSignValue</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedSignValue</span></div>
<div class="block"><p>Optional value visible on the main sign related to specific road sign types, as it is printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="localizedPreWarning">
<h3>localizedPreWarning</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedPreWarning</span></div>
<div class="block"><p>Optional pre-warning in terms of distance, of the upcoming warning or regulation.
 The pre-warning information is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="localizedDuration">
<h3>localizedDuration</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedDuration</span></div>
<div class="block"><p>Optional length information during which the warning is applicable.
 Usually, this information is shown on a separate shield below the main shield.
 For example, a sign may warn on playing children for a length of 100 m, starting from
 the location of the warning sign.
 The length information (most likely with units) is given as printed on the local road sign.</p></div>
</section>
</li>
<li>
<section class="detail" id="localizedValidityTime">
<h3>localizedValidityTime</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-localizedtext" title="class in com.here.sdk.core">LocalizedText</a></span> <span class="element-name">localizedValidityTime</span></div>
<div class="block"><p>Optional text visible on the supplemental sign indicating specific
 time(s) at which the road sign is applicable.
 The time information is given as printed on the local road sign.</p></div>
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
<section class="detail" id="&lt;init&gt;(int,com.here.sdk.routing.TravelDirection,com.here.sdk.navigation.RoadSignType,com.here.sdk.navigation.RoadSignCategory,boolean,com.here.sdk.navigation.GeneralWarningRoadSignType,java.util.List,com.here.sdk.navigation.WeatherType)">
<h3>RoadSign</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">RoadSign</span><wbr/><span class="parameters">(int offsetInMeters,
 @NonNull
 <a href="sdk-for-android-navigate-routing-traveldirection" title="enum class in com.here.sdk.routing">TravelDirection</a> travelDirection,
 @NonNull
 <a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a> roadSignType,
 @NonNull
 <a href="sdk-for-android-navigate-roadsigncategory" title="enum class in com.here.sdk.navigation">RoadSignCategory</a> roadSignCategory,
 boolean isPrioritySign,
 @NonNull
 <a href="sdk-for-android-navigate-generalwarningroadsigntype" title="enum class in com.here.sdk.navigation">GeneralWarningRoadSignType</a> generalWarningType,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-roadsignvehicletype" title="enum class in com.here.sdk.navigation">RoadSignVehicleType</a>&gt; vehicleTypes,
 @NonNull
 <a href="sdk-for-android-navigate-weathertype" title="enum class in com.here.sdk.navigation">WeatherType</a> weatherType)</span></div>
<div class="block"><p>Creates a new instance with default values.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>offsetInMeters</code> - <p>The offset in meters from the beginning of the segment to the location of the road sign
 in positive direction.</p></dd>
<dd><code>travelDirection</code> - <p>Segment direction which the road sign is applied.</p></dd>
<dd><code>roadSignType</code> - <p>Type of the road sign.</p></dd>
<dd><code>roadSignCategory</code> - <p>The main category to which the road sign belongs.</p></dd>
<dd><code>isPrioritySign</code> - <p>Flag indicating if the road sign is a priority sign.</p></dd>
<dd><code>generalWarningType</code> - <p>Specifies the general warning to which the road sign belongs.</p></dd>
<dd><code>vehicleTypes</code> - <p>Specifies a list of vehicle types for which the road sign is applicable.
 The list will be empty when the road sign is applicable for all vehicles including cars.</p></dd>
<dd><code>weatherType</code> - <p>Specifies the weather type for which the sign is applicable. If weather type is <code>WeatherType.UNKNOWN</code>, the sign is actual for all weather types.</p></dd>
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
