---
title: "MapMarkerCluster (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarkercluster"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarkerCluster

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapMarkerCluster
------------------------------------------------------------------------
public final class MapMarkerCluster extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Groups map markers and enables their clustering to reduce visual clutter when there are many of them in a small area.

The markers that are close to each other are replaced by a single cluster marker. Cluster groups are generated based on geographical distance between objects, not based on screen space collision. Hence it is possible, that cluster markers can overlap.

The markers can be added to a cluster or to a scene, but not to both. To display the cluster on the map, add it to the scene using [`MapScene.addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)`](sdk-for-android-explore-api-reference-latestmapscene#addMapMarkerCluster(com.here.sdk.mapview.MapMarkerCluster)). The display of a cluster is only guaranteed in case its origin is within the viewport. At the moment, this is a known limitation that mostly affects clusters which are visually large and cover a sizeable part of the viewport.

Markers part of the cluster with opacity set to zero are still on the map and are considered for picking and clustering.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static final class `

  [MapMarkerCluster.CounterStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-counterstyle)

Styling options for a marker cluster which is represented by the marker count as a text.

`static final class `

  [MapMarkerCluster.Grouping](sdk-for-android-explore-api-reference-latestmapmarkercluster-grouping)

Represents a group of map markers belonging to a cluster.

`static final class `

  [MapMarkerCluster.ImageStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle)

This class specifies the visual appearance of a cluster marker.

## Constructor Summary

Constructors

Constructor

  Description

  [MapMarkerCluster](#%3Cinit%3E(com.here.sdk.mapview.MapMarkerCluster.ImageStyle))`(`[`MapMarkerCluster.ImageStyle`](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle "class in com.here.sdk.mapview")` imageStyle)`

Creates a new instance of a map marker cluster which is represented as an image.

[MapMarkerCluster](#%3Cinit%3E(com.here.sdk.mapview.MapMarkerCluster.ImageStyle,com.here.sdk.mapview.MapMarkerCluster.CounterStyle))`(`[`MapMarkerCluster.ImageStyle`](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle "class in com.here.sdk.mapview")` imageStyle, `[`MapMarkerCluster.CounterStyle`](sdk-for-android-explore-api-reference-latestmapmarkercluster-counterstyle "class in com.here.sdk.mapview")` counterStyle)`

Creates a new instance of a map marker cluster which is represented as an image along with a counter showing how many markers are actually grouped under particular cluster icon.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `void`

  [addMapMarker](#addMapMarker(com.here.sdk.mapview.MapMarker))`(`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")` marker)`

Adds a map marker to this cluster.

`void`

  [addMapMarkers](#addMapMarkers(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`> markers)`

Adds a list of map markers to this cluster.

[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`>`

  [getMarkers](#getMarkers())`()`

Returns the list of map markers which currently belong to this cluster.

`double`

  [getOpacity](#getOpacity())`()`

Gets the current opacity of the marker cluster image.

`void`

  [removeAllMapMarkers](#removeAllMapMarkers())`()`

Removes all map markers from this cluster.

`void`

  [removeMapMarker](#removeMapMarker(com.here.sdk.mapview.MapMarker))`(`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")` marker)`

Removes a map marker from this cluster.

`void`

  [removeMapMarkers](#removeMapMarkers(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapMarker`](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")`> markers)`

Removes a list of map markers from this cluster.

`void`

  [setOpacity](#setOpacity(double))`(double value)`

Sets the opacity of the marker cluster image.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - (com.here.sdk.mapview.MapMarkerCluster.ImageStyle)" class="section detail">

### MapMarkerCluster

public MapMarkerCluster(@NonNull [MapMarkerCluster.ImageStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle "class in com.here.sdk.mapview") imageStyle)

    Creates a new instance of a map marker cluster which is represented as an image.

    Any modification to object passed as `imageStyle` after creation of `MapMarkerCluster` does not have any effect.
Parameters:
    `imageStyle` -

    The visual representation for the cluster.
- (com.here.sdk.mapview.MapMarkerCluster.ImageStyle,com.here.sdk.mapview.MapMarkerCluster.CounterStyle)" class="section detail">

### MapMarkerCluster

public MapMarkerCluster(@NonNull [MapMarkerCluster.ImageStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle "class in com.here.sdk.mapview") imageStyle, @NonNull [MapMarkerCluster.CounterStyle](sdk-for-android-explore-api-reference-latestmapmarkercluster-counterstyle "class in com.here.sdk.mapview") counterStyle)

    Creates a new instance of a map marker cluster which is represented as an image along with a counter showing how many markers are actually grouped under particular cluster icon.

    Any modification to `imageStyle` or `counterStyle` after creation of `MapMarkerCluster` does not have any effect.
Parameters:
    `imageStyle` -

    Describes the visual appearance of cluster icon.

    `counterStyle` -

    Describes the appearance of marker count label.

## Method Details

### addMapMarker

public void addMapMarker(@NonNull [MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") marker)

    Adds a map marker to this cluster. Adding a marker which is already part of the cluster or which was already added to the map scene has no effect.
Parameters:
    `marker` -

    The marker.

### addMapMarkers

public void addMapMarkers(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> markers)

    Adds a list of map markers to this cluster.

    Markers which are already part of the cluster or which were already added to the map scene will be ignored.
Parameters:
    `markers` -

    The list of markers.

### removeMapMarker

public void removeMapMarker(@NonNull [MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview") marker)

    Removes a map marker from this cluster.

    Removing a marker which is not part of this cluster has no effect.
Parameters:
    `marker` -

    The marker.

### removeMapMarkers

public void removeMapMarkers(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> markers)

    Removes a list of map markers from this cluster.

    Removing markers which are not part of this cluster has no effect.
Parameters:
    `markers` -

    The list of markers.

### removeAllMapMarkers

public void removeAllMapMarkers()

    Removes all map markers from this cluster.

### getMarkers

@NonNull public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapMarker](sdk-for-android-explore-api-reference-latestmapmarker "class in com.here.sdk.mapview")\> getMarkers()

    Returns the list of map markers which currently belong to this cluster.

    Modifying the list has no effect on the marker cluster.
Returns:
    The list of map markers which currently belong to this cluster.

### getOpacity

public double getOpacity()

    Gets the current opacity of the marker cluster image.
Returns:
    Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.

### setOpacity

public void setOpacity(double value)

    Sets the opacity of the marker cluster image.

    Provided value is clamped in range \[0.0, 1.0\]. Default value is 1.0 which means marker cluster is displayed with the default opacity of the image.

    Marker clusters with opacity value set to 0.0 are still on the map and are considered for picking.

    Markers part of cluster will use their respective opacity when not displayed as a cluster icon.
Parameters:
    `value` -

    Opacity is the factor which is applied to the alpha channel of the image used for marker cluster.
