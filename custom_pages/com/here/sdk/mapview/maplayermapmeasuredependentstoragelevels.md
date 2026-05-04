---
title: "MapLayerMapMeasureDependentStorageLevels (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapLayerMapMeasureDependentStorageLevels

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels
------------------------------------------------------------------------
public final class MapLayerMapMeasureDependentStorageLevels extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Provides a mapping between a MapLayer map measure to datasource storage level.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapLayerMapMeasureDependentStorageLevels`](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")

  [withStorageLevelOffset](#withStorageLevelOffset(int))`(int offset)`

Creates an instance of [`MapLayerMapMeasureDependentStorageLevels`](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview") with the specified storage level offset.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### withStorageLevelOffset

@NonNull public static [MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview") withStorageLevelOffset(int offset)

    Creates an instance of [`MapLayerMapMeasureDependentStorageLevels`](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview") with the specified storage level offset. This creates a map where the storage level is determined by applying an "offset" to the zoom level. A negative offset results in a storage level lower than the zoom level, while a positive offset increases it. For example, with an offset of 0, the storage level matches the zoom level directly. An offset of -1 makes the storage level one less than the zoom level, and so on. The offset value is clamped to the range of -3 to 3. Note: The generated mapping adjusts so that when the map camera is significantly tilted, the storage level is further reduced for data near the horizon.
Parameters:
    `offset` -

    Defines an offset of storage level from the zoom level. The value will be clamped to a range of -3 to 3.

    Returns:
    MapLayerMapMeasureDependentStorageLevels instance.
