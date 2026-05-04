---
title: "MapView.ViewPin (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapview-viewpin"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface MapView.ViewPin

Enclosing class:
[MapView](sdk-for-android-explore-api-reference-latestmapview "class in com.here.sdk.mapview")

------------------------------------------------------------------------
public static interface MapView.ViewPin
A ViewPin is used to display Android views at a fixed location on the map.

The pinned view will automatically be repositioned on the screen as the map moves. There is more performance overhead involved in positioning a pinned view as compared to a map marker, so for use cases which only require static images, markers should be used.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")

  [getAnchorPoint](#getAnchorPoint())`()`

Gets anchor point for this instance.

[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")

  [getGeoCoordinates](#getGeoCoordinates())`()`

Returns the current GeoCoordinates on the map.

`void`

  [setAnchorPoint](#setAnchorPoint(com.here.sdk.core.Anchor2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` anchorPoint)`

Sets an anchor point for this instance.

`void`

  [setGeoCoordinates](#setGeoCoordinates(com.here.sdk.core.GeoCoordinates))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoCoordinates)`

Sets the GeoCoordinates on the map.

`void`

  [unpin](#unpin())`()`

Removes the view from the `MapView` it was pinned to.

## Method Details

### unpin

void unpin()

    Removes the view from the `MapView` it was pinned to.

### getGeoCoordinates

[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") getGeoCoordinates()

    Returns the current GeoCoordinates on the map.
Returns:
    The current GeoCoordinates.

### setGeoCoordinates

void setGeoCoordinates(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoCoordinates)

    Sets the GeoCoordinates on the map.
    The altitude component of the coordinates, if set, is interpreted as above sea level. When not set, the coordinates are interpreted as at ground level.
Parameters:
    `geoCoordinates` - Desired GeoCoordinates for this view pin.

### setAnchorPoint

void setAnchorPoint(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") anchorPoint)

    Sets an anchor point for this instance.
    The anchor value has valid range from 0 to 1. Zero (0) for x and y means the view pin's upper left corner is located at the geographical location, whereas one (1) for x and y means that the pin will have its right bottom corner attached to the geographical location instead. The default value used is 0.5, 0.5, causing the view to be centered.
Parameters:
    `anchorPoint` - A `Anchor2D` relative to the top-left corner of the `ViewPin`.

### getAnchorPoint

[Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") getAnchorPoint()

    Gets anchor point for this instance.
Returns:
    anchorPoint A `Anchor2D` relative to the top-left corner of the ` ViewPin`.
