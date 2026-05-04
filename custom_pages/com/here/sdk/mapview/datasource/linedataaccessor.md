---
title: "LineDataAccessor (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlinedataaccessor"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LineDataAccessor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.LineDataAccessor
------------------------------------------------------------------------
public final class LineDataAccessor extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Line data accessor used for manipulating polylines that are part of a LineDataSource.

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

Gets polyline attributes accessor.

[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets polyline geometry.

`void`

  [setAttributes](#setAttributes(com.here.sdk.mapview.datasource.DataAttributes))`(`[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")` attributes)`

Replaces polyline attributes.

`void`

  [setGeometry](#setGeometry(com.here.sdk.core.GeoPolyline))`(`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")` geometry)`

Replaces polyline geometry.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getGeometry

@NonNull public [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") getGeometry()

    Gets polyline geometry.
Returns:
    The line geometry.

### getAttributes

@NonNull public [DataAttributesAccessor](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource") getAttributes()

    Gets polyline attributes accessor.
Returns:
    The polyline attributes accessor.

### setGeometry

public void setGeometry(@NonNull [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") geometry)

    Replaces polyline geometry. Altitude of the vertices is ignored.
Parameters:
    `geometry` -

    The geometry.

### setAttributes

public void setAttributes(@NonNull [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") attributes)

    Replaces polyline attributes.
Parameters:
    `attributes` -

    The attributes.
