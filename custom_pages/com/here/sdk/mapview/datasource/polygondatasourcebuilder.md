---
title: "PolygonDataSourceBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PolygonDataSourceBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PolygonDataSourceBuilder
------------------------------------------------------------------------
public final class PolygonDataSourceBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder of the polygons data source.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [PolygonDataSourceBuilder](#%3Cinit%3E(com.here.sdk.mapview.MapContext))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context)`

Creates a data source builder instance in the given context.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`PolygonDataSource`](sdk-for-android-explore-api-reference-latestpolygondatasource "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds a PolygonDataSource instance.

[`PolygonDataSourceBuilder`](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withName](#withName(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` dataSourceName)`

Configures the builder to use the given name for data source.

[`PolygonDataSourceBuilder`](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withPolygon](#withPolygon(com.here.sdk.mapview.datasource.PolygonData))`(`[`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")` polygon)`

Configures the builder to insert the given polygon in the data source.

[`PolygonDataSourceBuilder`](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withPolygons](#withPolygons(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")`> polygon)`

Configures the builder to insert the given polygons in the data source.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapContext)" class="section detail">

### PolygonDataSourceBuilder

public PolygonDataSourceBuilder(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context)

    Creates a data source builder instance in the given context.
Parameters:
    `context` -

    Map context to associate the data source with.

## Method Details

### withName

@NonNull public [PolygonDataSourceBuilder](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource") withName(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dataSourceName)

    Configures the builder to use the given name for data source.
Parameters:
    `dataSourceName` -

    Name of the created data source. Must be unique.

    Returns:
    This data source builder instance.

### withPolygon

@NonNull public [PolygonDataSourceBuilder](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource") withPolygon(@NonNull [PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") polygon)

    Configures the builder to insert the given polygon in the data source.
Parameters:
    `polygon` -

    The polygon to add.

    Returns:
    This data source builder instance.

### withPolygons

@NonNull public [PolygonDataSourceBuilder](sdk-for-android-explore-api-reference-latestpolygondatasourcebuilder "class in com.here.sdk.mapview.datasource") withPolygons(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")\> polygon)

    Configures the builder to insert the given polygons in the data source.
Parameters:
    `polygon` -

    The polygons to add.

    Returns:
    This data source builder instance.

### build

@NonNull public [PolygonDataSource](sdk-for-android-explore-api-reference-latestpolygondatasource "class in com.here.sdk.mapview.datasource") build()

    Builds a PolygonDataSource instance.
Returns:
    Instance of the data source created with given polygons and attributes.
