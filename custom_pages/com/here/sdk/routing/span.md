---
title: "Span (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestspan"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Span

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.Span
------------------------------------------------------------------------
public final class Span extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A span is a part of the [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing") which is traversable or navigable. Each span usually has some geometry associated with it.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getBaseDuration](#getBaseDuration())`()`

Gets the time duration necessary to traverse the span, using the speed provided in [`getDynamicSpeedInfo()`](#getDynamicSpeedInfo()) without taking into consideration the delays caused by the traffic.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`AccessAttributes`](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")`>`

  [getCarAttributes](#getCarAttributes())`()`

The list of car access attributes on the span.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getConsumptionInKilowattHours](#getConsumptionInKilowattHours())`()`

Gets the power consumption in kilowatt per hour necessary to traverse the span.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getCountryCode](#getCountryCode())`()`

Gets the country code of the span.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getDuration](#getDuration())`()`

Gets the time duration necessary to traverse the span, using the speed provided in [`getDynamicSpeedInfo()`](#getDynamicSpeedInfo()).

[`DynamicSpeedInfo`](sdk-for-android-explore-api-reference-latestdynamicspeedinfo "class in com.here.sdk.routing")

  [getDynamicSpeedInfo](#getDynamicSpeedInfo())`()`

The dynamic speed information on the span.

[`FunctionalRoadClass`](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing")

  [getFunctionalRoadClass](#getFunctionalRoadClass())`()`

Gets the functional road class of the span.

[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets the [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this span.

`int`

  [getLengthInMeters](#getLengthInMeters())`()`

Gets the length of this span in meters.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [getNoThroughRestrictionsIndexes](#getNoThroughRestrictionsIndexes())`()`

Get the list of indexes to [`Section.getNoThroughRestrictions()`](sdk-for-android-explore-api-reference-latestsection#getNoThroughRestrictions()) the parent section owns.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [getNoticeIndexes](#getNoticeIndexes())`()`

Gets the list of indexes to [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) the parent section owns.

[`LocalizedRoadNumbers`](sdk-for-android-explore-api-reference-latestlocalizedroadnumbers "class in com.here.sdk.routing")

  [getRoadNumbers](#getRoadNumbers())`()`

Gets the road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (`RouteType`).

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`AccessAttributes`](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")`>`

  [getScooterAttributes](#getScooterAttributes())`()`

The list of scooter access attributes on the span.

`int`

  [getSectionPolylineOffset](#getSectionPolylineOffset())`()`

Gets the position of the span inside the section's geometry, given as an offset.

[`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")

  [getSegmentReference](#getSegmentReference())`()`

Gets the segment reference of this span.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getShieldText](#getShieldText(com.here.sdk.routing.LocalizedRoadNumber))`(`[`LocalizedRoadNumber`](sdk-for-android-explore-api-reference-latestlocalizedroadnumber "class in com.here.sdk.routing")` roadNumber)`

Converts full route number to the value to be displayed on the road shield.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getSpeedLimitInMetersPerSecond](#getSpeedLimitInMetersPerSecond())`()`

Gets the speed limit in meters per second on the span.

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getStateCode](#getStateCode())`()`

Gets the state code of the span.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`StreetAttributes`](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")`>`

  [getStreetAttributes](#getStreetAttributes())`()`

The list of street attributes on the span.

[`LocalizedTexts`](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core")

  [getStreetNames](#getStreetNames())`()`

The street names on the span.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)`>`

  [getTrafficIncidentIndexes](#getTrafficIncidentIndexes())`()`

The indexes of traffic incidents from the field [`Section.getTrafficIncidents()`](sdk-for-android-explore-api-reference-latestsection#getTrafficIncidents()) of the parent [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing").

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`AccessAttributes`](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")`>`

  [getTruckAttributes](#getTruckAttributes())`()`

The list of truck access attributes on the span.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`WalkAttributes`](sdk-for-android-explore-api-reference-latestwalkattributes "enum class in com.here.sdk.routing")`>`

  [getWalkAttributes](#getWalkAttributes())`()`

The list of walk attributes on the span.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getShieldText

@NonNull public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getShieldText(@NonNull [LocalizedRoadNumber](sdk-for-android-explore-api-reference-latestlocalizedroadnumber "class in com.here.sdk.routing") roadNumber)

    Converts full route number to the value to be displayed on the road shield. The results are based on country code and state code of `Span` object and route type of passed `road_number` argument.
Parameters:
    `roadNumber` -

    Route number to convert to shield text.

    Returns:
    Text on the road shield to display.

### getGeometry

@NonNull public [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") getGeometry()

    Gets the [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this span.
Returns:
    The [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this span.

### getLengthInMeters

public int getLengthInMeters()

    Gets the length of this span in meters.
Returns:
    The length of this span in meters.

### getNoticeIndexes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> getNoticeIndexes()

    Gets the list of indexes to [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) the parent section owns. In case the list is not empty, the user must judge all the indexed [`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing")'s carefully before proceeding.
Returns:
    The list of indexes to [`Section.getSectionNotices()`](sdk-for-android-explore-api-reference-latestsection#getSectionNotices()) the parent section owns. In case the list is not empty, the user must judge all the indexed [`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing")s carefully before proceeding.

### getSegmentReference

@NonNull public [SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing") getSegmentReference()

    Gets the segment reference of this span.
Returns:
    The segment reference of this span.

### getTrafficIncidentIndexes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> getTrafficIncidentIndexes()

    The indexes of traffic incidents from the field [`Section.getTrafficIncidents()`](sdk-for-android-explore-api-reference-latestsection#getTrafficIncidents()) of the parent [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing"). Each matching incident takes at least a whole [`getGeometry()`](#getGeometry()). The same incident can take other spans and an area out of the built route as well.
Returns:
    The indexes of traffic incidents from the field [`Section.getTrafficIncidents()`](sdk-for-android-explore-api-reference-latestsection#getTrafficIncidents()) of the parent [`Section`](sdk-for-android-explore-api-reference-latestsection "class in com.here.sdk.routing"). Each matching incident takes at least a whole [`getGeometry()`](#getGeometry()). The same incident can take other spans and an area out of the built route as well.

### getSectionPolylineOffset

public int getSectionPolylineOffset()

    Gets the position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry.
Returns:
    The position of the span inside the section's geometry, given as an offset. The span geometry starts from this offset and ends on the offset of the next span, both start offset point and end offset point being included in the span, because the spans' geometry share a point in the section's geometry.

### getDynamicSpeedInfo

@Nullable public [DynamicSpeedInfo](sdk-for-android-explore-api-reference-latestdynamicspeedinfo "class in com.here.sdk.routing") getDynamicSpeedInfo()

    The dynamic speed information on the span.
Returns:
    The dynamic speed information on the span.

### getStreetAttributes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[StreetAttributes](sdk-for-android-explore-api-reference-lateststreetattributes "enum class in com.here.sdk.routing")\> getStreetAttributes()

    The list of street attributes on the span.
Returns:
    The list of street attributes on the span.

### getCarAttributes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[AccessAttributes](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")\> getCarAttributes()

    The list of car access attributes on the span.
Returns:
    The list of car access attributes on the span.

### getTruckAttributes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[AccessAttributes](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")\> getTruckAttributes()

    The list of truck access attributes on the span.
Returns:
    The list of truck access attributes on the span.

### getScooterAttributes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[AccessAttributes](sdk-for-android-explore-api-reference-latestaccessattributes "enum class in com.here.sdk.routing")\> getScooterAttributes()

    The list of scooter access attributes on the span.
Returns:
    The list of scooter access attributes on the span.

### getWalkAttributes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[WalkAttributes](sdk-for-android-explore-api-reference-latestwalkattributes "enum class in com.here.sdk.routing")\> getWalkAttributes()

    The list of walk attributes on the span.
Returns:
    The list of walk attributes on the span.

### getStreetNames

@NonNull public [LocalizedTexts](sdk-for-android-explore-api-reference-latestlocalizedtexts "class in com.here.sdk.core") getStreetNames()

    The street names on the span.
Returns:
    The street names on the span.

### getRoadNumbers

@NonNull public [LocalizedRoadNumbers](sdk-for-android-explore-api-reference-latestlocalizedroadnumbers "class in com.here.sdk.routing") getRoadNumbers()

    Gets the road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (`RouteType`).
Returns:
    The road numbers on the span enriched with information specific to *route numbers* of a road such as I-10, US-50, or A3, and cardinal direction, if available, and a road level classification (`RouteType`).

### getSpeedLimitInMetersPerSecond

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getSpeedLimitInMetersPerSecond()

    Gets the speed limit in meters per second on the span.
Returns:
    The speed limit in meters per second on the span.

### getConsumptionInKilowattHours

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getConsumptionInKilowattHours()

    Gets the power consumption in kilowatt per hour necessary to traverse the span.
Returns:
    The power consumption in kilowatt per hour necessary to traverse the span.

### getFunctionalRoadClass

@Nullable public [FunctionalRoadClass](sdk-for-android-explore-api-reference-latestfunctionalroadclass "enum class in com.here.sdk.routing") getFunctionalRoadClass()

    Gets the functional road class of the span.
Returns:
    The functional road class of the span.

### getDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getDuration()

    Gets the time duration necessary to traverse the span, using the speed provided in [`getDynamicSpeedInfo()`](#getDynamicSpeedInfo()). This duration takes also into consideration the delays caused by the traffic.
Returns:
    The time duration necessary to traverse the span, using the speed provided in [`getDynamicSpeedInfo()`](#getDynamicSpeedInfo()). This duration takes also into consideration the delays caused by the traffic.

### getBaseDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getBaseDuration()

    Gets the time duration necessary to traverse the span, using the speed provided in [`getDynamicSpeedInfo()`](#getDynamicSpeedInfo()) without taking into consideration the delays caused by the traffic.
Returns:
    The time duration necessary to traverse the span, using the speed provided in [`getDynamicSpeedInfo()`](#getDynamicSpeedInfo()) without taking into consideration the delays caused by the traffic.

### getCountryCode

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getCountryCode()

    Gets the country code of the span. The value is `null` when no data is available.
Returns:
    The country code of the span. The value is `null` when no data is available.

### getStateCode

@Nullable public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getStateCode()

    Gets the state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is `null` when no data is available.
Returns:
    The state code of the span. State code is available in some countries to denote principal subdivisions(provinces or states), e.g. in the United States, AK stands for Alaska and OH stands for Ohio. The format of state code can vary for different countries, take the United States as example, it consists of two alphabet letters. The value is `null` when no data is available.

### getNoThroughRestrictionsIndexes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html)\> getNoThroughRestrictionsIndexes()

    Get the list of indexes to [`Section.getNoThroughRestrictions()`](sdk-for-android-explore-api-reference-latestsection#getNoThroughRestrictions()) the parent section owns. In case the list is not empty, the user must judge all the indexed [`Section.getNoThroughRestrictions()`](sdk-for-android-explore-api-reference-latestsection#getNoThroughRestrictions())'s carefully before proceeding.
Returns:
    The list of indexes to [`Section.getNoThroughRestrictions()`](sdk-for-android-explore-api-reference-latestsection#getNoThroughRestrictions()) the parent section owns. In case the list is not empty, the user must judge all the indexed sdk routing noThroughRestriction's carefully before proceeding.
