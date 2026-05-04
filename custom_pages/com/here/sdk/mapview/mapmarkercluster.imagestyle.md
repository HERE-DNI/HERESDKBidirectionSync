---
title: "MapMarkerCluster.ImageStyle (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapmarkercluster-imagestyle"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapMarkerCluster.ImageStyle

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
com.here.sdk.mapview.MapMarkerCluster.ImageStyle
Enclosing class:
[MapMarkerCluster](sdk-for-android-explore-api-reference-latestmapmarkercluster "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static final class MapMarkerCluster.ImageStyle extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
This class specifies the visual appearance of a cluster marker.

## Field Summary

Fields

Modifier and Type

  Field

  Description

  `final `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

  [anchor](#anchor)

The anchor point for the marker image which specifies the position offset relative to the cluster's position.

`final `[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")

  [image](#image)

The map image for the cluster marker.

## Constructor Summary

Constructors

Constructor

  Description

  [ImageStyle](#%3Cinit%3E(com.here.sdk.mapview.MapImage))`(`[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image)`

Creates a marker cluster image representation with default anchor.

[ImageStyle](#%3Cinit%3E(com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D))`(`[`MapImage`](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview")` image, `[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchor)`

Creates a cluster marker image style using a map image with anchor.

## Method Summary

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Field Details

### image

@NonNull public final [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image

    The map image for the cluster marker.

### anchor

@NonNull public final [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor

    The anchor point for the marker image which specifies the position offset relative to the cluster's position.

## Constructor Details

  - (com.here.sdk.mapview.MapImage,com.here.sdk.core.Anchor2D)" class="section detail">

### ImageStyle

public ImageStyle(@NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image, @NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchor)

    Creates a cluster marker image style using a map image with anchor.

    The anchor is a way of specifying position offset relative to image's dimensions on the screen. For example, (0, 0) places the top-left corner of the image at the cluster's position. (1, 1) would place the bottom-right corner of the image at the cluster's position.
Parameters:
    `image` -

    The map image for the cluster marker.

    `anchor` -

    The anchor point for the marker image which specifies the position offset relative to the cluster's position.
- (com.here.sdk.mapview.MapImage)" class="section detail">

### ImageStyle

public ImageStyle(@NonNull [MapImage](sdk-for-android-explore-api-reference-latestmapimage "class in com.here.sdk.mapview") image)

    Creates a marker cluster image representation with default anchor.
Parameters:
    `image` -

    The map image for the cluster marker.
