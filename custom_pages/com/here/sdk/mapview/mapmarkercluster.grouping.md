---
title: "MapMarkerCluster.Grouping (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarkercluster-grouping"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarkerCluster.Grouping

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapMarkerCluster.Grouping
Enclosing class:
[MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapMarkerCluster.Grouping extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
Represents a group of map markers belonging to a cluster.

It contains a list of map markers grouped on map view under single icon of marker cluster or single map marker entry for markers being part of cluster but spread enough not to be grouped.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`>`

  [markers](#markers)

List of map markers grouped on map view under map marker cluster icon.

[`MapMarkerCluster`](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")

  [parent](#parent)

Map marker cluster that entries in [`markers`](#markers) belong to.

## Constructor Summary

Constructors

Constructor

  Description

  [Grouping](#%3Cinit%3E(java.util.List,com.here.sdk.mapview.MapMarkerCluster))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`> markers, `[`MapMarkerCluster`](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")` parent)`

Creates a new instance.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### markers

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> markers

    List of map markers grouped on map view under map marker cluster icon.

### parent

@NonNull public [MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview") parent

    Map marker cluster that entries in [`markers`](#markers) belong to.

## Constructor Details

  - (java.util.List,com.here.sdk.mapview.MapMarkerCluster)" class="section detail">

### Grouping

public Grouping(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> markers, @NonNull [MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview") parent)

    Creates a new instance.
Parameters:
    `markers` -

    List of map markers grouped on map view under map marker cluster icon.

    `parent` -

    Map marker cluster that entries in [`markers`](#markers) belong to.
