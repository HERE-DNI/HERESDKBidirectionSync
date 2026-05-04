---
title: "PointDataBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpointdatabuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PointDataBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PointDataBuilder
------------------------------------------------------------------------
public final class PointDataBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder of [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") instances.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [PointDataBuilder](#%3Cinit%3E())`()`

Creates a builder instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds an instance of [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") and resets the builder instance.

[`PointDataBuilder`](sdk-for-android-explore-api-reference-latestpointdatabuilder "class in com.here.sdk.mapview.datasource")

  [withAttributes](#withAttributes(com.here.sdk.mapview.datasource.DataAttributes))`(`[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")` attributes)`

Configures the builder with custom attributes for point to be created.

[`PointDataBuilder`](sdk-for-android-explore-api-reference-latestpointdatabuilder "class in com.here.sdk.mapview.datasource")

  [withCoordinates](#withCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` coordinates)`

Configures the builder with geodetic coordinates for point to be created.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### PointDataBuilder

public PointDataBuilder()

    Creates a builder instance.

## Method Details

### withCoordinates

@NonNull public [PointDataBuilder](sdk-for-android-explore-api-reference-latestpointdatabuilder "class in com.here.sdk.mapview.datasource") withCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") coordinates)

    Configures the builder with geodetic coordinates for point to be created.
Parameters:
    `coordinates` -

    Geodetic coordinates of the point. Altitude of coordinates is ignored.

    Returns:
    The builder.

### withAttributes

@NonNull public [PointDataBuilder](sdk-for-android-explore-api-reference-latestpointdatabuilder "class in com.here.sdk.mapview.datasource") withAttributes(@NonNull [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") attributes)

    Configures the builder with custom attributes for point to be created.
Parameters:
    `attributes` -

    Custom data attributes to be associated with the point.

    Returns:
    The builder.

### build

@NonNull public [PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") build()

    Builds an instance of [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") and resets the builder instance.
Returns:
    Instance of [`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") created with the configured parameters.
