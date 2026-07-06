---
title: "SectionNoticeCode (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum\<SectionNoticeCode\>com.here.sdk.routing.SectionNoticeCode
→ java.lang.Enum → SectionNoticeCode →
com.here.sdk.routing.SectionNoticeCode

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`SectionNoticeCode`](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum
</span><span class="element-name type-name-label">SectionNoticeCode</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a>\<[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")\></span>

</div>

<div class="block">

Notice codes which point the issues encountered during processing of a
Section . Note: The section notice codes are going to be extended for
new error situations.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-explore-enum-constant-summary"
  class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#CHARGING_STOP_NOT_NEEDED"
  class="member-name-link"><code>CHARGING_STOP_NOT_NEEDED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A charging stop was planned at the destination of this section, but it
  is no longer needed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#NO_INTERMEDIATE"
  class="member-name-link"><code>NO_INTERMEDIATE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Information about intermediate stops is not available for a transit
  section.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#NO_SCHEDULE"
  class="member-name-link"><code>NO_SCHEDULE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  No schedule information is available for a transit section.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#NO_THROUGH_RESTRICTION"
  class="member-name-link"><code>NO_THROUGH_RESTRICTION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route goes through a road that does not allow through traffic.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#POTENTIAL_CARPOOL"
  class="member-name-link"><code>POTENTIAL_CARPOOL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route utilizes a designated carpool lane, potentially subject to
  restrictions beyond the scheduled travel hours.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#POTENTIAL_TURN_RESTRICTION"
  class="member-name-link"><code>POTENTIAL_TURN_RESTRICTION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route includes a turn that is potentially restricted and inaccessible
  beyond the scheduled travel hours.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#POTENTIAL_VEHICLE_RESTRICTION"
  class="member-name-link"><code>POTENTIAL_VEHICLE_RESTRICTION</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route utilizes roads that are potentially off-limits to the specified
  vehicle profile beyond the scheduled travel hours.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#POTENTIAL_ZONE_RESTRICTION"
  class="member-name-link"><code>POTENTIAL_ZONE_RESTRICTION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route incorporates roads within zones, which are potentially not
  accessible beyond the scheduled travel hours.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#SCHEDULED_TIMES"
  class="member-name-link"><code>SCHEDULED_TIMES</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This transit section returned times which are scheduled times, even
  though delay information is available.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#SEASONAL_CLOSURE"
  class="member-name-link"><code>SEASONAL_CLOSURE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route goes through seasonal closure.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#SIMPLE_POLYLINE"
  class="member-name-link"><code>SIMPLE_POLYLINE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  An accurate polyline is not available for this section.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#TOLL_TRANSPONDER"
  class="member-name-link"><code>TOLL_TRANSPONDER</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route goes through toll booth that requires transponder.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#TOLLS_DATA_TEMPORARILY_UNAVAILABLE"
  class="member-name-link"><code>TOLLS_DATA_TEMPORARILY_UNAVAILABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Tolls data was requested but is temporarily unavailable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#TOLLS_DATA_UNAVAILABLE"
  class="member-name-link"><code>TOLLS_DATA_UNAVAILABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Tolls data was requested but could not be calculated for this section.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#UNWANTED_MODE"
  class="member-name-link"><code>UNWANTED_MODE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  This transit section contains a transport mode that was explictly
  disabled.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY"
  class="member-name-link"><code>VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_DIFFICULT_TURNS"
  class="member-name-link"><code>VIOLATED_AVOID_DIFFICULT_TURNS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid difficult turns.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_DIRT_ROAD"
  class="member-name-link"><code>VIOLATED_AVOID_DIRT_ROAD</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_FERRY"
  class="member-name-link"><code>VIOLATED_AVOID_FERRY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_PARK"
  class="member-name-link"><code>VIOLATED_AVOID_PARK</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_RAIL_FERRY"
  class="member-name-link"><code>VIOLATED_AVOID_RAIL_FERRY</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_SEASONAL_CLOSURE"
  class="member-name-link"><code>VIOLATED_AVOID_SEASONAL_CLOSURE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route did not manage to avoid seasonal closure.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TOLL_ROAD"
  class="member-name-link"><code>VIOLATED_AVOID_TOLL_ROAD</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TOLL_TRANSPONDER"
  class="member-name-link"><code>VIOLATED_AVOID_TOLL_TRANSPONDER</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route did not manage to avoid toll booth that requires transponder.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TRUCK_ROAD_TYPE"
  class="member-name-link"><code>VIOLATED_AVOID_TRUCK_ROAD_TYPE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid restricted truck road types.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_TUNNEL"
  class="member-name-link"><code>VIOLATED_AVOID_TUNNEL</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_AVOID_U_TURNS"
  class="member-name-link"><code>VIOLATED_AVOID_U_TURNS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid u turns.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_BLOCKED_ROAD"
  class="member-name-link"><code>VIOLATED_BLOCKED_ROAD</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route uses roads blocked by traffic events or route did not manage to
  avoid the requested avoidBoundingBoxAreas or countries or segments .

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_CARPOOL"
  class="member-name-link"><code>VIOLATED_CARPOOL</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route did not manage to avoid user preference.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_CHARGING_STATION_OPENING_HOURS"
  class="member-name-link"><code>VIOLATED_CHARGING_STATION_OPENING_HOURS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Charging at the charging station planned at the destination of this
  section falls outside of opening hours.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_CRITICAL_RULE"
  class="member-name-link"><code>VIOLATED_CRITICAL_RULE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route has violoated a non-detailed critical rule.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_EMERGENCY_GATE"
  class="member-name-link"><code>VIOLATED_EMERGENCY_GATE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route goes through an emergency gate.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_MIN_CHARGE_AT_CS"
  class="member-name-link"><code>VIOLATED_MIN_CHARGE_AT_CS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The route can not reach all charging stations on the route with the
  minimum required charge, as the initial charge was to low.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_MIN_CHARGE_AT_DESTINATION"
  class="member-name-link"><code>VIOLATED_MIN_CHARGE_AT_DESTINATION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The route can not reach the waypoint, as the there are not enough
  charging stops available or the initial charge was to low.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_MIN_CHARGE_AT_FIRST_CS"
  class="member-name-link"><code>VIOLATED_MIN_CHARGE_AT_FIRST_CS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The route can not reach the first charging station with the minimum
  required charge, as the initial charge was to low.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_START_DIRECTION"
  class="member-name-link"><code>VIOLATED_START_DIRECTION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Start direction of the route is not as requested.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_TURN_RESTRICTION"
  class="member-name-link"><code>VIOLATED_TURN_RESTRICTION</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route uses a time-restricted turn.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_VEHICLE_RESTRICTION"
  class="member-name-link"><code>VIOLATED_VEHICLE_RESTRICTION</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Route uses a road which is forbidden for the given vehicle profile.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode#VIOLATED_ZONE_RESTRICTION"
  class="member-name-link"><code>VIOLATED_ZONE_RESTRICTION</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Route uses a road which is part of restricted zoneCategories requested
  to be avoided by user.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`SectionNoticeCode`](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf(String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `[`SectionNoticeCode`](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the
  order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-enum-constant-detail"
  class="section constant-details">

  - <div id="sdk-for-android-explore-VIOLATED_CRITICAL_RULE"
    class="section detail">

    ### VIOLATED_CRITICAL_RULE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_CRITICAL_RULE</span>

    </div>

    <div class="block">

    Route has violoated a non-detailed critical rule. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY"
    class="section detail">

    ### VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_TOLL_ROAD"
    class="section detail">

    ### VIOLATED_AVOID_TOLL_ROAD

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_TOLL_ROAD</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_FERRY"
    class="section detail">

    ### VIOLATED_AVOID_FERRY

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_FERRY</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_TUNNEL"
    class="section detail">

    ### VIOLATED_AVOID_TUNNEL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_TUNNEL</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_DIRT_ROAD"
    class="section detail">

    ### VIOLATED_AVOID_DIRT_ROAD

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_DIRT_ROAD</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_RAIL_FERRY"
    class="section detail">

    ### VIOLATED_AVOID_RAIL_FERRY

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_RAIL_FERRY</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_PARK"
    class="section detail">

    ### VIOLATED_AVOID_PARK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_PARK</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_BLOCKED_ROAD"
    class="section detail">

    ### VIOLATED_BLOCKED_ROAD

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_BLOCKED_ROAD</span>

    </div>

    <div class="block">

    Route uses roads blocked by traffic events or route did not manage
    to avoid the requested avoidBoundingBoxAreas or countries or
    segments . Severity: NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_START_DIRECTION"
    class="section detail">

    ### VIOLATED_START_DIRECTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_START_DIRECTION</span>

    </div>

    <div class="block">

    Start direction of the route is not as requested. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_CARPOOL"
    class="section detail">

    ### VIOLATED_CARPOOL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_CARPOOL</span>

    </div>

    <div class="block">

    Route did not manage to avoid user preference. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_TURN_RESTRICTION"
    class="section detail">

    ### VIOLATED_TURN_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_TURN_RESTRICTION</span>

    </div>

    <div class="block">

    Route uses a time-restricted turn. Severity: NoticeSeverity.CRITICAL
    .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_VEHICLE_RESTRICTION"
    class="section detail">

    ### VIOLATED_VEHICLE_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_VEHICLE_RESTRICTION</span>

    </div>

    <div class="block">

    Route uses a road which is forbidden for the given vehicle profile.
    Severity: NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_ZONE_RESTRICTION"
    class="section detail">

    ### VIOLATED_ZONE_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_ZONE_RESTRICTION</span>

    </div>

    <div class="block">

    Route uses a road which is part of restricted zoneCategories
    requested to be avoided by user. Severity: NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_U_TURNS"
    class="section detail">

    ### VIOLATED_AVOID_U_TURNS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_U_TURNS</span>

    </div>

    <div class="block">

    Route did not manage to avoid u turns. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_EMERGENCY_GATE"
    class="section detail">

    ### VIOLATED_EMERGENCY_GATE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_EMERGENCY_GATE</span>

    </div>

    <div class="block">

    Route goes through an emergency gate. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_SEASONAL_CLOSURE"
    class="section detail">

    ### VIOLATED_AVOID_SEASONAL_CLOSURE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_SEASONAL_CLOSURE</span>

    </div>

    <div class="block">

    Route did not manage to avoid seasonal closure. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_TRUCK_ROAD_TYPE"
    class="section detail">

    ### VIOLATED_AVOID_TRUCK_ROAD_TYPE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_TRUCK_ROAD_TYPE</span>

    </div>

    <div class="block">

    Route did not manage to avoid restricted truck road types.

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_TOLL_TRANSPONDER"
    class="section detail">

    ### VIOLATED_AVOID_TOLL_TRANSPONDER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_TOLL_TRANSPONDER</span>

    </div>

    <div class="block">

    Route did not manage to avoid toll booth that requires transponder.
    Severity: NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_CHARGING_STATION_OPENING_HOURS"
    class="section detail">

    ### VIOLATED_CHARGING_STATION_OPENING_HOURS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_CHARGING_STATION_OPENING_HOURS</span>

    </div>

    <div class="block">

    Charging at the charging station planned at the destination of this
    section falls outside of opening hours. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_AVOID_DIFFICULT_TURNS"
    class="section detail">

    ### VIOLATED_AVOID_DIFFICULT_TURNS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_AVOID_DIFFICULT_TURNS</span>

    </div>

    <div class="block">

    Route did not manage to avoid difficult turns. Severity:
    NoticeSeverity.CRITICAL .

    </div>

    </div>

  - <div id="sdk-for-android-explore-SEASONAL_CLOSURE"
    class="section detail">

    ### SEASONAL_CLOSURE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">SEASONAL_CLOSURE</span>

    </div>

    <div class="block">

    Route goes through seasonal closure. Severity: NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-TOLL_TRANSPONDER"
    class="section detail">

    ### TOLL_TRANSPONDER

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">TOLL_TRANSPONDER</span>

    </div>

    <div class="block">

    Route goes through toll booth that requires transponder. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-TOLLS_DATA_UNAVAILABLE"
    class="section detail">

    ### TOLLS_DATA_UNAVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">TOLLS_DATA_UNAVAILABLE</span>

    </div>

    <div class="block">

    Tolls data was requested but could not be calculated for this
    section. Severity: NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-TOLLS_DATA_TEMPORARILY_UNAVAILABLE"
    class="section detail">

    ### TOLLS_DATA_TEMPORARILY_UNAVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">TOLLS_DATA_TEMPORARILY_UNAVAILABLE</span>

    </div>

    <div class="block">

    Tolls data was requested but is temporarily unavailable. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-CHARGING_STOP_NOT_NEEDED"
    class="section detail">

    ### CHARGING_STOP_NOT_NEEDED

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">CHARGING_STOP_NOT_NEEDED</span>

    </div>

    <div class="block">

    A charging stop was planned at the destination of this section, but
    it is no longer needed. It may be issued only when refreshing a
    route via RouteHandle . Severity: NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_SCHEDULE"
    class="section detail">

    ### NO_SCHEDULE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_SCHEDULE</span>

    </div>

    <div class="block">

    No schedule information is available for a transit section. As a
    result, departure/arrival times are approximated. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_INTERMEDIATE"
    class="section detail">

    ### NO_INTERMEDIATE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_INTERMEDIATE</span>

    </div>

    <div class="block">

    Information about intermediate stops is not available for a transit
    section. Severity: NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-UNWANTED_MODE"
    class="section detail">

    ### UNWANTED_MODE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">UNWANTED_MODE</span>

    </div>

    <div class="block">

    This transit section contains a transport mode that was explictly
    disabled. Mode filtering is not available in this area. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-SCHEDULED_TIMES"
    class="section detail">

    ### SCHEDULED_TIMES

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">SCHEDULED_TIMES</span>

    </div>

    <div class="block">

    This transit section returned times which are scheduled times, even
    though delay information is available. Severity: NoticeSeverity.INFO
    .

    </div>

    </div>

  - <div id="sdk-for-android-explore-SIMPLE_POLYLINE"
    class="section detail">

    ### SIMPLE_POLYLINE

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">SIMPLE_POLYLINE</span>

    </div>

    <div class="block">

    An accurate polyline is not available for this section. An accurate
    polyline is not available for this section. The returned polyline
    has been generated from departure and arrival places. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-POTENTIAL_CARPOOL"
    class="section detail">

    ### POTENTIAL_CARPOOL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">POTENTIAL_CARPOOL</span>

    </div>

    <div class="block">

    Route utilizes a designated carpool lane, potentially subject to
    restrictions beyond the scheduled travel hours. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-POTENTIAL_TURN_RESTRICTION"
    class="section detail">

    ### POTENTIAL_TURN_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">POTENTIAL_TURN_RESTRICTION</span>

    </div>

    <div class="block">

    Route includes a turn that is potentially restricted and
    inaccessible beyond the scheduled travel hours. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-POTENTIAL_VEHICLE_RESTRICTION"
    class="section detail">

    ### POTENTIAL_VEHICLE_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">POTENTIAL_VEHICLE_RESTRICTION</span>

    </div>

    <div class="block">

    Route utilizes roads that are potentially off-limits to the
    specified vehicle profile beyond the scheduled travel hours.
    Severity: NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-POTENTIAL_ZONE_RESTRICTION"
    class="section detail">

    ### POTENTIAL_ZONE_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">POTENTIAL_ZONE_RESTRICTION</span>

    </div>

    <div class="block">

    Route incorporates roads within zones, which are potentially not
    accessible beyond the scheduled travel hours. Severity:
    NoticeSeverity.INFO .

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_MIN_CHARGE_AT_FIRST_CS"
    class="section detail">

    ### VIOLATED_MIN_CHARGE_AT_FIRST_CS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_MIN_CHARGE_AT_FIRST_CS</span>

    </div>

    <div class="block">

    The route can not reach the first charging station with the minimum
    required charge, as the initial charge was to low.

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_MIN_CHARGE_AT_CS"
    class="section detail">

    ### VIOLATED_MIN_CHARGE_AT_CS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_MIN_CHARGE_AT_CS</span>

    </div>

    <div class="block">

    The route can not reach all charging stations on the route with the
    minimum required charge, as the initial charge was to low.

    </div>

    </div>

  - <div id="sdk-for-android-explore-VIOLATED_MIN_CHARGE_AT_DESTINATION"
    class="section detail">

    ### VIOLATED_MIN_CHARGE_AT_DESTINATION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">VIOLATED_MIN_CHARGE_AT_DESTINATION</span>

    </div>

    <div class="block">

    The route can not reach the waypoint, as the there are not enough
    charging stops available or the initial charge was to low.

    </div>

    </div>

  - <div id="sdk-for-android-explore-NO_THROUGH_RESTRICTION"
    class="section detail">

    ### NO_THROUGH_RESTRICTION

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">NO_THROUGH_RESTRICTION</span>

    </div>

    <div class="block">

    Route goes through a road that does not allow through traffic.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="sdk-for-android-explore-valueOf(java.lang.String)"
    class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[SectionNoticeCode](sdk-for-android-explore-com-here-sdk-routing-sectionnoticecode "enum class in com.here.sdk.routing")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

</div>

