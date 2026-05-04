---
title: "LineDataBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlinedatabuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LineDataBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.LineDataBuilder
------------------------------------------------------------------------
public final class LineDataBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder of [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") instances.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [LineDataBuilder](#%3Cinit%3E())`()`

Creates a builder instance.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds an instance of [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") and resets the builder instance.

[`LineDataBuilder`](sdk-for-android-explore-api-reference-latestlinedatabuilder "class in com.here.sdk.mapview.datasource")

  [withAttributes](#withAttributes(com.here.sdk.mapview.datasource.DataAttributes))`(`[`DataAttributes`](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource")` attributes)`

Configures the builder with custom attributes for line to be created.

[`LineDataBuilder`](sdk-for-android-explore-api-reference-latestlinedatabuilder "class in com.here.sdk.mapview.datasource")

  [withGeometry](#withGeometry(com.here.sdk.core.GeoPolyline))`(`[`GeoPolyline`](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core")` geometry)`

Configures the builder with geometry for line to be created.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### LineDataBuilder

public LineDataBuilder()

    Creates a builder instance.

## Method Details

### withGeometry

@NonNull public [LineDataBuilder](sdk-for-android-explore-api-reference-latestlinedatabuilder "class in com.here.sdk.mapview.datasource") withGeometry(@NonNull [GeoPolyline](sdk-for-android-explore-api-reference-latestgeopolyline "class in com.here.sdk.core") geometry)

    Configures the builder with geometry for line to be created.
Parameters:
    `geometry` -

    Geometry of the polyline. Each vertex defines two line segments: one with a previous vertex and one with a next vertex. First and last vertices don't have resp. previous and next vertices and thus belong to single line segments. Consecutive duplicate vertices are ignored. Altitude of polyline vertices is ignored.

    Returns:
    The builder.

### withAttributes

@NonNull public [LineDataBuilder](sdk-for-android-explore-api-reference-latestlinedatabuilder "class in com.here.sdk.mapview.datasource") withAttributes(@NonNull [DataAttributes](sdk-for-android-explore-api-reference-latestdataattributes "class in com.here.sdk.mapview.datasource") attributes)

    Configures the builder with custom attributes for line to be created.
Parameters:
    `attributes` -

    Custom data attributes to be associated with the line.

    Returns:
    The builder.

### build

@NonNull public [LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") build()

    Builds an instance of [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") and resets the builder instance.
Returns:
    Instance of [`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") created with the configured parameters.
