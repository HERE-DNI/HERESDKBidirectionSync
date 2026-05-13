---
title: "RoadSignType (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-navigation-roadsigntype"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- RoadSignType.html -->
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
<li><a href="#nested-class-summary">Nested</a> | </li>
<li><a href="#enum-constant-summary">Enum Constants</a> | </li>
<li>Field | </li>
<li><a href="#method-summary">Method</a></li>
</ul>
<ul class="sub-nav-list">
<li>Detail: </li>
<li><a href="#enum-constant-detail">Enum Constants</a> | </li>
<li>Field | </li>
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
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a>&gt;
<div class="inheritance">com.here.sdk.navigation.RoadSignType</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>
<hr/>
<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">RoadSignType</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a>&gt;</span></div>
<div class="block"><p>A road sign type classifying road signs that can appear along a road.
 Some signs are standardized and look the same in all countries, e.g. <a href="#STOP_SIGN"><code>STOP_SIGN</code></a>.
 In general, the visual appearance of the road signs can differ across countries.
 Some road signs can be combined with other signs, like <code>WeatherType</code> signs. The road sign will be always shown topmost.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="inherited-list">

<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">Enum.EnumDesc</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a> extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" title="class or interface in java.lang">E</a>&gt;&gt;</code></div>
</section>
</li>
<!-- =========== ENUM CONSTANT SUMMARY =========== -->
<li>
<section class="constants-summary" id="enum-constant-summary">

<div class="caption"><span>Enum Constants</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Enum Constant</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#ACCIDENT_HAZARD">ACCIDENT_HAZARD</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating accident hazard.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#ANIMAL_CROSSING">ANIMAL_CROSSING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating animal crossing.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#BICYCLE_CROSSING">BICYCLE_CROSSING</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating bicycles crossing.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#CONGESTION_HAZARD">CONGESTION_HAZARD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating congestion hazard.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#CROSSING_WITH_PRIORITY_FROM_THE_RIGHT">CROSSING_WITH_PRIORITY_FROM_THE_RIGHT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating crossing with priority from the right.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#DOUBLE_HAIRPIN">DOUBLE_HAIRPIN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a double hairpin.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#EMBANKMENT">EMBANKMENT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating embankment.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#END_OF_ALL_RESTRICTIONS">END_OF_ALL_RESTRICTIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating the end of all restrictions.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#END_OF_LOW_GEAR">END_OF_LOW_GEAR</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating the use of low gear.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#END_OF_NO_ENGINE_BRAKE">END_OF_NO_ENGINE_BRAKE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating the end of no engine brake zone.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#END_OF_NO_OVERTAKING">END_OF_NO_OVERTAKING</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating the ending of a no overtaking zone.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#END_OF_NO_OVERTAKING_TRUCKS">END_OF_NO_OVERTAKING_TRUCKS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating the end of no overtaking trucks zone.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#FALLING_ROCKS">FALLING_ROCKS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating falling rocks.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#FLOOD_AREA">FLOOD_AREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a flood area.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#GENERAL_CURVE">GENERAL_CURVE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a general curve.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#GENERAL_HILL">GENERAL_HILL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a general hill.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#GENERAL_WARNING_SIGN">GENERAL_WARNING_SIGN</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a general warning.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#HORN_SIGN">HORN_SIGN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating restriction for horning.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#HUMP_BRIDGE">HUMP_BRIDGE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a hump bridge.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#ICY_CONDITIONS">ICY_CONDITIONS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating icy conditions.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#LANE_MERGE_CENTER">LANE_MERGE_CENTER</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating merging of the center lane.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#LANE_MERGE_LEFT">LANE_MERGE_LEFT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating merging of the left lane.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#LANE_MERGE_RIGHT">LANE_MERGE_RIGHT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating merging of the right lane.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#LATERAL_WIND">LATERAL_WIND</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating lateral winds.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#LOW_GEAR">LOW_GEAR</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating the use of low gear.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#NO_CAMPER_OR_MOTORHOME_ALLOWED">NO_CAMPER_OR_MOTORHOME_ALLOWED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating no camper or motorhome allowed.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#NO_ENGINE_BRAKE">NO_ENGINE_BRAKE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating no engine brake.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#NO_IDLING">NO_IDLING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating no idling.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#NO_TOWED_CARAVAN_ALLOWED">NO_TOWED_CARAVAN_ALLOWED</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating no towed caravan allowed.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#NO_TOWED_TRAILER_ALLOWED">NO_TOWED_TRAILER_ALLOWED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating no towed trailer allowed.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#NO_TURN_ON_RED">NO_TURN_ON_RED</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating no turning on red permitted.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#OBSTACLE">OBSTACLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating an obstacle.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#PEDESTRIAN_CROSSING">PEDESTRIAN_CROSSING</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating pedestrian crossing.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#PRIORITY_OVER_ONCOMING_TRAFFIC">PRIORITY_OVER_ONCOMING_TRAFFIC</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating priority over oncoming traffic.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#PROTECTED_OVERTAKING_EXTRA_LANE">PROTECTED_OVERTAKING_EXTRA_LANE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating an extra lane for overtaking.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE">PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating an extra lane for overtaking on the left side.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE">PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating an extra lane for overtaking on the right side.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#RAILWAY_CROSSING_PROTECTED">RAILWAY_CROSSING_PROTECTED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a protected railway crossing.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#RAILWAY_CROSSING_UNPROTECTED">RAILWAY_CROSSING_UNPROTECTED</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating an unprotected railway crossing.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#RISK_OF_GROUNDING">RISK_OF_GROUNDING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating risk of grounding.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#ROAD_NARROWS">ROAD_NARROWS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a narrowing road.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SCHOOL_ZONE">SCHOOL_ZONE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating school zone.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SHARP_CURVE_LEFT">SHARP_CURVE_LEFT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a sharp curve to the left.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#SHARP_CURVE_RIGHT">SHARP_CURVE_RIGHT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a sharp curve to the right.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#SLIPPERY_ROAD">SLIPPERY_ROAD</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating slippery road.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#START_OF_NO_OVERTAKING">START_OF_NO_OVERTAKING</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating the starting of a no overtaking zone.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#START_OF_NO_OVERTAKING_TRUCKS">START_OF_NO_OVERTAKING_TRUCKS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating no overtaking trucks.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#STEEP_HILL_DOWNWARDS">STEEP_HILL_DOWNWARDS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a steep hill downward.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#STEEP_HILL_UPWARDS">STEEP_HILL_UPWARDS</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a steep hill upwards.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#STOP_SIGN">STOP_SIGN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a stop.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#TRAMWAY_CROSSING">TRAMWAY_CROSSING</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a tramway crossing.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#TRIPLE_HAIRPIN">TRIPLE_HAIRPIN</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a triple hairpin.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#TRUCK_ROLLOVER">TRUCK_ROLLOVER</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating truck rollover.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#TURN_PERMITTED_ON_RED">TURN_PERMITTED_ON_RED</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating turning on red permitted.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#TWO_STAGE_LEFT">TWO_STAGE_LEFT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating that turning left requires a two-stage maneuver,
 also known as a hook turn or Copenhagen Left, which is a special maneuver to safely
 make a left turn at an intersection without crossing oncoming traffic.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#TWO_STAGE_RIGHT">TWO_STAGE_RIGHT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating turning right with the specified vehicle type requires a two stage maneuver.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#TWO_WAY_TRAFFIC">TWO_WAY_TRAFFIC</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating two way traffic.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#UNEVEN_ROAD">UNEVEN_ROAD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating uneven road.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#UNKNOWN">UNKNOWN</a></code></div>
<div class="col-last even-row-color">
<div class="block">Unknown road sign type</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#URBAN_AREA">URBAN_AREA</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating urban area.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#WINDING_ROAD_STARTING_LEFT">WINDING_ROAD_STARTING_LEFT</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating a winding road starting left.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#WINDING_ROAD_STARTING_RIGHT">WINDING_ROAD_STARTING_RIGHT</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating a winding road starting right.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#YIELD">YIELD</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating yielding.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="#YIELD_TO_BICYCLES">YIELD_TO_BICYCLES</a></code></div>
<div class="col-last odd-row-color">
<div class="block">A sign indicating yielding to bicycles.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="#YIELD_TO_ONCOMING_TRAFFIC">YIELD_TO_ONCOMING_TRAFFIC</a></code></div>
<div class="col-last even-row-color">
<div class="block">A sign indicating yielding to oncoming traffic.</div>
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
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="#values()">values</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Enum">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" title="class or interface in java.lang">compareTo</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" title="class or interface in java.lang">describeConstable</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" title="class or interface in java.lang">getDeclaringClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" title="class or interface in java.lang">name</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" title="class or interface in java.lang">ordinal</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" title="class or interface in java.lang">valueOf</a></code></div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ ENUM CONSTANT DETAIL =========== -->
<li>
<section class="constant-details" id="enum-constant-detail">

<ul class="member-list">
<li>
<section class="detail" id="UNKNOWN">
<h3>UNKNOWN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">UNKNOWN</span></div>
<div class="block"><p>Unknown road sign type</p></div>
</section>
</li>
<li>
<section class="detail" id="START_OF_NO_OVERTAKING">
<h3>START_OF_NO_OVERTAKING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">START_OF_NO_OVERTAKING</span></div>
<div class="block"><p>A sign indicating the starting of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#No_overtaking_or_passing_signs">Start of no overtaking sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="END_OF_NO_OVERTAKING">
<h3>END_OF_NO_OVERTAKING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">END_OF_NO_OVERTAKING</span></div>
<div class="block"><p>A sign indicating the ending of a no overtaking zone. Example: <a href="https://en.wikipedia.org/wiki/Prohibitory_traffic_sign#End_of_overtaking_signs">End of no overtaking sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="PROTECTED_OVERTAKING_EXTRA_LANE">
<h3>PROTECTED_OVERTAKING_EXTRA_LANE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">PROTECTED_OVERTAKING_EXTRA_LANE</span></div>
<div class="block"><p>A sign indicating an extra lane for overtaking. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-3.svg">Protected overtaking extra lane sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE">
<h3>PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">PROTECTED_OVERTAKING_EXTRA_LANE_RIGHT_SIDE</span></div>
<div class="block"><p>A sign indicating an extra lane for overtaking on the right side. Example: <a href="https://en.wikipedia.org/wiki/Passing_lane#/media/File:MUTCD_R4-16.svg">Protected overtaking extra lane on the right side sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE">
<h3>PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">PROTECTED_OVERTAKING_EXTRA_LANE_LEFT_SIDE</span></div>
<div class="block"><p>A sign indicating an extra lane for overtaking on the left side. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_R6-29.svg">Protected overtaking extra lane on the left side sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="LANE_MERGE_RIGHT">
<h3>LANE_MERGE_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">LANE_MERGE_RIGHT</span></div>
<div class="block"><p>A sign indicating merging of the right lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W4-3R.svg">Merge right lane sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="LANE_MERGE_LEFT">
<h3>LANE_MERGE_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">LANE_MERGE_LEFT</span></div>
<div class="block"><p>A sign indicating merging of the left lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Mauritius#/media/File:Mauritius_Road_Signs_-_Warning_Sign_-_Traffic_Merging_From_Left_Behind.svg">Merge left lane sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="LANE_MERGE_CENTER">
<h3>LANE_MERGE_CENTER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">LANE_MERGE_CENTER</span></div>
<div class="block"><p>A sign indicating merging of the center lane. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:Roadsign_lane_drop_ahead.svg">Merge center lane sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="RAILWAY_CROSSING_PROTECTED">
<h3>RAILWAY_CROSSING_PROTECTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">RAILWAY_CROSSING_PROTECTED</span></div>
<div class="block"><p>A sign indicating a protected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-4.svg">Protected railway crossing sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="RAILWAY_CROSSING_UNPROTECTED">
<h3>RAILWAY_CROSSING_UNPROTECTED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">RAILWAY_CROSSING_UNPROTECTED</span></div>
<div class="block"><p>A sign indicating an unprotected railway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W7-7-L.svg">Protected railway crossing sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="ROAD_NARROWS">
<h3>ROAD_NARROWS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">ROAD_NARROWS</span></div>
<div class="block"><p>A sign indicating a narrowing road. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W4-3.svg">Road narrows sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="SHARP_CURVE_LEFT">
<h3>SHARP_CURVE_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">SHARP_CURVE_LEFT</span></div>
<div class="block"><p>A sign indicating a sharp curve to the left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512L.svg">Sharp curve left sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="SHARP_CURVE_RIGHT">
<h3>SHARP_CURVE_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">SHARP_CURVE_RIGHT</span></div>
<div class="block"><p>A sign indicating a sharp curve to the right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_512.svg">Sharp curve right sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="WINDING_ROAD_STARTING_LEFT">
<h3>WINDING_ROAD_STARTING_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">WINDING_ROAD_STARTING_LEFT</span></div>
<div class="block"><p>A sign indicating a winding road starting left. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513.svg">Winding road starting left sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="WINDING_ROAD_STARTING_RIGHT">
<h3>WINDING_ROAD_STARTING_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">WINDING_ROAD_STARTING_RIGHT</span></div>
<div class="block"><p>A sign indicating a winding road starting right. Example: <a href="https://en.wikipedia.org/wiki/File:UK_traffic_sign_513R.svg">Winding road starting right sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="START_OF_NO_OVERTAKING_TRUCKS">
<h3>START_OF_NO_OVERTAKING_TRUCKS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">START_OF_NO_OVERTAKING_TRUCKS</span></div>
<div class="block"><p>A sign indicating no overtaking trucks. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4c.svg">No overtaking trucks sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="END_OF_NO_OVERTAKING_TRUCKS">
<h3>END_OF_NO_OVERTAKING_TRUCKS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">END_OF_NO_OVERTAKING_TRUCKS</span></div>
<div class="block"><p>A sign indicating the end of no overtaking trucks zone. Example: <a href="https://en.wikipedia.org/wiki/File:Vorschriftszeichen_4d.svg">End of no overtaking trucks sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="STEEP_HILL_UPWARDS">
<h3>STEEP_HILL_UPWARDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">STEEP_HILL_UPWARDS</span></div>
<div class="block"><p>A sign indicating a steep hill upwards. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(b).svg">Steep hills upwards sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="STEEP_HILL_DOWNWARDS">
<h3>STEEP_HILL_DOWNWARDS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">STEEP_HILL_DOWNWARDS</span></div>
<div class="block"><p>A sign indicating a steep hill downward. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-9(a).svg">Steep hills downwards sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="STOP_SIGN">
<h3>STOP_SIGN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">STOP_SIGN</span></div>
<div class="block"><p>A sign indicating a stop. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_RUS-027.svg">Stop sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="LATERAL_WIND">
<h3>LATERAL_WIND</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">LATERAL_WIND</span></div>
<div class="block"><p>A sign indicating lateral winds. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-226.svg">Lateral winds sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="GENERAL_WARNING_SIGN">
<h3>GENERAL_WARNING_SIGN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">GENERAL_WARNING_SIGN</span></div>
<div class="block"><p>A sign indicating a general warning. Example: <a href="https://en.wikipedia.org/wiki/File:Hong_Kong_road_sign_240.svg">General warning sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="RISK_OF_GROUNDING">
<h3>RISK_OF_GROUNDING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">RISK_OF_GROUNDING</span></div>
<div class="block"><p>A sign indicating risk of grounding. Example: <a href="https://en.wikipedia.org/wiki/File:Croatia_road_sign_A31.svg">Risk of grounding sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="GENERAL_CURVE">
<h3>GENERAL_CURVE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">GENERAL_CURVE</span></div>
<div class="block"><p>A sign indicating a general curve. Example: <a href="https://en.wikipedia.org/wiki/File:Italian_traffic_signs_-_curva_pericolosa_a_sinistra.svg">General curve sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="END_OF_ALL_RESTRICTIONS">
<h3>END_OF_ALL_RESTRICTIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">END_OF_ALL_RESTRICTIONS</span></div>
<div class="block"><p>A sign indicating the end of all restrictions. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_374.svg">End of all restrictions sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="GENERAL_HILL">
<h3>GENERAL_HILL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">GENERAL_HILL</span></div>
<div class="block"><p>A sign indicating a general hill. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W7-1A.svg">General hill sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="ANIMAL_CROSSING">
<h3>ANIMAL_CROSSING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">ANIMAL_CROSSING</span></div>
<div class="block"><p>A sign indicating animal crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_13b.svg">Animal crossing sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="ICY_CONDITIONS">
<h3>ICY_CONDITIONS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">ICY_CONDITIONS</span></div>
<div class="block"><p>A sign indicating icy conditions. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-185.png">Icy conditions sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="SLIPPERY_ROAD">
<h3>SLIPPERY_ROAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">SLIPPERY_ROAD</span></div>
<div class="block"><p>A sign indicating slippery road. Example: <a href="https://en.wikipedia.org/wiki/File:Argentina_MSV_2017_road_sign_P-12.svg">Slippery road sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="FALLING_ROCKS">
<h3>FALLING_ROCKS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">FALLING_ROCKS</span></div>
<div class="block"><p>A sign indicating falling rocks. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_1.25.2.svg">Falling rocks sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="SCHOOL_ZONE">
<h3>SCHOOL_ZONE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">SCHOOL_ZONE</span></div>
<div class="block"><p>A sign indicating school zone. Example: <a href="https://en.wikipedia.org/wiki/File:Mauritius_Road_Signs_-_Warning_Sign_-_Children.svg">School zone sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TRAMWAY_CROSSING">
<h3>TRAMWAY_CROSSING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TRAMWAY_CROSSING</span></div>
<div class="block"><p>A sign indicating a tramway crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W5-41.svg">Tramway crossing sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="CONGESTION_HAZARD">
<h3>CONGESTION_HAZARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">CONGESTION_HAZARD</span></div>
<div class="block"><p>A sign indicating congestion hazard. Example: <a href="https://en.wikipedia.org/wiki/File:Czech_Republic_road_sign_A_23.svg">Congestion hazard sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="ACCIDENT_HAZARD">
<h3>ACCIDENT_HAZARD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">ACCIDENT_HAZARD</span></div>
<div class="block"><p>A sign indicating accident hazard. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AK31.svg">Accident hazard sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="PRIORITY_OVER_ONCOMING_TRAFFIC">
<h3>PRIORITY_OVER_ONCOMING_TRAFFIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">PRIORITY_OVER_ONCOMING_TRAFFIC</span></div>
<div class="block"><p>A sign indicating priority over oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Zeichen_308_-_Vorrang_vor_dem_Gegenverkehr,_StVO_1992.svg">Priority over oncoming traffic sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="YIELD_TO_ONCOMING_TRAFFIC">
<h3>YIELD_TO_ONCOMING_TRAFFIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">YIELD_TO_ONCOMING_TRAFFIC</span></div>
<div class="block"><p>A sign indicating yielding to oncoming traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Moldova_road_sign_2.5.svg">Yield to oncoming traffic sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="CROSSING_WITH_PRIORITY_FROM_THE_RIGHT">
<h3>CROSSING_WITH_PRIORITY_FROM_THE_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">CROSSING_WITH_PRIORITY_FROM_THE_RIGHT</span></div>
<div class="block"><p>A sign indicating crossing with priority from the right. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_France#/media/File:France_road_sign_AB1.svg">Crossing with priority from the right sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="PEDESTRIAN_CROSSING">
<h3>PEDESTRIAN_CROSSING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">PEDESTRIAN_CROSSING</span></div>
<div class="block"><p>A sign indicating pedestrian crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Estonia_road_sign_171.svg">Pedestrian crossing sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="YIELD">
<h3>YIELD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">YIELD</span></div>
<div class="block"><p>A sign indicating yielding. Example: <a href="https://en.wikipedia.org/wiki/File:Ontario_Wb-1A.svg">Yield sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="DOUBLE_HAIRPIN">
<h3>DOUBLE_HAIRPIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">DOUBLE_HAIRPIN</span></div>
<div class="block"><p>A sign indicating a double hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Australia#/media/File:Australia_road_sign_W1-7-L.svg">Double hairpin sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TRIPLE_HAIRPIN">
<h3>TRIPLE_HAIRPIN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TRIPLE_HAIRPIN</span></div>
<div class="block"><p>A sign indicating a triple hairpin. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_doppia_curva_sx.svg">Triple hairpin sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="EMBANKMENT">
<h3>EMBANKMENT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">EMBANKMENT</span></div>
<div class="block"><p>A sign indicating embankment. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-138.png">Embankment sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TWO_WAY_TRAFFIC">
<h3>TWO_WAY_TRAFFIC</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TWO_WAY_TRAFFIC</span></div>
<div class="block"><p>A sign indicating two way traffic. Example: <a href="https://en.wikipedia.org/wiki/File:Gefahrenzeichen_14.svg">Two way traffic sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="URBAN_AREA">
<h3>URBAN_AREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">URBAN_AREA</span></div>
<div class="block"><p>A sign indicating urban area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_preavviso_intersezione.svg">Urban area sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="HUMP_BRIDGE">
<h3>HUMP_BRIDGE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">HUMP_BRIDGE</span></div>
<div class="block"><p>A sign indicating a hump bridge. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_528.svg">Hump bridge sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="UNEVEN_ROAD">
<h3>UNEVEN_ROAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">UNEVEN_ROAD</span></div>
<div class="block"><p>A sign indicating uneven road. Example: <a href="https://en.wikipedia.org/wiki/File:IE_road_sign_W-133.svg">Uneven road sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="FLOOD_AREA">
<h3>FLOOD_AREA</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">FLOOD_AREA</span></div>
<div class="block"><p>A sign indicating a flood area. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Italy#/media/File:Italian_traffic_signs_-_zona_soggetta_ad_allagamento.svg">Flood area sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="OBSTACLE">
<h3>OBSTACLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">OBSTACLE</span></div>
<div class="block"><p>A sign indicating an obstacle. Example: <a href="https://en.wikipedia.org/wiki/Warning_sign#/media/File:Belgian_road_sign_A51.svg">Obstacle sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="HORN_SIGN">
<h3>HORN_SIGN</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">HORN_SIGN</span></div>
<div class="block"><p>A sign indicating restriction for horning. Example: <a href="https://en.wikipedia.org/wiki/File:EE_traffic_sign-355.png">Horn sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="NO_ENGINE_BRAKE">
<h3>NO_ENGINE_BRAKE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">NO_ENGINE_BRAKE</span></div>
<div class="block"><p>A sign indicating no engine brake. Example: <a href="https://commons.wikimedia.org/wiki/File:Canada_Avoid_Engine_Brake_Sign.svg">No engine brake sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="END_OF_NO_ENGINE_BRAKE">
<h3>END_OF_NO_ENGINE_BRAKE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">END_OF_NO_ENGINE_BRAKE</span></div>
<div class="block"><p>A sign indicating the end of no engine brake zone. Example: No examples available.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_IDLING">
<h3>NO_IDLING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">NO_IDLING</span></div>
<div class="block"><p>A sign indicating no idling. Example: <a href="https://en.wikipedia.org/wiki/Idle_reduction#/media/File:Idle_free_zone_-_turn_engine_off_sign.jpg">No idling sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TRUCK_ROLLOVER">
<h3>TRUCK_ROLLOVER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TRUCK_ROLLOVER</span></div>
<div class="block"><p>A sign indicating truck rollover. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_States#/media/File:MUTCD_W1-13L.svg">Truck rollover sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="LOW_GEAR">
<h3>LOW_GEAR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">LOW_GEAR</span></div>
<div class="block"><p>A sign indicating the use of low gear. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_Philippines#/media/File:Philippines_road_sign_S1-3.svg">Low gear sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="END_OF_LOW_GEAR">
<h3>END_OF_LOW_GEAR</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">END_OF_LOW_GEAR</span></div>
<div class="block"><p>A sign indicating the use of low gear. Example: No examples available.</p></div>
</section>
</li>
<li>
<section class="detail" id="BICYCLE_CROSSING">
<h3>BICYCLE_CROSSING</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">BICYCLE_CROSSING</span></div>
<div class="block"><p>A sign indicating bicycles crossing. Example: <a href="https://en.wikipedia.org/wiki/File:Australia_road_sign_W6-7-FYG.svg">Bicycle crossing sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="YIELD_TO_BICYCLES">
<h3>YIELD_TO_BICYCLES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">YIELD_TO_BICYCLES</span></div>
<div class="block"><p>A sign indicating yielding to bicycles. Example: <a href="https://en.wikipedia.org/wiki/File:MK_road_sign_302.2.svg">Yield to bicycles sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="NO_TOWED_CARAVAN_ALLOWED">
<h3>NO_TOWED_CARAVAN_ALLOWED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">NO_TOWED_CARAVAN_ALLOWED</span></div>
<div class="block"><p>A sign indicating no towed caravan allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_the_United_Kingdom#/media/File:UK_traffic_sign_622.7.svg">No towed caravan allowed sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="NO_TOWED_TRAILER_ALLOWED">
<h3>NO_TOWED_TRAILER_ALLOWED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">NO_TOWED_TRAILER_ALLOWED</span></div>
<div class="block"><p>A sign indicating no towed trailer allowed. Example: <a href="https://en.wikipedia.org/wiki/Road_signs_in_Sweden#/media/File:Sweden_road_sign_C6.svg">No towed trailer allowed sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="NO_CAMPER_OR_MOTORHOME_ALLOWED">
<h3>NO_CAMPER_OR_MOTORHOME_ALLOWED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">NO_CAMPER_OR_MOTORHOME_ALLOWED</span></div>
<div class="block"><p>A sign indicating no camper or motorhome allowed. Example: No examples available.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_TURN_ON_RED">
<h3>NO_TURN_ON_RED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">NO_TURN_ON_RED</span></div>
<div class="block"><p>A sign indicating no turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:CA-QC_road_sign_P-115-1.svg">No turn on red sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TURN_PERMITTED_ON_RED">
<h3>TURN_PERMITTED_ON_RED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TURN_PERMITTED_ON_RED</span></div>
<div class="block"><p>A sign indicating turning on red permitted. Example: <a href="https://en.wikipedia.org/wiki/Turn_on_red#/media/File:Chile_road_sign_RA-2.svg">Turn permitted on red sign</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TWO_STAGE_LEFT">
<h3>TWO_STAGE_LEFT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TWO_STAGE_LEFT</span></div>
<div class="block"><p>A sign indicating that turning left requires a two-stage maneuver,
 also known as a hook turn or Copenhagen Left, which is a special maneuver to safely
 make a left turn at an intersection without crossing oncoming traffic.
 This maneuver applies only in right-hand driving countries and is particularly beneficial
 for cyclists, as it minimizes interaction with oncoming traffic, allowing for safer crossings. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage left turn</a></p></div>
</section>
</li>
<li>
<section class="detail" id="TWO_STAGE_RIGHT">
<h3>TWO_STAGE_RIGHT</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">TWO_STAGE_RIGHT</span></div>
<div class="block"><p>A sign indicating turning right with the specified vehicle type requires a two stage maneuver.
 A TWO_STAGE_RIGHT maneuver, is a special maneuver commonly used by cyclists to safely
 make a right turn at an intersection without crossing oncoming traffic.
 This maneuver is applicable only in left-hand driving countries and is particularly beneficial
 for cyclists as they allow for safer crossings by minimizing the interaction with oncoming traffic. Example: <a href="https://medium.com/@maharudrabhishekkumar/understanding-two-stage-turns-for-cyclists-safer-crossings-made-simple-navigating-busy-e028f07bcc79">Two stage right turn</a></p></div>
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
<section class="detail" id="values()">
<h3>values</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a>[]</span> <span class="element-name">values</span>()</div>
<div class="block">Returns an array containing the constants of this enum class, in
the order they are declared.</div>
<dl class="notes">
<dt>Returns:</dt>
<dd>an array containing the constants of this enum class, in the order they are declared</dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="valueOf(java.lang.String)">
<h3>valueOf</h3>
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-roadsigntype" title="enum class in com.here.sdk.navigation">RoadSignType</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
<div class="block">Returns the enum constant of this class with the specified name.
The string must match <i>exactly</i> an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)</div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>name</code> - the name of the enum constant to be returned.</dd>
<dt>Returns:</dt>
<dd>the enum constant with the specified name</dd>
<dt>Throws:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" title="class or interface in java.lang">IllegalArgumentException</a></code> - if this enum class has no constant with the specified name</dd>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" title="class or interface in java.lang">NullPointerException</a></code> - if the argument is null</dd>
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
