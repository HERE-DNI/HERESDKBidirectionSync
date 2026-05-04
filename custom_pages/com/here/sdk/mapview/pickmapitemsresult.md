---
title: "PickMapItemsResult (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestpickmapitemsresult"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class PickMapItemsResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.PickMapItemsResult
------------------------------------------------------------------------
public final class PickMapItemsResult extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Carries results from the picking of map items on the map scene.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarkerCluster.Grouping`](sdk-for-android-explore-api-reference-latestmapmarkercluster-grouping "class in com.here.sdk.mapview")`>`

  [getClusteredMarkers](#getClusteredMarkers())`()`

Gets list of clustered marker groups at the location of picking.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`>`

  [getMarkers](#getMarkers())`()`

Gets list of markers at the location of picking.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker3D`](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")`>`

  [getMarkers3d](#getMarkers3d())`()`

Gets list of 3d markers at the location of picking.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapPolygon`](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")`>`

  [getPolygons](#getPolygons())`()`

Gets list of polygons at the location of picking.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapPolyline`](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")`>`

  [getPolylines](#getPolylines())`()`

Gets list of polylines at the location of picking.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### getClusteredMarkers

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarkerCluster.Grouping](sdk-for-android-explore-api-reference-latestmapmarkercluster-grouping "class in com.here.sdk.mapview")\> getClusteredMarkers()

    Gets list of clustered marker groups at the location of picking.
Returns:
    List of marker groups (represented by a single cluster marker) or individual markers belonging to a cluster at the location of picking.

### getMarkers

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> getMarkers()

    Gets list of markers at the location of picking.
Returns:
    List of markers at the location of picking.

### getMarkers3d

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker3D](sdk-for-android-explore-api-reference-latestmapmarker3d "class in com.here.sdk.mapview")\> getMarkers3d()

    Gets list of 3d markers at the location of picking.
Returns:
    List of 3d markers at the location of picking.

### getPolylines

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapPolyline](sdk-for-android-explore-api-reference-latestmappolyline "class in com.here.sdk.mapview")\> getPolylines()

    Gets list of polylines at the location of picking.
Returns:
    List of polylines at the location of picking.

### getPolygons

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapPolygon](sdk-for-android-explore-api-reference-latestmappolygon "class in com.here.sdk.mapview")\> getPolygons()

    Gets list of polygons at the location of picking.
Returns:
    List of polygons at the location of picking.
