---
title: "SectionNoticeCode (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsectionnoticecode"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Enum Class SectionNoticeCode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")\>
com.here.sdk.routing.SectionNoticeCode
All Implemented Interfaces:
[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html)`<`[`SectionNoticeCode`](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")`>`, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html)

------------------------------------------------------------------------
public enum SectionNoticeCode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)\<[SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")\>
Notice codes which point the issues encountered during processing of a [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing").

**Note:** The section notice codes are going to be extended for new error situations.

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)` extends `[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)`<`[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html)`>>`

## Enum Constant Summary

Enum Constants

Enum Constant

  Description

  [CHARGING_STOP_NOT_NEEDED](#CHARGING_STOP_NOT_NEEDED)

A charging stop was planned at the destination of this section, but it is no longer needed.

[NO_INTERMEDIATE](#NO_INTERMEDIATE)

Information about intermediate stops is not available for a transit section.

[NO_SCHEDULE](#NO_SCHEDULE)

No schedule information is available for a transit section.

[NO_THROUGH_RESTRICTION](#NO_THROUGH_RESTRICTION)

Route goes through a road that does not allow through traffic.

[POTENTIAL_CARPOOL](#POTENTIAL_CARPOOL)

Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours.

[POTENTIAL_TURN_RESTRICTION](#POTENTIAL_TURN_RESTRICTION)

Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours.

[POTENTIAL_VEHICLE_RESTRICTION](#POTENTIAL_VEHICLE_RESTRICTION)

Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours.

[POTENTIAL_ZONE_RESTRICTION](#POTENTIAL_ZONE_RESTRICTION)

Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours.

[SCHEDULED_TIMES](#SCHEDULED_TIMES)

This transit section returned times which are scheduled times, even though delay information is available.

[SEASONAL_CLOSURE](#SEASONAL_CLOSURE)

Route goes through seasonal closure.

[SIMPLE_POLYLINE](#SIMPLE_POLYLINE)

An accurate polyline is not available for this section.

[TOLL_TRANSPONDER](#TOLL_TRANSPONDER)

Route goes through toll booth that requires transponder.

[TOLLS_DATA_TEMPORARILY_UNAVAILABLE](#TOLLS_DATA_TEMPORARILY_UNAVAILABLE)

Tolls data was requested but is temporarily unavailable.

[TOLLS_DATA_UNAVAILABLE](#TOLLS_DATA_UNAVAILABLE)

Tolls data was requested but could not be calculated for this section.

[UNWANTED_MODE](#UNWANTED_MODE)

This transit section contains a transport mode that was explictly disabled.

[VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY](#VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_DIFFICULT_TURNS](#VIOLATED_AVOID_DIFFICULT_TURNS)

Route did not manage to avoid difficult turns.

[VIOLATED_AVOID_DIRT_ROAD](#VIOLATED_AVOID_DIRT_ROAD)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_FERRY](#VIOLATED_AVOID_FERRY)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_PARK](#VIOLATED_AVOID_PARK)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_RAIL_FERRY](#VIOLATED_AVOID_RAIL_FERRY)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_SEASONAL_CLOSURE](#VIOLATED_AVOID_SEASONAL_CLOSURE)

Route did not manage to avoid seasonal closure.

[VIOLATED_AVOID_TOLL_ROAD](#VIOLATED_AVOID_TOLL_ROAD)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_TOLL_TRANSPONDER](#VIOLATED_AVOID_TOLL_TRANSPONDER)

Route did not manage to avoid toll booth that requires transponder.

[VIOLATED_AVOID_TRUCK_ROAD_TYPE](#VIOLATED_AVOID_TRUCK_ROAD_TYPE)

Route did not manage to avoid restricted truck road types.

[VIOLATED_AVOID_TUNNEL](#VIOLATED_AVOID_TUNNEL)

Route did not manage to avoid user preference.

[VIOLATED_AVOID_U_TURNS](#VIOLATED_AVOID_U_TURNS)

Route did not manage to avoid u turns.

[VIOLATED_BLOCKED_ROAD](#VIOLATED_BLOCKED_ROAD)

Route uses roads blocked by traffic events or route did not manage to avoid the requested `avoidBoundingBoxAreas` or `countries` or `segments`.

[VIOLATED_CARPOOL](#VIOLATED_CARPOOL)

Route did not manage to avoid user preference.

[VIOLATED_CHARGING_STATION_OPENING_HOURS](#VIOLATED_CHARGING_STATION_OPENING_HOURS)

Charging at the charging station planned at the destination of this section falls outside of opening hours.

[VIOLATED_CRITICAL_RULE](#VIOLATED_CRITICAL_RULE)

Route has violoated a non-detailed critical rule.

[VIOLATED_EMERGENCY_GATE](#VIOLATED_EMERGENCY_GATE)

Route goes through an emergency gate.

[VIOLATED_MIN_CHARGE_AT_CS](#VIOLATED_MIN_CHARGE_AT_CS)

The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.

[VIOLATED_MIN_CHARGE_AT_DESTINATION](#VIOLATED_MIN_CHARGE_AT_DESTINATION)

The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.

[VIOLATED_MIN_CHARGE_AT_FIRST_CS](#VIOLATED_MIN_CHARGE_AT_FIRST_CS)

The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.

[VIOLATED_START_DIRECTION](#VIOLATED_START_DIRECTION)

Start direction of the route is not as requested.

[VIOLATED_TURN_RESTRICTION](#VIOLATED_TURN_RESTRICTION)

Route uses a time-restricted turn.

[VIOLATED_VEHICLE_RESTRICTION](#VIOLATED_VEHICLE_RESTRICTION)

Route uses a road which is forbidden for the given vehicle profile.

[VIOLATED_ZONE_RESTRICTION](#VIOLATED_ZONE_RESTRICTION)

Route uses a road which is part of restricted `zoneCategories` requested to be avoided by user.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`SectionNoticeCode`](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")

  [valueOf](#valueOf(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Returns the enum constant of this class with the specified name.

`static `[`SectionNoticeCode`](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")`[]`

  [values](#values())`()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String))

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Enum Constant Details

### VIOLATED_CRITICAL_RULE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_CRITICAL_RULE

    Route has violoated a non-detailed critical rule. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_CONTROLLED_ACCESS_HIGHWAY

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_TOLL_ROAD

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_TOLL_ROAD

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_FERRY

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_FERRY

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_TUNNEL

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_TUNNEL

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_DIRT_ROAD

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_DIRT_ROAD

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_RAIL_FERRY

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_RAIL_FERRY

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_PARK

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_PARK

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_BLOCKED_ROAD

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_BLOCKED_ROAD

    Route uses roads blocked by traffic events or route did not manage to avoid the requested `avoidBoundingBoxAreas` or `countries` or `segments`. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_START_DIRECTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_START_DIRECTION

    Start direction of the route is not as requested. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_CARPOOL

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_CARPOOL

    Route did not manage to avoid user preference. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_TURN_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_TURN_RESTRICTION

    Route uses a time-restricted turn. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_VEHICLE_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_VEHICLE_RESTRICTION

    Route uses a road which is forbidden for the given vehicle profile. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_ZONE_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_ZONE_RESTRICTION

    Route uses a road which is part of restricted `zoneCategories` requested to be avoided by user. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_U_TURNS

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_U_TURNS

    Route did not manage to avoid u turns. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_EMERGENCY_GATE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_EMERGENCY_GATE

    Route goes through an emergency gate. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_SEASONAL_CLOSURE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_SEASONAL_CLOSURE

    Route did not manage to avoid seasonal closure. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_TRUCK_ROAD_TYPE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_TRUCK_ROAD_TYPE

    Route did not manage to avoid restricted truck road types.

### VIOLATED_AVOID_TOLL_TRANSPONDER

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_TOLL_TRANSPONDER

    Route did not manage to avoid toll booth that requires transponder. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_CHARGING_STATION_OPENING_HOURS

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_CHARGING_STATION_OPENING_HOURS

    Charging at the charging station planned at the destination of this section falls outside of opening hours. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### VIOLATED_AVOID_DIFFICULT_TURNS

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_AVOID_DIFFICULT_TURNS

    Route did not manage to avoid difficult turns. Severity: [`NoticeSeverity.CRITICAL`](sdk-for-android-explore-api-reference-latestnoticeseverity#CRITICAL).

### SEASONAL_CLOSURE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") SEASONAL_CLOSURE

    Route goes through seasonal closure. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### TOLL_TRANSPONDER

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") TOLL_TRANSPONDER

    Route goes through toll booth that requires transponder. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### TOLLS_DATA_UNAVAILABLE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") TOLLS_DATA_UNAVAILABLE

    Tolls data was requested but could not be calculated for this section. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### TOLLS_DATA_TEMPORARILY_UNAVAILABLE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") TOLLS_DATA_TEMPORARILY_UNAVAILABLE

    Tolls data was requested but is temporarily unavailable. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### CHARGING_STOP_NOT_NEEDED

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") CHARGING_STOP_NOT_NEEDED

    A charging stop was planned at the destination of this section, but it is no longer needed. It may be issued only when refreshing a route via [`RouteHandle`](sdk-for-android-explore-api-reference-latestroutehandle "class in com.here.sdk.routing"). Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### NO_SCHEDULE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") NO_SCHEDULE

    No schedule information is available for a transit section. As a result, departure/arrival times are approximated. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### NO_INTERMEDIATE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") NO_INTERMEDIATE

    Information about intermediate stops is not available for a transit section. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### UNWANTED_MODE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") UNWANTED_MODE

    This transit section contains a transport mode that was explictly disabled. Mode filtering is not available in this area. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### SCHEDULED_TIMES

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") SCHEDULED_TIMES

    This transit section returned times which are scheduled times, even though delay information is available. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### SIMPLE_POLYLINE

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") SIMPLE_POLYLINE

    An accurate polyline is not available for this section. An accurate polyline is not available for this section. The returned polyline has been generated from departure and arrival places. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### POTENTIAL_CARPOOL

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") POTENTIAL_CARPOOL

    Route utilizes a designated carpool lane, potentially subject to restrictions beyond the scheduled travel hours. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### POTENTIAL_TURN_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") POTENTIAL_TURN_RESTRICTION

    Route includes a turn that is potentially restricted and inaccessible beyond the scheduled travel hours. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### POTENTIAL_VEHICLE_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") POTENTIAL_VEHICLE_RESTRICTION

    Route utilizes roads that are potentially off-limits to the specified vehicle profile beyond the scheduled travel hours. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### POTENTIAL_ZONE_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") POTENTIAL_ZONE_RESTRICTION

    Route incorporates roads within zones, which are potentially not accessible beyond the scheduled travel hours. Severity: [`NoticeSeverity.INFO`](sdk-for-android-explore-api-reference-latestnoticeseverity#INFO).

### VIOLATED_MIN_CHARGE_AT_FIRST_CS

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_MIN_CHARGE_AT_FIRST_CS

    The route can not reach the first charging station with the minimum required charge, as the initial charge was to low.

### VIOLATED_MIN_CHARGE_AT_CS

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_MIN_CHARGE_AT_CS

    The route can not reach all charging stations on the route with the minimum required charge, as the initial charge was to low.

### VIOLATED_MIN_CHARGE_AT_DESTINATION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") VIOLATED_MIN_CHARGE_AT_DESTINATION

    The route can not reach the waypoint, as the there are not enough charging stops available or the initial charge was to low.

### NO_THROUGH_RESTRICTION

public static final [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") NO_THROUGH_RESTRICTION

    Route goes through a road that does not allow through traffic.

## Method Details

### values

public static [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing")\[\] values()

    Returns an array containing the constants of this enum class, in the order they are declared.
Returns:
    an array containing the constants of this enum class, in the order they are declared

### valueOf

public static [SectionNoticeCode](sdk-for-android-explore-api-reference-latestsectionnoticecode "enum class in com.here.sdk.routing") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Returns the enum constant of this class with the specified name. The string must match *exactly* an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)
Parameters:
    `name` - the name of the enum constant to be returned.

    Returns:
    the enum constant with the specified name

    Throws:
    [IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html) - if this enum class has no constant with the specified name

    [NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html) - if the argument is null
