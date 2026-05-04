---
title: "MapPickResult (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmappickresult"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapPickResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapPickResult
------------------------------------------------------------------------
public final class MapPickResult extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
A class representing a map pick result.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapObjectDescriptor`](sdk-for-android-explore-api-reference-latestmapobjectdescriptor "class in com.here.sdk.mapview")`>`

  [getCustomLayerObjectDescriptors](#getCustomLayerObjectDescriptors())`()`

Gets a list of map object descriptors representing picked objects from custom user data layers.

[`PickMapContentResult`](sdk-for-android-explore-api-reference-latestpickmapcontentresult "class in com.here.sdk.mapview")

  [getMapContent](#getMapContent())`()`

Gets a picked map content result.

[`PickMapItemsResult`](sdk-for-android-explore-api-reference-latestpickmapitemsresult "class in com.here.sdk.mapview")

  [getMapItems](#getMapItems())`()`

Gets a picked map items result.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getMapItems

@Nullable public [PickMapItemsResult](sdk-for-android-explore-api-reference-latestpickmapitemsresult "class in com.here.sdk.mapview") getMapItems()

    Gets a picked map items result.
Returns:
    Picked map items result.

### getMapContent

@Nullable public [PickMapContentResult](sdk-for-android-explore-api-reference-latestpickmapcontentresult "class in com.here.sdk.mapview") getMapContent()

    Gets a picked map content result.
Returns:
    Picked map content result.

### getCustomLayerObjectDescriptors

@Nullable public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapObjectDescriptor](sdk-for-android-explore-api-reference-latestmapobjectdescriptor "class in com.here.sdk.mapview")\> getCustomLayerObjectDescriptors()

    Gets a list of map object descriptors representing picked objects from custom user data layers.
Returns:
    List of map object descriptors representing picked objects from custom user data layers.
