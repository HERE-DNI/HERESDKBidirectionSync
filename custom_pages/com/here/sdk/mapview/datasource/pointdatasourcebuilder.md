---
title: "PointDataSourceBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpointdatasourcebuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PointDataSourceBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PointDataSourceBuilder
------------------------------------------------------------------------
public final class PointDataSourceBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder of points data source.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [PointDataSourceBuilder](#%3Cinit%3E(com.here.sdk.mapview.MapContext))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context)`

Creates a data source builder instance in the given context.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`PointDataSource`](sdk-for-android-explore-api-reference-latestpointdatasource "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds a PointDataSource instance and resets the builder instance.

[`PointDataSourceBuilder`](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withName](#withName(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` dataSourceName)`

Configures the builder to use the given name for data source.

[`PointDataSourceBuilder`](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withPoint](#withPoint(com.here.sdk.mapview.datasource.PointData))`(`[`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")` point)`

Configures the builder to insert the given point in the data source.

[`PointDataSourceBuilder`](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withPoints](#withPoints(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")`> points)`

Configures the builder to insert the given points in the data source.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapContext)" class="section detail">

### PointDataSourceBuilder

public PointDataSourceBuilder(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context)

    Creates a data source builder instance in the given context.
Parameters:
    `context` -

    Map context to associate the data source with.

## Method Details

### withName

@NonNull public [PointDataSourceBuilder](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource") withName(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dataSourceName)

    Configures the builder to use the given name for data source.
Parameters:
    `dataSourceName` -

    Name of the created data source. Must be unique.

    Returns:
    This data source builder instance.

### withPoint

@NonNull public [PointDataSourceBuilder](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource") withPoint(@NonNull [PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") point)

    Configures the builder to insert the given point in the data source.
Parameters:
    `point` -

    Point to be added.

    Returns:
    This data source builder instance.

### withPoints

@NonNull public [PointDataSourceBuilder](sdk-for-android-explore-api-reference-latestpointdatasourcebuilder "class in com.here.sdk.mapview.datasource") withPoints(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")\> points)

    Configures the builder to insert the given points in the data source.
Parameters:
    `points` -

    Points to be added.

    Returns:
    This data source builder instance.

### build

@NonNull public [PointDataSource](sdk-for-android-explore-api-reference-latestpointdatasource "class in com.here.sdk.mapview.datasource") build()

    Builds a PointDataSource instance and resets the builder instance.
Returns:
    Instance of the data source created with given points and attributes.
