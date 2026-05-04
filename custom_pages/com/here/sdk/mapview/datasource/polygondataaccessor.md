---
title: "PolygonDataAccessor (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolygondataaccessor"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PolygonDataAccessor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PolygonDataAccessor
------------------------------------------------------------------------
public final class PolygonDataAccessor extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.

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

Gets polygon attributes accessor.

[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")

  [getGeometry](#getGeometry())`()`

Gets polygon geometry.

`void`

  [setAttributes](#setAttributes(com.here.sdk.mapview.datasource.DataAttributes))`(`[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")` attributes)`

Replaces polygon attributes.

`void`

  [setGeometry](#setGeometry(com.here.sdk.core.GeoPolygon))`(`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")` geometry)`

Replaces polygon geometry.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getGeometry

@NonNull public [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") getGeometry()

    Gets polygon geometry.
Returns:
    The polygon geometry.

### getAttributes

@NonNull public [DataAttributesAccessor](sdk-for-android-explore-api-reference-latestdataattributesaccessor "class in com.here.sdk.mapview.datasource") getAttributes()

    Gets polygon attributes accessor.
Returns:
    The polygon attributes accessor.

### setGeometry

public void setGeometry(@NonNull [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") geometry)

    Replaces polygon geometry. The outer boundary has to be ordered clockwise and closed.

    Altitude of the vertices is ignored.

    The visual behaviour for self-intersecting outer boundary is undefined.
Parameters:
    `geometry` -

    Geometry of the polygon. The outer boundary has to be ordered clockwise and closed. Altitude of the vertices is ignored. The visual behaviour for self-intersecting outer boundary is undefined.

### setAttributes

public void setAttributes(@NonNull [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") attributes)

    Replaces polygon attributes.
Parameters:
    `attributes` -

    The attributes.
