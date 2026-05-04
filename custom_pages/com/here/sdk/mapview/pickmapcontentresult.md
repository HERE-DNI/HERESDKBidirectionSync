---
title: "PickMapContentResult (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpickmapcontentresult"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PickMapContentResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.PickMapContentResult
------------------------------------------------------------------------
public final class PickMapContentResult extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A class that contains possible results from picking map content on the map scene.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [PickMapContentResult.TrafficIncidentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult)

Carries the result of picking a Carto traffic incident object.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PickedPlace`](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core")`>`

  [getPickedPlaces](#getPickedPlaces())`()`

Gets a list of picked places containing the POIs at the location of picking.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PickMapContentResult.TrafficIncidentResult`](sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult "class in com.here.sdk.mapview")`>`

  [getTrafficIncidents](#getTrafficIncidents())`()`

Gets the list of traffic incidents at the location of picking.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getPickedPlaces

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PickedPlace](sdk-for-android-explore-api-reference-latestpickedplace "class in com.here.sdk.core")\> getPickedPlaces()

    Gets a list of picked places containing the POIs at the location of picking.
Returns:
    List of picked places containing the POIs at the location of picking.

### getTrafficIncidents

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PickMapContentResult.TrafficIncidentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult-trafficincidentresult "class in com.here.sdk.mapview")\> getTrafficIncidents()

    Gets the list of traffic incidents at the location of picking.
Returns:
    List of traffic incidents at the location of picking.
