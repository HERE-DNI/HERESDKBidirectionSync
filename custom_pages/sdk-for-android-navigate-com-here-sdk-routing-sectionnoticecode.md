---
title: "SectionNoticeCode (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- SectionNoticeCode.html -->










<!-- ======== START OF CLASS DATA ======== -->

<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">java.lang.Enum</a>&lt;<a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a>&gt;
<div class="inheritance">com.here.sdk.routing.SectionNoticeCode</div>
</div>
</div>
<section class="class-description" id="class-description">
<dl class="notes">
<dt>All Implemented Interfaces:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" title="class or interface in java.io">Serializable</a></code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" title="class or interface in java.lang">Comparable</a>&lt;<a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a>&gt;</code>, <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" title="class or interface in java.lang.constant">Constable</a></code></dd>
</dl>

<div class="type-signature"><span class="modifiers">public enum </span><span class="element-name type-name-label">SectionNoticeCode</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" title="class or interface in java.lang">Enum</a>&lt;<a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a>&gt;</span></div>
<div class="block"><p>Notice codes which point the issues encountered during processing of a <a href="sdk-for-android-navigate-section" title="class in com.here.sdk.routing"><code>Section</code></a>.
 <strong>Note:</strong> The section notice codes are going to be extended for new error situations.</p></div>
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
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#CHARGING_STOP_NOT_NEEDED">CHARGING_STOP_NOT_NEEDED</a></code></div>
<div class="col-last even-row-color">
<div class="block">A charging stop was planned at the destination of this section, but it is no longer
 needed.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#NO_INTERMEDIATE">NO_INTERMEDIATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Information about intermediate stops is not available for a transit section.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#NO_SCHEDULE">NO_SCHEDULE</a></code></div>
<div class="col-last even-row-color">
<div class="block">No schedule information is available for a transit section.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#NO_THROUGH_RESTRICTION">NO_THROUGH_RESTRICTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route goes through a road that does not allow through traffic.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#POTENTIAL_CARPOOL">POTENTIAL_CARPOOL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#POTENTIAL_TURN_RESTRICTION">POTENTIAL_TURN_RESTRICTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#POTENTIAL_VEHICLE_RESTRICTION">POTENTIAL_VEHICLE_RESTRICTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#POTENTIAL_ZONE_RESTRICTION">POTENTIAL_ZONE_RESTRICTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#SCHEDULED_TIMES">SCHEDULED_TIMES</a></code></div>
<div class="col-last even-row-color">
<div class="block">This transit section returned times which are scheduled times, even though delay information is available.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#SEASONAL_CLOSURE">SEASONAL_CLOSURE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route goes through seasonal closure.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#SIMPLE_POLYLINE">SIMPLE_POLYLINE</a></code></div>
<div class="col-last even-row-color">
<div class="block">An accurate polyline is not available for this section.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#TOLL_TRANSPONDER">TOLL_TRANSPONDER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route goes through toll booth that requires transponder.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#TOLLS_DATA_TEMPORARILY_UNAVAILABLE">TOLLS_DATA_TEMPORARILY_UNAVAILABLE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Tolls data was requested but is temporarily unavailable.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#TOLLS_DATA_UNAVAILABLE">TOLLS_DATA_UNAVAILABLE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Tolls data was requested but could not be calculated for this section.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#UNWANTED_MODE">UNWANTED_MODE</a></code></div>
<div class="col-last even-row-color">
<div class="block">This transit section contains a transport mode that was explictly disabled.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY">VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_DIFFICULT_TURNS">VIOLATED_AVOID_DIFFICULT_TURNS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid difficult turns.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_DIRT_ROAD">VIOLATED_AVOID_DIRT_ROAD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_FERRY">VIOLATED_AVOID_FERRY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_PARK">VIOLATED_AVOID_PARK</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_RAIL_FERRY">VIOLATED_AVOID_RAIL_FERRY</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_SEASONAL_CLOSURE">VIOLATED_AVOID_SEASONAL_CLOSURE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route did not manage to avoid seasonal closure.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TOLL_ROAD">VIOLATED_AVOID_TOLL_ROAD</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TOLL_TRANSPONDER">VIOLATED_AVOID_TOLL_TRANSPONDER</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route did not manage to avoid toll booth that requires transponder.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TRUCK_ROAD_TYPE">VIOLATED_AVOID_TRUCK_ROAD_TYPE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid restricted truck road types.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TUNNEL">VIOLATED_AVOID_TUNNEL</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_U_TURNS">VIOLATED_AVOID_U_TURNS</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid u turns.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_BLOCKED_ROAD">VIOLATED_BLOCKED_ROAD</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route uses roads blocked by traffic events or
 route did not manage to avoid the requested
 <code>avoidBoundingBoxAreas</code> or <code>countries</code> or <code>segments</code>.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_CARPOOL">VIOLATED_CARPOOL</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route did not manage to avoid user preference.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_CHARGING_STATION_OPENING_HOURS">VIOLATED_CHARGING_STATION_OPENING_HOURS</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Charging at the charging station planned at the destination of this section falls outside of opening hours.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_CRITICAL_RULE">VIOLATED_CRITICAL_RULE</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route has violoated a non-detailed critical rule.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_EMERGENCY_GATE">VIOLATED_EMERGENCY_GATE</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route goes through an emergency gate.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_MIN_CHARGE_AT_CS">VIOLATED_MIN_CHARGE_AT_CS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_MIN_CHARGE_AT_DESTINATION">VIOLATED_MIN_CHARGE_AT_DESTINATION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_MIN_CHARGE_AT_FIRST_CS">VIOLATED_MIN_CHARGE_AT_FIRST_CS</a></code></div>
<div class="col-last even-row-color">
<div class="block">The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_START_DIRECTION">VIOLATED_START_DIRECTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Start direction of the route is not as requested.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_TURN_RESTRICTION">VIOLATED_TURN_RESTRICTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route uses a time-restricted turn.</div>
</div>
<div class="col-first odd-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_VEHICLE_RESTRICTION">VIOLATED_VEHICLE_RESTRICTION</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Route uses a road which is forbidden for the given vehicle profile.</div>
</div>
<div class="col-first even-row-color"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#VIOLATED_ZONE_RESTRICTION">VIOLATED_ZONE_RESTRICTION</a></code></div>
<div class="col-last even-row-color">
<div class="block">Route uses a road which is part of restricted <code>zoneCategories</code>
 requested to be avoided by user.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab1" onclick="show('method-summary-table', 'method-summary-table-tab1', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Static Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#valueOf(java.lang.String)">valueOf</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">
<div class="block">Returns the enum constant of this class with the specified name.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code>static <a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a>[]</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-navigate-com-here-sdk-routing-sectionnoticecode#values()">values</a>()</code></div>
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
<section class="detail" id="VIOLATED_CRITICAL_RULE">
<h3>VIOLATED_CRITICAL_RULE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_CRITICAL_RULE</span></div>
<div class="block"><p>Route has violoated a non-detailed critical rule.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY">
<h3>VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_TOLL_ROAD">
<h3>VIOLATED_AVOID_TOLL_ROAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_TOLL_ROAD</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_FERRY">
<h3>VIOLATED_AVOID_FERRY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_FERRY</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_TUNNEL">
<h3>VIOLATED_AVOID_TUNNEL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_TUNNEL</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_DIRT_ROAD">
<h3>VIOLATED_AVOID_DIRT_ROAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_DIRT_ROAD</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_RAIL_FERRY">
<h3>VIOLATED_AVOID_RAIL_FERRY</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_RAIL_FERRY</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_PARK">
<h3>VIOLATED_AVOID_PARK</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_PARK</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_BLOCKED_ROAD">
<h3>VIOLATED_BLOCKED_ROAD</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_BLOCKED_ROAD</span></div>
<div class="block"><p>Route uses roads blocked by traffic events or
 route did not manage to avoid the requested
 <code>avoidBoundingBoxAreas</code> or <code>countries</code> or <code>segments</code>.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_START_DIRECTION">
<h3>VIOLATED_START_DIRECTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_START_DIRECTION</span></div>
<div class="block"><p>Start direction of the route is not as requested.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_CARPOOL">
<h3>VIOLATED_CARPOOL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_CARPOOL</span></div>
<div class="block"><p>Route did not manage to avoid user preference.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_TURN_RESTRICTION">
<h3>VIOLATED_TURN_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_TURN_RESTRICTION</span></div>
<div class="block"><p>Route uses a time-restricted turn.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_VEHICLE_RESTRICTION">
<h3>VIOLATED_VEHICLE_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_VEHICLE_RESTRICTION</span></div>
<div class="block"><p>Route uses a road which is forbidden for the given vehicle profile.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_ZONE_RESTRICTION">
<h3>VIOLATED_ZONE_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_ZONE_RESTRICTION</span></div>
<div class="block"><p>Route uses a road which is part of restricted <code>zoneCategories</code>
 requested to be avoided by user.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_U_TURNS">
<h3>VIOLATED_AVOID_U_TURNS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_U_TURNS</span></div>
<div class="block"><p>Route did not manage to avoid u turns.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_EMERGENCY_GATE">
<h3>VIOLATED_EMERGENCY_GATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_EMERGENCY_GATE</span></div>
<div class="block"><p>Route goes through an emergency gate.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_SEASONAL_CLOSURE">
<h3>VIOLATED_AVOID_SEASONAL_CLOSURE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_SEASONAL_CLOSURE</span></div>
<div class="block"><p>Route did not manage to avoid seasonal closure.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_TRUCK_ROAD_TYPE">
<h3>VIOLATED_AVOID_TRUCK_ROAD_TYPE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_TRUCK_ROAD_TYPE</span></div>
<div class="block"><p>Route did not manage to avoid restricted truck road types.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_TOLL_TRANSPONDER">
<h3>VIOLATED_AVOID_TOLL_TRANSPONDER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_TOLL_TRANSPONDER</span></div>
<div class="block"><p>Route did not manage to avoid toll booth that requires transponder.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_CHARGING_STATION_OPENING_HOURS">
<h3>VIOLATED_CHARGING_STATION_OPENING_HOURS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_CHARGING_STATION_OPENING_HOURS</span></div>
<div class="block"><p>Charging at the charging station planned at the destination of this section falls outside of opening hours.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_AVOID_DIFFICULT_TURNS">
<h3>VIOLATED_AVOID_DIFFICULT_TURNS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_AVOID_DIFFICULT_TURNS</span></div>
<div class="block"><p>Route did not manage to avoid difficult turns.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#CRITICAL"><code>NoticeSeverity.CRITICAL</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="SEASONAL_CLOSURE">
<h3>SEASONAL_CLOSURE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">SEASONAL_CLOSURE</span></div>
<div class="block"><p>Route goes through seasonal closure.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="TOLL_TRANSPONDER">
<h3>TOLL_TRANSPONDER</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">TOLL_TRANSPONDER</span></div>
<div class="block"><p>Route goes through toll booth that requires transponder.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="TOLLS_DATA_UNAVAILABLE">
<h3>TOLLS_DATA_UNAVAILABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">TOLLS_DATA_UNAVAILABLE</span></div>
<div class="block"><p>Tolls data was requested but could not be calculated for this section.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="TOLLS_DATA_TEMPORARILY_UNAVAILABLE">
<h3>TOLLS_DATA_TEMPORARILY_UNAVAILABLE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">TOLLS_DATA_TEMPORARILY_UNAVAILABLE</span></div>
<div class="block"><p>Tolls data was requested but is temporarily unavailable.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="CHARGING_STOP_NOT_NEEDED">
<h3>CHARGING_STOP_NOT_NEEDED</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">CHARGING_STOP_NOT_NEEDED</span></div>
<div class="block"><p>A charging stop was planned at the destination of this section, but it is no longer
 needed. It may be issued only when refreshing a route via <a href="sdk-for-android-navigate-routehandle" title="class in com.here.sdk.routing"><code>RouteHandle</code></a>.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_SCHEDULE">
<h3>NO_SCHEDULE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">NO_SCHEDULE</span></div>
<div class="block"><p>No schedule information is available for a transit section. As a result, departure/arrival times are approximated.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_INTERMEDIATE">
<h3>NO_INTERMEDIATE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">NO_INTERMEDIATE</span></div>
<div class="block"><p>Information about intermediate stops is not available for a transit section.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="UNWANTED_MODE">
<h3>UNWANTED_MODE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">UNWANTED_MODE</span></div>
<div class="block"><p>This transit section contains a transport mode that was explictly disabled.
 Mode filtering is not available in this area.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="SCHEDULED_TIMES">
<h3>SCHEDULED_TIMES</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">SCHEDULED_TIMES</span></div>
<div class="block"><p>This transit section returned times which are scheduled times, even though delay information is available.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="SIMPLE_POLYLINE">
<h3>SIMPLE_POLYLINE</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">SIMPLE_POLYLINE</span></div>
<div class="block"><p>An accurate polyline is not available for this section. An accurate polyline is not available for this
 section. The returned polyline has been generated from departure and arrival places.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="POTENTIAL_CARPOOL">
<h3>POTENTIAL_CARPOOL</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">POTENTIAL_CARPOOL</span></div>
<div class="block"><p>Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="POTENTIAL_TURN_RESTRICTION">
<h3>POTENTIAL_TURN_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">POTENTIAL_TURN_RESTRICTION</span></div>
<div class="block"><p>Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="POTENTIAL_VEHICLE_RESTRICTION">
<h3>POTENTIAL_VEHICLE_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">POTENTIAL_VEHICLE_RESTRICTION</span></div>
<div class="block"><p>Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="POTENTIAL_ZONE_RESTRICTION">
<h3>POTENTIAL_ZONE_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">POTENTIAL_ZONE_RESTRICTION</span></div>
<div class="block"><p>Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours.
 Severity: <a href="sdk-for-android-navigate-noticeseverity#INFO"><code>NoticeSeverity.INFO</code></a>.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_MIN_CHARGE_AT_FIRST_CS">
<h3>VIOLATED_MIN_CHARGE_AT_FIRST_CS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_MIN_CHARGE_AT_FIRST_CS</span></div>
<div class="block"><p>The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_MIN_CHARGE_AT_CS">
<h3>VIOLATED_MIN_CHARGE_AT_CS</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_MIN_CHARGE_AT_CS</span></div>
<div class="block"><p>The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.</p></div>
</section>
</li>
<li>
<section class="detail" id="VIOLATED_MIN_CHARGE_AT_DESTINATION">
<h3>VIOLATED_MIN_CHARGE_AT_DESTINATION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">VIOLATED_MIN_CHARGE_AT_DESTINATION</span></div>
<div class="block"><p>The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.</p></div>
</section>
</li>
<li>
<section class="detail" id="NO_THROUGH_RESTRICTION">
<h3>NO_THROUGH_RESTRICTION</h3>
<div class="member-signature"><span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">NO_THROUGH_RESTRICTION</span></div>
<div class="block"><p>Route goes through a road that does not allow through traffic.</p></div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a>[]</span> <span class="element-name">values</span>()</div>
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
<div class="member-signature"><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-sectionnoticecode" title="enum class in com.here.sdk.routing">SectionNoticeCode</a></span> <span class="element-name">valueOf</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a> name)</span></div>
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






</div>
`
}</HTMLBlock>
