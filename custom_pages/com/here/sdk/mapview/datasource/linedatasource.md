---
title: "LineDataSource (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestlinedatasource"
hidden: false
---

Package [com.here.sdk.mapview.datasource](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class LineDataSource

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.datasource.LineDataSource
------------------------------------------------------------------------
public final class LineDataSource extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Polyline data source allows the rendering engine access to the user provided polylines geometry and their attributes.

Polyline segments are rendered following the shortest path between their end vertices.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static interface `

  [LineDataSource.LineDataProcessor](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor)

Called for each line, allowing inspection, removal or update of coordinates and attributes.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [add](#add(com.here.sdk.mapview.datasource.LineData))`(`[`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")` line)`

Adds a new line to the data source.

`void`

  [add](#add(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`LineData`](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")`> lines)`

Adds new lines to the data source.

`void`

  [destroy](#destroy())`()`

Frees all internally used resources.

`void`

  [forEach](#forEach(com.here.sdk.mapview.datasource.LineDataSource.LineDataProcessor))`(`[`LineDataSource.LineDataProcessor`](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor "interface in com.here.sdk.mapview.datasource")` processor)`

Iterates through all the lines from the data source and passes them to the given processor, one by one.

`void`

  [removeAll](#removeAll())`()`

Removes all lines from the data source.

`void`

  [removeIf](#removeIf(com.here.sdk.mapview.datasource.LineDataSource.LineDataProcessor))`(`[`LineDataSource.LineDataProcessor`](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor "interface in com.here.sdk.mapview.datasource")` inspector)`

Iterates through all the lines from the data source and passes them to the given inspector, one by one.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### add

public void add(@NonNull [LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource") line)

    Adds a new line to the data source.
Parameters:
    `line` -

    Line to add.

### add

public void add(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[LineData](sdk-for-android-explore-api-reference-latestlinedata "class in com.here.sdk.mapview.datasource")\> lines)

    Adds new lines to the data source.
Parameters:
    `lines` -

    Lines to add.

### removeAll

public void removeAll()

    Removes all lines from the data source.

### forEach

public void forEach(@NonNull [LineDataSource.LineDataProcessor](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor "interface in com.here.sdk.mapview.datasource") processor)

    Iterates through all the lines from the data source and passes them to the given processor, one by one. The processor can update the line data. The iteration stops after all lines have been processed or the processor returns false from the process call.
Parameters:
    `processor` -

    Line processor.

### removeIf

public void removeIf(@NonNull [LineDataSource.LineDataProcessor](sdk-for-android-explore-api-reference-latestlinedatasource-linedataprocessor "interface in com.here.sdk.mapview.datasource") inspector)

    Iterates through all the lines from the data source and passes them to the given inspector, one by one. All lines for which the inspector returns `true` get removed from the data source. The inspector cannot update the line data.
Parameters:
    `inspector` -

    Line data processor.

### destroy

public void destroy()

    Frees all internally used resources. After calling this method, the object is not usable anymore.
