---
title: "Section (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestsection"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class Section

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.routing.Section
------------------------------------------------------------------------
public final class Section extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A section is a part of the route between two stopovers. A stopover is a location on the route where a stop is made.

**Note:** A section contains a list of [`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing") objects that describe *potential issues* after the route was calculated. If the list is non-empty, it is recommended to evaluate possible violations against the requested route options and reject the route if deemed necessary.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`LocationTime`](sdk-for-android-explore-api-reference-latestlocationtime "class in com.here.sdk.core")

  [getArrivalLocationTime](#getArrivalLocationTime())`()`

Gets the arrival location time of this section.

[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")

  [getArrivalPlace](#getArrivalPlace())`()`

Gets the arrival place.

[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")

  [getBoundingBox](#getBoundingBox())`()`

Gets the closest rectangular area where this section fits in.

[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html)

  [getConsumptionInKilowattHours](#getConsumptionInKilowattHours())`()`

Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle.

[`LocationTime`](sdk-for-android-explore-api-reference-latestlocationtime "class in com.here.sdk.core")

  [getDepartureLocationTime](#getDepartureLocationTime())`()`

Gets the departure location time of this section.

[`RoutePlace`](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing")

  [getDeparturePlace](#getDeparturePlace())`()`

Gets the departure place.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getDuration](#getDuration())`()`

Gets the estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets the [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this section.

`int`

  [getLengthInMeters](#getLengthInMeters())`()`

Gets the length of this section in meters.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Maneuver`](sdk-for-android-explore-api-reference-latestmaneuver "class in com.here.sdk.routing")`>`

  [getManeuvers](#getManeuvers())`()`

Gets the maneuvers for this section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ViolatedRestriction`](sdk-for-android-explore-api-reference-latestviolatedrestriction "class in com.here.sdk.routing")`>`

  [getNoThroughRestrictions](#getNoThroughRestrictions())`()`

list of no through restriction.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PassThroughWaypoint`](sdk-for-android-explore-api-reference-latestpassthroughwaypoint "class in com.here.sdk.routing")`>`

  [getPassthroughWaypoints](#getPassthroughWaypoints())`()`

Gets the list of passthrough waypoints in this section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PostAction`](sdk-for-android-explore-api-reference-latestpostaction "class in com.here.sdk.routing")`>`

  [getPostActions](#getPostActions())`()`

Gets the post actions that must be done after the arrival at the end of the section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PreAction`](sdk-for-android-explore-api-reference-latestpreaction "class in com.here.sdk.routing")`>`

  [getPreActions](#getPreActions())`()`

Gets the preceding actions that must be done prior to departure at the beginning of the section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SectionNotice`](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing")`>`

  [getSectionNotices](#getSectionNotices())`()`

Gets the notices which explains the issues encountered during processing of this section.

[`SectionTransportMode`](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing")

  [getSectionTransportMode](#getSectionTransportMode())`()`

Gets the transport mode of this section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Span`](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing")`>`

  [getSpans](#getSpans())`()`

Gets the [`Span`](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing")'s that constitute this section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`Toll`](sdk-for-android-explore-api-reference-latesttoll "class in com.here.sdk.routing")`>`

  [getTolls](#getTolls())`()`

Gets all the tolls for this section.

[`Duration`](sdk-for-android-explore-api-reference-latestduration "class in com.here.time")

  [getTrafficDelay](#getTrafficDelay())`()`

Gets the estimated extra time in seconds spent due to traffic delays along this section.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TrafficIncidentOnRoute`](sdk-for-android-explore-api-reference-latesttrafficincidentonroute "class in com.here.sdk.routing")`>`

  [getTrafficIncidents](#getTrafficIncidents())`()`

the list of traffic incidents that are found on the section.

[`TransitSectionDetails`](sdk-for-android-explore-api-reference-latesttransitsectiondetails "class in com.here.sdk.routing")

  [getTransitDetails](#getTransitDetails())`()`

Gets the details of a transit section.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getGeometry

@NonNull public [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") getGeometry()

    Gets the [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this section.
Returns:
    The [`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") object representing the polyline of this section.

### getSpans

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Span](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing")\> getSpans()

    Gets the [`Span`](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing")'s that constitute this section.
Returns:
    The [`Span`](sdk-for-android-explore-api-reference-latestspan "class in com.here.sdk.routing")'s that constitute this section.

### getManeuvers

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Maneuver](sdk-for-android-explore-api-reference-latestmaneuver "class in com.here.sdk.routing")\> getManeuvers()

    Gets the maneuvers for this section.
Returns:
    The maneuvers for this section.

### getBoundingBox

@NonNull public [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") getBoundingBox()

    Gets the closest rectangular area where this section fits in.
Returns:
    The closest rectangular area where this section fits in.

### getLengthInMeters

public int getLengthInMeters()

    Gets the length of this section in meters.
Returns:
    The length of this section in meters.

### getSectionTransportMode

@NonNull public [SectionTransportMode](sdk-for-android-explore-api-reference-latestsectiontransportmode "enum class in com.here.sdk.routing") getSectionTransportMode()

    Gets the transport mode of this section.
Returns:
    The transport mode of this section.

### getDeparturePlace

@NonNull public [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") getDeparturePlace()

    Gets the departure place.
Returns:
    Describes the departure place.

### getArrivalPlace

@NonNull public [RoutePlace](sdk-for-android-explore-api-reference-latestrouteplace "class in com.here.sdk.routing") getArrivalPlace()

    Gets the arrival place.

    Describes the arrival place.
Returns:
    The arrival place.

### getDepartureLocationTime

@Nullable public [LocationTime](sdk-for-android-explore-api-reference-latestlocationtime "class in com.here.sdk.core") getDepartureLocationTime()

    Gets the departure location time of this section.
Returns:
    The departure location time of this section.

### getArrivalLocationTime

@Nullable public [LocationTime](sdk-for-android-explore-api-reference-latestlocationtime "class in com.here.sdk.core") getArrivalLocationTime()

    Gets the arrival location time of this section.
Returns:
    The arrival location time of this section.

### getPreActions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PreAction](sdk-for-android-explore-api-reference-latestpreaction "class in com.here.sdk.routing")\> getPreActions()

    Gets the preceding actions that must be done prior to departure at the beginning of the section.
Returns:
    The preceding actions that must be done prior to departure at the beginning of the section.

### getPostActions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PostAction](sdk-for-android-explore-api-reference-latestpostaction "class in com.here.sdk.routing")\> getPostActions()

    Gets the post actions that must be done after the arrival at the end of the section.
Returns:
    The post actions that must be done after the arrival at the end of the section.

### getSectionNotices

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SectionNotice](sdk-for-android-explore-api-reference-latestsectionnotice "class in com.here.sdk.routing")\> getSectionNotices()

    Gets the notices which explains the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.
Returns:
    The notices which explain the issues encountered during processing of this section. For example, while the scooter transport mode is selected, if no reasonable alternative route is possible except violating controlled-access to highway rule for the section, one notice is generated for the violation. The user must judge all the notices carefully before proceeding.

### getConsumptionInKilowattHours

@Nullable public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html) getConsumptionInKilowattHours()

    Gets estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.
Returns:
    Estimated net energy consumption (in kWh) if the transportation mode used for this route is an electric vehicle. Note that it can be negative due to energy recuperation.

### getTransitDetails

@Nullable public [TransitSectionDetails](sdk-for-android-explore-api-reference-latesttransitsectiondetails "class in com.here.sdk.routing") getTransitDetails()

    Gets the details of a transit section.
Returns:
    The transit details which are avilable for transit sections of a route.

### getTolls

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[Toll](sdk-for-android-explore-api-reference-latesttoll "class in com.here.sdk.routing")\> getTolls()

    Gets all the tolls for this section. Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too.

    Note that tolls are found depending on the transport mode. For example, if pedestrian or bicycle transport mode specified, route sections have no tolls. Indoor route sections have no tolls, too. **Note**: If you're using the `OfflineRoutingEngine`, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the `OfflineRoutingEngine` is only available with the Navigate license. If you're using the `RoutingEngine`, this feature is considered to be stable.
Returns:
    All the tolls for this section.

### getTrafficIncidents

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TrafficIncidentOnRoute](sdk-for-android-explore-api-reference-latesttrafficincidentonroute "class in com.here.sdk.routing")\> getTrafficIncidents()

    the list of traffic incidents that are found on the section.
Returns:
    The list of traffic incidents that are found on the section.

### getDuration

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getDuration()

    Gets the estimated time in seconds needed to travel along this section, including real-time traffic delays if available.
Returns:
    The estimated time in seconds needed to travel along this section, including real-time traffic delays if available.

### getTrafficDelay

@NonNull public [Duration](sdk-for-android-explore-api-reference-latestduration "class in com.here.time") getTrafficDelay()

    Gets the estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.
Returns:
    The estimated extra time in seconds spent due to traffic delays along this section. Negative values indicate that the route can be traversed faster than usual.

### getPassthroughWaypoints

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PassThroughWaypoint](sdk-for-android-explore-api-reference-latestpassthroughwaypoint "class in com.here.sdk.routing")\> getPassthroughWaypoints()

    Gets the list of passthrough waypoints in this section.
Returns:
    The list of passthrough waypoints in this section.

### getNoThroughRestrictions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ViolatedRestriction](sdk-for-android-explore-api-reference-latestviolatedrestriction "class in com.here.sdk.routing")\> getNoThroughRestrictions()

    list of no through restriction.
Returns:
    The list of no through restriction The no through restriction area is part of the road network that do not allow through traffic. For example the `Resident only` sign indicates that vehicles are only allowed to enter this area if they are making a stop. This area will be set only if `origin`, `destination` or `via` waypoint will be requested within the area.
