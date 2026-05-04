---
title: "PointDataSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpointdatasource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PointDataSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.PointDataSource
------------------------------------------------------------------------
public final class PointDataSource extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Point data source allows the rendering engine access to the user provided geographical locations and their attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [PointDataSource.PointDataProcessor](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor)

Called for each point, allowing inspection, removal or update of coordinates and attributes.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [add](#add(com.here.sdk.mapview.datasource.PointData))`(`[`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")` point)`

Adds a new point to the data source.

`void`

  [add](#add(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`PointData`](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")`> points)`

Adds new points to the data source.

`void`

  [destroy](#destroy())`()`

Frees all internally used resources.

`void`

  [forEach](#forEach(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor))`(`[`PointDataSource.PointDataProcessor`](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource")` processor)`

Iterates through all the points from the data source and passes them to the given processor, one by one.

`void`

  [removeAll](#removeAll())`()`

Removes all points from the data source.

`void`

  [removeIf](#removeIf(com.here.sdk.mapview.datasource.PointDataSource.PointDataProcessor))`(`[`PointDataSource.PointDataProcessor`](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource")` processor)`

Iterates through all the points from the data source and passes them to the given inspector, one by one.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### add

public void add(@NonNull [PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource") point)

    Adds a new point to the data source. Altitude of the point coordinates is ignored.
Parameters:
    `point` -

    Point to be added.

### add

public void add(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[PointData](sdk-for-android-explore-api-reference-latestpointdata "class in com.here.sdk.mapview.datasource")\> points)

    Adds new points to the data source. Altitude of the points coordinates is ignored.
Parameters:
    `points` -

    Point positions.

### removeAll

public void removeAll()

    Removes all points from the data source.

### forEach

public void forEach(@NonNull [PointDataSource.PointDataProcessor](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource") processor)

    Iterates through all the points from the data source and passes them to the given processor, one by one. The processor can update the point data.

    The iteration stops after all points have been processed or the processor returns false from the process call.
Parameters:
    `processor` -

    Point data processor.

### removeIf

public void removeIf(@NonNull [PointDataSource.PointDataProcessor](sdk-for-android-explore-api-reference-latestpointdatasource-pointdataprocessor "interface in com.here.sdk.mapview.datasource") processor)

    Iterates through all the points from the data source and passes them to the given inspector, one by one. All points for which the inspector returns `true` get removed from the data source. The inspector cannot update the point data.
Parameters:
    `processor` -

    Point data processor.

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
