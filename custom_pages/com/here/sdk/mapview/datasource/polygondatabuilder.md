---
title: "PolygonDataBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolygondatabuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PolygonDataBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PolygonDataBuilder
------------------------------------------------------------------------
public final class PolygonDataBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder of [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") instances.

The builder can create [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") instances for polygons with an outer boundary and optionally one or more inner boundaries (holes).

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [PolygonDataBuilder](#%3Cinit%3E())`()`

Creates a builder instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds an instance of [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") and resets the builder instance.

[`PolygonDataBuilder`](sdk-for-android-explore-api-reference-latestpolygondatabuilder "class in com.here.sdk.mapview.datasource")

  [withAttributes](#withAttributes(com.here.sdk.mapview.datasource.DataAttributes))`(`[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")` attributes)`

Configures the builder with custom attributes for polygon to be created.

[`PolygonDataBuilder`](sdk-for-android-explore-api-reference-latestpolygondatabuilder "class in com.here.sdk.mapview.datasource")

  [withGeometry](#withGeometry(com.here.sdk.core.GeoPolygon))`(`[`GeoPolygon`](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core")` geometry)`

Configures the builder with geometry for the polygon to be created.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### PolygonDataBuilder

public PolygonDataBuilder()

    Creates a builder instance.

## Method Details

### withGeometry

@NonNull public [PolygonDataBuilder](sdk-for-android-explore-api-reference-latestpolygondatabuilder "class in com.here.sdk.mapview.datasource") withGeometry(@NonNull [GeoPolygon](sdk-for-android-explore-api-reference-latestgeopolygon "class in com.here.sdk.core") geometry)

    Configures the builder with geometry for the polygon to be created.
Parameters:
    `geometry` -

    Geometry of the polygon. The outer boundary has to be ordered clockwise and closed. Any inner boundary has to be ordered counterclockwise and closed. Altitude of boundary vertices is ignored. The visual behaviour for self-intersecting outer boundary is undefined.

    Returns:
    The builder.

### withAttributes

@NonNull public [PolygonDataBuilder](sdk-for-android-explore-api-reference-latestpolygondatabuilder "class in com.here.sdk.mapview.datasource") withAttributes(@NonNull [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") attributes)

    Configures the builder with custom attributes for polygon to be created.
Parameters:
    `attributes` -

    Custom data attributes to be associated with the polygon.

    Returns:
    The builder.

### build

@NonNull public [PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") build()

    Builds an instance of [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") and resets the builder instance.
Returns:
    Instance of [`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") created with the configured parameters.
