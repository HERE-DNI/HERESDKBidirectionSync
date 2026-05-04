---
title: "AvoidanceOptions (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestavoidanceoptions"
hidden: false
---

Package [com.here.sdk.routing](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class AvoidanceOptions

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.routing.AvoidanceOptions
------------------------------------------------------------------------
public final class AvoidanceOptions extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
The options to specify restrictions for route calculations.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`AvoidBoundingBoxAreaOptions`](sdk-for-android-explore-api-reference-latestavoidboundingboxareaoptions "class in com.here.sdk.routing")`>`

  [avoidBoundingBoxAreasOptions](#avoidBoundingBoxAreasOptions)

List of rectangular shapes which routes must not cross and additional options for this area.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`AvoidCorridorAreaOptions`](sdk-for-android-explore-api-reference-latestavoidcorridorareaoptions "class in com.here.sdk.routing")`>`

  [avoidCorridorAreasOptions](#avoidCorridorAreasOptions)

List of corridor shapes which routes must not cross and additional options for this area.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`TruckRoadType`](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")`>`

  [avoidedTruckRoadTypes](#avoidedTruckRoadTypes)

Specifies a list of avoided truck road types for vehicle.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`AvoidPolygonAreaOptions`](sdk-for-android-explore-api-reference-latestavoidpolygonareaoptions "class in com.here.sdk.routing")`>`

  [avoidPolygonAreasOptions](#avoidPolygonAreasOptions)

List of polygon shapes which routes must not cross and additional options for this area.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`CountryCode`](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")`>`

  [countries](#countries)

Countries that the route must avoid.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [exceptZoneIds](#exceptZoneIds)

Exception to `AvoidanceOptions.zone_categories`, which can be specified by list of zone identifiers.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`RoadFeatures`](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")`>`

  [roadFeatures](#roadFeatures)

Features which routes should avoid.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`SegmentReference`](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")`>`

  [segments](#segments)

Segments that routes will avoid going through.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`ZoneCategory`](sdk-for-android-explore-api-reference-latestzonecategory "enum class in com.here.sdk.routing")`>`

  [zoneCategories](#zoneCategories)

Zone categories which routes must not cross.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)`>`

  [zoneIds](#zoneIds)

List containing identifiers of zones that routes should avoid going through.

## Constructor Summary

Constructors

Constructor

  Description

  [AvoidanceOptions](#%3Cinit%3E())`()`

Creates a new instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `boolean`

  [equals](#equals(java.lang.Object))`(`[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)` obj)`

  `int`

  [hashCode](#hashCode())`()`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### roadFeatures

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[RoadFeatures](sdk-for-android-explore-api-reference-latestroadfeatures "enum class in com.here.sdk.routing")\> roadFeatures

    Features which routes should avoid. Best effort only (not enforced).

### countries

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[CountryCode](sdk-for-android-explore-api-reference-latestcountrycode "enum class in com.here.sdk.core")\> countries

    Countries that the route must avoid. Strictly enforced. Violations are reported as [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_BLOCKED_ROAD). **Note:** This avoidance option is not supported in `IsolineOptions` for isoline calculation.

### avoidBoundingBoxAreasOptions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[AvoidBoundingBoxAreaOptions](sdk-for-android-explore-api-reference-latestavoidboundingboxareaoptions "class in com.here.sdk.routing")\> avoidBoundingBoxAreasOptions

    List of rectangular shapes which routes must not cross and additional options for this area.

### avoidPolygonAreasOptions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[AvoidPolygonAreaOptions](sdk-for-android-explore-api-reference-latestavoidpolygonareaoptions "class in com.here.sdk.routing")\> avoidPolygonAreasOptions

    List of polygon shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of polygons is limited to 20.

### avoidCorridorAreasOptions

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[AvoidCorridorAreaOptions](sdk-for-android-explore-api-reference-latestavoidcorridorareaoptions "class in com.here.sdk.routing")\> avoidCorridorAreasOptions

    List of corridor shapes which routes must not cross and additional options for this area. **Note:** Currently, the maximum count of corridors is limited to 20.

### zoneCategories

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[ZoneCategory](sdk-for-android-explore-api-reference-latestzonecategory "enum class in com.here.sdk.routing")\> zoneCategories

    Zone categories which routes must not cross. Strictly enforced. Violations are reported as [`SectionNoticeCode.VIOLATED_ZONE_RESTRICTION`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_ZONE_RESTRICTION).

### segments

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[SegmentReference](sdk-for-android-explore-api-reference-latestsegmentreference "class in com.here.sdk.routing")\> segments

    Segments that routes will avoid going through. Violations are reported as [`SectionNoticeCode.VIOLATED_BLOCKED_ROAD`](sdk-for-android-explore-api-reference-latestsectionnoticecode#VIOLATED_BLOCKED_ROAD).

    **Notes:**

    - This avoidance option is not supported in `IsolineOptions` for isoline calculation.
    - The engine does not support an unlimited number of segments to avoid. The limit is defined by the HERE backend services and may change. For now, the maximum number of segments to avoid should be below 250. This value may change on the backend and it is therefore not guaranteed to be stable.

### exceptZoneIds

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> exceptZoneIds

    Exception to `AvoidanceOptions.zone_categories`, which can be specified by list of zone identifiers. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".

### zoneIds

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)\> zoneIds

    List containing identifiers of zones that routes should avoid going through. e.g. the format of ID is like `here:cm:envzone:2`. Information about the various routing zones originates from the respective catalogs of platform.here.com. For example, more information on zone IDs for Environmental Zones is available under "https://platform.here.com/data/hrn:here:data::olp-here:rib-2/environmental-zones/overview".

### avoidedTruckRoadTypes

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[TruckRoadType](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport")\> avoidedTruckRoadTypes

    Specifies a list of avoided truck road types for vehicle. Refer to [`TruckRoadType`](sdk-for-android-explore-api-reference-latesttruckroadtype "enum class in com.here.sdk.transport") for the available options.

## Constructor Details

  - ()" class="section detail">

### AvoidanceOptions

public AvoidanceOptions()

    Creates a new instance.

## Method Details

### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html) obj)
Overrides:
    [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

### hashCode

public int hashCode()
Overrides:
    [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()) in class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
