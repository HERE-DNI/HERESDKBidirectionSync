---
title: "LineTileDataSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlinetiledatasource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LineTileDataSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.LineTileDataSource
------------------------------------------------------------------------
public final class LineTileDataSource extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Line tile data source allows the rendering engine access to user managed data sets of geodetic lines and their attributes through a [`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource").

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Method Summary

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`LineTileDataSource`](sdk-for-android-explore-api-reference-latestlinetiledatasource "class in com.here.sdk.mapview.datasource")

  [create](#create(com.here.sdk.mapview.MapContext,java.lang.String,com.here.sdk.mapview.datasource.LineTileSource))`(`[`MapContext`](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview")` context, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name, `[`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource")` tileSource)`

Creates a named [`LineTileDataSource`](sdk-for-android-explore-api-reference-latestlinetiledatasource "class in com.here.sdk.mapview.datasource") in the given context over a given [`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource").

`void`

  [destroy](#destroy())`()`

Frees all internally used resources.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### create

@NonNull public static [LineTileDataSource](sdk-for-android-explore-api-reference-latestlinetiledatasource "class in com.here.sdk.mapview.datasource") create(@NonNull [MapContext](sdk-for-android-explore-api-reference-latestmapcontext "class in com.here.sdk.mapview") context, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name, @NonNull [LineTileSource](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource") tileSource)

    Creates a named [`LineTileDataSource`](sdk-for-android-explore-api-reference-latestlinetiledatasource "class in com.here.sdk.mapview.datasource") in the given context over a given [`LineTileSource`](sdk-for-android-explore-api-reference-latestlinetilesource "interface in com.here.sdk.mapview.datasource").
Parameters:
    `context` -

    Map context to associate the data source with.

    `name` -

    Name of the data source to be created. Must be unique.

    `tileSource` -

    The source of tile data.

    Returns:
    Instance of the data source created with given name and tile source.

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
