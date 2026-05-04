---
title: "PolygonDataSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpolygondatasource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PolygonDataSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PolygonDataSource
------------------------------------------------------------------------
public final class PolygonDataSource extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Polygon data source allows the rendering engine access to the user provided polygons geometry and their attributes.

Polygon segments are rendered following the shortest path between their end points.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor)

Called for each polygon, allowing inspection, removal or update of coordinates and attributes.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [add](#add(com.here.sdk.mapview.datasource.PolygonData))`(`[`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")` polygon)`

Adds a new polygon to the data source.

`void`

  [add](#add(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PolygonData`](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")`> polygons)`

Adds new polygons to the data source.

`void`

  [destroy](#destroy())`()`

Frees all internally used resources.

`void`

  [forEach](#forEach(com.here.sdk.mapview.datasource.PolygonDataSource.PolygonDataProcessor))`(`[`PolygonDataSource.PolygonDataProcessor`](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource")` processor)`

Iterates through all the polygons from the data source and passes them to the given processor, one by one.

`void`

  [removeAll](#removeAll())`()`

Removes all polygons from the data source.

`void`

  [removeIf](#removeIf(com.here.sdk.mapview.datasource.PolygonDataSource.PolygonDataProcessor))`(`[`PolygonDataSource.PolygonDataProcessor`](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource")` inspector)`

Iterates through all the polygons from the data source and passes them to the given inspector, one by one.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### add

public void add(@NonNull [PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource") polygon)

    Adds a new polygon to the data source.
Parameters:
    `polygon` -

    Polygon to add.

### add

public void add(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PolygonData](sdk-for-android-explore-api-reference-latestpolygondata "class in com.here.sdk.mapview.datasource")\> polygons)

    Adds new polygons to the data source.
Parameters:
    `polygons` -

    Polygons to add.

### removeAll

public void removeAll()

    Removes all polygons from the data source.

### forEach

public void forEach(@NonNull [PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource") processor)

    Iterates through all the polygons from the data source and passes them to the given processor, one by one. The processor can update the polygon data.

    The iteration stops after all polygons have been processed or the processor returns false from the process call.
Parameters:
    `processor` -

    Polygon processor.

### removeIf

public void removeIf(@NonNull [PolygonDataSource.PolygonDataProcessor](sdk-for-android-explore-api-reference-latestpolygondatasource-polygondataprocessor "interface in com.here.sdk.mapview.datasource") inspector)

    Iterates through all the polygons from the data source and passes them to the given inspector, one by one. All polygons for which the inspector returns `true` get removed from the data source. The inspector cannot update the polygon data.
Parameters:
    `inspector` -

    Polygon data processor.

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
