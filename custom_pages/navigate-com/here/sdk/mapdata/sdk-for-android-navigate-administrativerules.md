---
title: "AdministrativeRules (API Reference)"
slug: "sdk-for-android-navigate-administrativerules"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- AdministrativeRules.html -->
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
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapdata</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.mapdata.AdministrativeRules</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">AdministrativeRules</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Represents a set of administrative rules for a country or a state.</p></div>
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
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#adminContextId">adminContextId</a></code></div>
<div class="col-last even-row-color">
<div class="block">The administrative context ID used to identify this administrative region.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-bloodalcoholcontentlimit" title="class in com.here.sdk.mapdata">BloodAlcoholContentLimit</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#bloodAlcoholContentLimit">bloodAlcoholContentLimit</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the rules regarding alcohol in blood content limit in a country or state for
 all types of drivers.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#countryCode">countryCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">Country code for which the administrative rules apply.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-core-timerule" title="class in com.here.sdk.core">TimeRule</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#daylightSavingPeriod">daylightSavingPeriod</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Time rule indicating the time periods in which daylight savings applies.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-drivingside" title="enum class in com.here.sdk.mapdata">DrivingSide</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#drivingSide">drivingSide</a></code></div>
<div class="col-last even-row-color">
<div class="block">The side of the road used for driving in the country or state.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-headlightsrequirement" title="enum class in com.here.sdk.mapdata">HeadlightsRequirement</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#headlightsRequirements">headlightsRequirements</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates in which conditions should the headlights be turned on.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isCleanAirStickerRequired">isCleanAirStickerRequired</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates if the country or state requires an ecological sticker.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isTollRequired">isTollRequired</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates if the country or state requires paid fees for usage of the motorways / controlled access
 roads.</div>
</div>
<div class="col-first even-row-color"><code>boolean</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#isTollStickerRequired">isTollStickerRequired</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates if the country or state requires a toll sticker.</div>
</div>
<div class="col-first odd-row-color"><code>boolean</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#isUturnRestricted">isUturnRestricted</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates if performing a u-turn maneuver is restricted.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#parentAdminContextIds">parentAdminContextIds</a></code></div>
<div class="col-last even-row-color">
<div class="block">The list of parent administrative context IDs.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-parkingsideregulation" title="enum class in com.here.sdk.mapdata">ParkingSideRegulation</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#parkingSideRegulations">parkingSideRegulations</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the regulations for parking on the side of the road.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-pretripplanning" title="class in com.here.sdk.mapdata">PreTripPlanning</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#preTripPlanning">preTripPlanning</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the legal requirements to be considered before a trip for all vehicles types.</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-navigate-transport-generalvehiclespeedlimits" title="class in com.here.sdk.transport">GeneralVehicleSpeedLimits</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#speedLimits">speedLimits</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The general speed limits in the country or state.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#stateCode">stateCode</a></code></div>
<div class="col-last even-row-color">
<div class="block">The state code for which the administrative rules apply.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#timeZoneOffsetsInMinutes">timeZoneOffsetsInMinutes</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The time zone offset from UTC of the country or state expressed in minutes.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-tollsystem" title="class in com.here.sdk.mapdata">TollSystem</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#tollSystems">tollSystems</a></code></div>
<div class="col-last even-row-color">
<div class="block">Indicates the toll systems present in a country or state.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-turnonredregulation" title="enum class in com.here.sdk.mapdata">TurnOnRedRegulation</a>&gt;</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="#turnOnRedRegulations">turnOnRedRegulations</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Indicates the regulations for turning on the red color of the traffic light.</div>
</div>
<div class="col-first even-row-color"><code><a href="sdk-for-android-navigate-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="#unitSystem">unitSystem</a></code></div>
<div class="col-last even-row-color">
<div class="block">Defines the measurement system used for distances.</div>
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
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="#%3Cinit%3E(com.here.sdk.mapdata.AdminContextId)">AdministrativeRules</a><wbr/>(<a href="sdk-for-android-navigate-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a> adminContextId)</code></div>
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
<section class="detail" id="countryCode">
<h3>countryCode</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-countrycode" title="enum class in com.here.sdk.core">CountryCode</a></span> <span class="element-name">countryCode</span></div>
<div class="block"><p>Country code for which the administrative rules apply.</p></div>
</section>
</li>
<li>
<section class="detail" id="stateCode">
<h3>stateCode</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">stateCode</span></div>
<div class="block"><p>The state code for which the administrative rules apply. It represents the state / province code. It is
 a 1 to 3 upper-case characters string that follows the ISO 3166-2 standard, but without the preceding
 country code (e.g. for Texas, the state code will be TX).
 It will be <code>null</code> if the rules are applying to the entire country and not just a specific state.</p></div>
</section>
</li>
<li>
<section class="detail" id="adminContextId">
<h3>adminContextId</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a></span> <span class="element-name">adminContextId</span></div>
<div class="block"><p>The administrative context ID used to identify this administrative region.
 This ID is used internally to load commercial vehicle regulations and other
 administrative-specific data.</p></div>
</section>
</li>
<li>
<section class="detail" id="parentAdminContextIds">
<h3>parentAdminContextIds</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a>&gt;</span> <span class="element-name">parentAdminContextIds</span></div>
<div class="block"><p>The list of parent administrative context IDs.
 These represent the administrative hierarchy (e.g., state-&gt;country).
 Used internally to load commercial vehicle regulations that may be inherited
 from parent administrative regions.</p></div>
</section>
</li>
<li>
<section class="detail" id="drivingSide">
<h3>drivingSide</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-drivingside" title="enum class in com.here.sdk.mapdata">DrivingSide</a></span> <span class="element-name">drivingSide</span></div>
<div class="block"><p>The side of the road used for driving in the country or state. Defaults to right driving side.</p></div>
</section>
</li>
<li>
<section class="detail" id="unitSystem">
<h3>unitSystem</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-unitsystem" title="enum class in com.here.sdk.core">UnitSystem</a></span> <span class="element-name">unitSystem</span></div>
<div class="block"><p>Defines the measurement system used for distances. Defaults to metric measurement system.</p></div>
</section>
</li>
<li>
<section class="detail" id="speedLimits">
<h3>speedLimits</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-transport-generalvehiclespeedlimits" title="class in com.here.sdk.transport">GeneralVehicleSpeedLimits</a></span> <span class="element-name">speedLimits</span></div>
<div class="block"><p>The general speed limits in the country or state.</p></div>
</section>
</li>
<li>
<section class="detail" id="timeZoneOffsetsInMinutes">
<h3>timeZoneOffsetsInMinutes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-time-duration" title="class in com.here.time">Duration</a>&gt;</span> <span class="element-name">timeZoneOffsetsInMinutes</span></div>
<div class="block"><p>The time zone offset from UTC of the country or state expressed in minutes. The value can also be negative
 (e.g.: Eastern Standard Time (EST) will be -360 minutes, Central European Time (CET) will be 60 minutes).
 Defaults to 0 minutes.
 <strong>Note:</strong> A time zone with a positive shift of 1 hour and 30 minutes will result in a time zone offset of
 90 minutes. A time zone with a negative shift of 3 hour and 30 minutes will result in an time zone offset
 of -210 minutes. In order to properly calculate the time zone offset, the [AdministrativeRules.daylight_saving_period]
 should be taken into consideration and if the daylight savings time is observed at the time of the
 calculation, then a value of 60 minutes should be substracted from the time zone offset.</p></div>
</section>
</li>
<li>
<section class="detail" id="daylightSavingPeriod">
<h3>daylightSavingPeriod</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-core-timerule" title="class in com.here.sdk.core">TimeRule</a></span> <span class="element-name">daylightSavingPeriod</span></div>
<div class="block"><p>Time rule indicating the time periods in which daylight savings applies.
 If the field is 'null' then daylight savings time is not observed in the country or state.
 <strong>Note:</strong> In order to properly calculate the time zone offset, if the daylight savings time is observed at
 the time of the calculation, then a value of 60 minutes should be substracted from the time zone offset.</p></div>
</section>
</li>
<li>
<section class="detail" id="isUturnRestricted">
<h3>isUturnRestricted</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isUturnRestricted</span></div>
<div class="block"><p>Indicates if performing a u-turn maneuver is restricted. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="headlightsRequirements">
<h3>headlightsRequirements</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-headlightsrequirement" title="enum class in com.here.sdk.mapdata">HeadlightsRequirement</a>&gt;</span> <span class="element-name">headlightsRequirements</span></div>
<div class="block"><p>Indicates in which conditions should the headlights be turned on. Defaults to an empty list,
 which means that by default there are no special situations in which the headlights should be
 turned on.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTollRequired">
<h3>isTollRequired</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTollRequired</span></div>
<div class="block"><p>Indicates if the country or state requires paid fees for usage of the motorways / controlled access
 roads. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="isTollStickerRequired">
<h3>isTollStickerRequired</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isTollStickerRequired</span></div>
<div class="block"><p>Indicates if the country or state requires a toll sticker. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="turnOnRedRegulations">
<h3>turnOnRedRegulations</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-turnonredregulation" title="enum class in com.here.sdk.mapdata">TurnOnRedRegulation</a>&gt;</span> <span class="element-name">turnOnRedRegulations</span></div>
<div class="block"><p>Indicates the regulations for turning on the red color of the traffic light.</p></div>
</section>
</li>
<li>
<section class="detail" id="parkingSideRegulations">
<h3>parkingSideRegulations</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-parkingsideregulation" title="enum class in com.here.sdk.mapdata">ParkingSideRegulation</a>&gt;</span> <span class="element-name">parkingSideRegulations</span></div>
<div class="block"><p>Indicates the regulations for parking on the side of the road.</p></div>
</section>
</li>
<li>
<section class="detail" id="isCleanAirStickerRequired">
<h3>isCleanAirStickerRequired</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">isCleanAirStickerRequired</span></div>
<div class="block"><p>Indicates if the country or state requires an ecological sticker. Defaults to <code>false</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="bloodAlcoholContentLimit">
<h3>bloodAlcoholContentLimit</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-bloodalcoholcontentlimit" title="class in com.here.sdk.mapdata">BloodAlcoholContentLimit</a></span> <span class="element-name">bloodAlcoholContentLimit</span></div>
<div class="block"><p>Indicates the rules regarding alcohol in blood content limit in a country or state for
 all types of drivers.</p></div>
</section>
</li>
<li>
<section class="detail" id="tollSystems">
<h3>tollSystems</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-tollsystem" title="class in com.here.sdk.mapdata">TollSystem</a>&gt;</span> <span class="element-name">tollSystems</span></div>
<div class="block"><p>Indicates the toll systems present in a country or state.</p></div>
</section>
</li>
<li>
<section class="detail" id="preTripPlanning">
<h3>preTripPlanning</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-pretripplanning" title="class in com.here.sdk.mapdata">PreTripPlanning</a></span> <span class="element-name">preTripPlanning</span></div>
<div class="block"><p>Indicates the legal requirements to be considered before a trip for all vehicles types.</p></div>
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
<section class="detail" id="&lt;init&gt;(com.here.sdk.mapdata.AdminContextId)">
<h3>AdministrativeRules</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">AdministrativeRules</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-navigate-admincontextid" title="class in com.here.sdk.mapdata">AdminContextId</a> adminContextId)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>adminContextId</code> - <p>The administrative context ID used to identify this administrative region.
 This ID is used internally to load commercial vehicle regulations and other
 administrative-specific data.</p></dd>
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
