---
title: "PointDataAccessor (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpointdataaccessor"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PointDataAccessor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PointDataAccessor
------------------------------------------------------------------------
public final class PointDataAccessor extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Point data accessor used for manipulating points that are part of a PointDataSource.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`DataAttributesAccessor`](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource")

  [getAttributes](#getAttributes())`()`

Gets point attributes accessor.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getCoordinates](#getCoordinates())`()`

Gets point coordinates.

`void`

  [setAttributes](#setAttributes(com.here.sdk.mapview.datasource.DataAttributes))`(`[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")` attributes)`

Replaces point attributes.

`void`

  [setCoordinates](#setCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` position)`

Updates point coordinates.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getCoordinates

@NonNull public [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getCoordinates()

    Gets point coordinates.
Returns:
    The point coordinates.

### getAttributes

@NonNull public [DataAttributesAccessor](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource") getAttributes()

    Gets point attributes accessor.
Returns:
    The point attributes accessor.

### setCoordinates

public void setCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") position)

    Updates point coordinates.
Parameters:
    `position` -

    The new point coordinates.

### setAttributes

public void setAttributes(@NonNull [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") attributes)

    Replaces point attributes.
Parameters:
    `attributes` -

    The new point attributes.
