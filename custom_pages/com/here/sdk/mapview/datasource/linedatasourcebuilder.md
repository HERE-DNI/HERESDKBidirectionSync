---
title: "LineDataSourceBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlinedatasourcebuilder"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LineDataSourceBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.LineDataSourceBuilder
------------------------------------------------------------------------
public final class LineDataSourceBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Builder of lines data source.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Constructor Summary

Constructors

Constructor

  Description

  [LineDataSourceBuilder](#%3Cinit%3E(com.here.sdk.mapview.MapContext))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context)`

Creates a data source builder instance in the given context.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`LineDataSource`](sdk-for-android-explore-api-reference-latestlinedatasource "class in com.here.sdk.mapview.datasource")

  [build](#build())`()`

Builds instance of LineDataSource.

[`LineDataSourceBuilder`](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withName](#withName(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` dataSourceName)`

Configures the builder to use the given name for data source.

[`LineDataSourceBuilder`](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withPolyline](#withPolyline(com.here.sdk.mapview.datasource.LineData))`(`[`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")` polyline)`

Configures the builder to insert the given polyline in the data source.

[`LineDataSourceBuilder`](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource")

  [withPolylines](#withPolylines(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")`> polylines)`

Configures the builder to insert the given polylines in the data source.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapContext)" class="section detail">

### LineDataSourceBuilder

public LineDataSourceBuilder(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context)

    Creates a data source builder instance in the given context.
Parameters:
    `context` -

    Map context to associate the data source with.

## Method Details

### withName

@NonNull public [LineDataSourceBuilder](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource") withName(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dataSourceName)

    Configures the builder to use the given name for data source.
Parameters:
    `dataSourceName` -

    Name of the created data source. Must be unique.

    Returns:
    This data source builder instance.

### withPolyline

@NonNull public [LineDataSourceBuilder](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource") withPolyline(@NonNull [LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") polyline)

    Configures the builder to insert the given polyline in the data source.
Parameters:
    `polyline` -

    Polyline to add.

    Returns:
    This data source builder instance.

### withPolylines

@NonNull public [LineDataSourceBuilder](sdk-for-android-explore-api-reference-latestlinedatasourcebuilder "class in com.here.sdk.mapview.datasource") withPolylines(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")\> polylines)

    Configures the builder to insert the given polylines in the data source.
Parameters:
    `polylines` -

    Polylines to add.

    Returns:
    This data source builder instance.

### build

@NonNull public [LineDataSource](sdk-for-android-explore-api-reference-latestlinedatasource "class in com.here.sdk.mapview.datasource") build()

    Builds instance of LineDataSource.
Returns:
    Instance of the data source created with given polylines and attributes.
