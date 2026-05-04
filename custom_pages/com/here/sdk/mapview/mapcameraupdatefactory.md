---
title: "MapCameraUpdateFactory (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmapcameraupdatefactory"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapCameraUpdateFactory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapCameraUpdateFactory
------------------------------------------------------------------------
public final class MapCameraUpdateFactory extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
Factory for creating MapCameraUpdate to change map's camera.

For some factory methods you can apply an additional padding in pixels by setting a `viewRectangle` parameter based on the current size of the map view:

    int leftPaddingInPixels = 5;
     int rightPaddingInPixels = 5;
     int topPaddingInPixels = 5;
     int bottomPaddingInPixels = 5;
     int horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels;
     int verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels;

     Point2D origin = new Point2D(leftPaddingInPixels, topPaddingInPixels);
     Size2D sizeInPixels = new Size2D(mapView.getWidth() - horizontalPaddingInPixels, mapView.getHeight() - verticalPaddingInPixels);
     Rectangle2D paddedViewRectangle = new Rectangle2D(origin, sizeInPixels);

The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates also the top-left corner of the map's viewport.

## Method Summary

  All Methods
  Static Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  `static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [compositeUpdate](#compositeUpdate(java.util.List))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")`> mapCameraUpdates)`

Creates a composite camera update from a list of camera updates.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoBox))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` target)`

Creates an update to look at the given geo-box, preserving current orientation and zooming at the center of viewport.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Rectangle2D))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewRectangle)`

Create an update to look at the given geo-box and fit it inside the given rectangle.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoBox,com.here.sdk.core.Rectangle2D))`(`[`GeoBox`](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core")` target, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewRectangle)`

Creates an update to look at the given geo-box and fit it inside the given rectangle, preserving current orientation and zooming at the center of view rectangle.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinatesUpdate))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target)`

Creates an update to position the map camera to look at the given target, preserving the current orientation at look-at target and map measure.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation)`

Creates an update to position the map camera to look at the given target with the given orientation preserving the current map measure (zoom level/distance/scale) Any target or orientation sub-element value that is not finite will be excluded from the update.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` measure)`

Creates an update to position the map camera to look at the given target with the given orientation and map measure.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.core.GeoOrientationUpdate,java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.mapview.MapMeasure,com.here.sdk.mapview.MapMeasure))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> points, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewRectangle, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` minMeasure, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` maxMeasure)`

Creates an update to position the camera to look at the given target with the given orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(com.here.sdk.core.GeoCoordinatesUpdate,com.here.sdk.mapview.MapMeasure))`(`[`GeoCoordinatesUpdate`](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core")` target, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` measure)`

Creates an update to position the map camera to look at the given target with the given map measure preserving the current orientation at look-at target.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookAt](#lookAt(java.util.List,com.here.sdk.core.Rectangle2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure))`(`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)`<`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")`> points, `[`Rectangle2D`](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core")` viewRectangle, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` measureLimit)`

Create an update to look at the given geo locations and fit them inside the given rectangle, in accordance with a map measure limit.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookToMatch](#lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoPoint, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewPoint)`

Creates an update to position the map camera to look at the map with the given geo point located at the given view point.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [lookToMatch](#lookToMatch(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.Point2D,com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.mapview.MapMeasure))`(`[`GeoCoordinates`](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")` geoPoint, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` viewPoint, `[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` orientation, `[`MapMeasure`](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview")` measure)`

Creates an update to position the map camera to look at the map with the given orientation and map measure and with the given geo point located at the given view point.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [orbitBy](#orbitBy(com.here.sdk.core.GeoOrientationUpdate,com.here.sdk.core.Point2D))`(`[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` delta, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [panBy](#panBy(double,double))`(double xOffset, double yOffset)`

Creates an update to pan map camera over the map by the specified number of pixels in the x and y direction starting from current principal point position.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [rotateBy](#rotateBy(com.here.sdk.core.GeoOrientationUpdate))`(`[`GeoOrientationUpdate`](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core")` delta)`

Creates an update to change map camera orientation by specified geodetic orientation delta.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [setNormalizedPrincipalPoint](#setNormalizedPrincipalPoint(com.here.sdk.core.Anchor2D))`(`[`Anchor2D`](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core")` principalPoint)`

Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is (0.5, 0.5)).

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [setPrincipalPoint](#setPrincipalPoint(com.here.sdk.core.Point2D))`(`[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` principalPoint)`

Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is the center of the view).

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [setVerticalFieldOfView](#setVerticalFieldOfView(double))`(double verticalFieldOfView)`

Creates an update to change the vertical field of view of the map camera.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [zoomBy](#zoomBy(double,com.here.sdk.core.Point2D))`(double factor, `[`Point2D`](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core")` origin)`

Creates an update to zoom map camera by a given factor preserving a given focus point.

`static `[`MapCameraUpdate`](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")

  [zoomTo](#zoomTo(double))`(double zoomLevel)`

Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Method Details

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target)

    Creates an update to position the map camera to look at the given target, preserving the current orientation at look-at target and map measure.

    Any target sub-element value that is not finite will be excluded from the update.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The look-at target position in geodetic coordinates, altitude is ignored, the target is considered to be located on the ground.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation)

    Creates an update to position the map camera to look at the given target with the given orientation preserving the current map measure (zoom level/distance/scale) Any target or orientation sub-element value that is not finite will be excluded from the update.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The look-at target position in geodetic coordinates.

    `orientation` -

    Geodetic orientation at look-at target.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") measure)

    Creates an update to position the map camera to look at the given target with the given map measure preserving the current orientation at look-at target. Any target sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The look-at target position in geodetic coordinates.

    `measure` -

    The desired map measure.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") measure)

    Creates an update to position the map camera to look at the given target with the given orientation and map measure. Any target or orientation sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The look-at target position in geodetic coordinates.

    `orientation` -

    Geodetic orientation at look-at target.

    `measure` -

    The desired map measure.

    Returns:
    MapCameraUpdate instance.

### lookToMatch

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookToMatch(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoPoint, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewPoint, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") measure)

    Creates an update to position the map camera to look at the map with the given orientation and map measure and with the given geo point located at the given view point.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.
Parameters:
    `geoPoint` -

    The geo point that will be matched to the given view point. Note: the geo point will differ from the look at target of the camera. After this update the camera will still look at the principal point and therefore the look at target will be different from the geo point, since the geo point will correspond to the given view point and the look at target will correspond to the principal point. Look at target and the geo point will be identical only if the given view point is identical to the principal point.

    `viewPoint` -

    View point coordinates in pixels.

    `orientation` -

    Geodetic orientation at look-at target.

    `measure` -

    The desired map measure.

    Returns:
    MapCameraUpdate instance.

### lookToMatch

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookToMatch(@NonNull [GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core") geoPoint, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") viewPoint)

    Creates an update to position the map camera to look at the map with the given geo point located at the given view point. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `geoPoint` -

    The geo point that will be matched to the given view point. Note: the geo point will differ from the look at target of the camera. After this update the camera will still look at the principal point and therefore the look at target will be different from the geo point, since the geo point will correspond to the given view point and the look at target will correspond to the principal point. Look at target and the geo point will be identical only if the given view point is identical to the principal point.

    `viewPoint` -

    View point coordinates in pixels.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> points, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewRectangle, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") measureLimit)

    Create an update to look at the given geo locations and fit them inside the given rectangle, in accordance with a map measure limit.

    If the provided `points` list is empty, no update will be applied to the camera.

    If the `viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `viewRectangle`. Thus, no padding will be applied. A `viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

    All `viewRectangle` values need to be finite to be considered as valid. If measure limit is not valid, no update will be applied to the map camera.

    The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `points` -

    Array of points in geodetic space that should be visible inside the given view rectangle.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.

    `orientation` -

    Geodetic orientation at the new calculated target point.

    `measureLimit` -

    Map measure limit:

    - as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters. The map camera should not be positioned closer to the center of view rectangle than this.
    - as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for the calculated lookAt target point. Can be used to not zoom closer than a given level.
    - as scale: the minimum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the center of view rectangle in meters. This is not the scale for the calculated lookAt target point.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoCoordinatesUpdate](sdk-for-android-explore-api-reference-latestgeocoordinatesupdate "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[GeoCoordinates](sdk-for-android-explore-api-reference-latestgeocoordinates "class in com.here.sdk.core")\> points, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewRectangle, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") minMeasure, @NonNull [MapMeasure](sdk-for-android-explore-api-reference-latestmapmeasure "class in com.here.sdk.mapview") maxMeasure)

    Creates an update to position the camera to look at the given target with the given orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle. Such position update can possibly not be found.

    Any target or orientation sub-element value that is not finite will be excluded from the update.

    If the provided `points` list is empty, no update will be applied to the map camera.

    If the `viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `viewRectangle`. Thus, no padding will be applied. A `viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

    If map measures are not valid, no update will be applied to the map camera.

    The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    The look-at target position in geodetic coordinates.

    `orientation` -

    Geodetic orientation at look-at target.

    `points` -

    Array of points in geodetic space that should be visible inside the given view rectangle.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates inside which the geographical points are displayed.

    `minMeasure` -

    Minimum map measure:

    - as distance: the minimum distance from map camera to earth surface at the look-at target in meters. The map camera should not be positioned closer to target than this.
    - as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters. Can be used to not zoom closer than a given level.
    - as scale: the minimum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters.

    `maxMeasure` -

    Maximum map measure:

    - as distance: the maximum distance from map camera to earth surface at the look-at target in meters. The map camera should not be positioned further from target than this.
    - as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters. Can be used to not zoom further than a given level.
    - as scale: the maximum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") target, @NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") orientation, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewRectangle)

    Create an update to look at the given geo-box and fit it inside the given rectangle.

    If geoBox is not valid, no update will be applied to the map camera.

    If the `viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `viewRectangle`. Thus, no padding will be applied. A `viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

    All `viewRectangle` values need to be finite to be considered as valid.

    In cases where it is not possible to find a solution for the given parameters, the resulting MapCameraUpdate will not change the map camera.

    The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    Geodetic box that should be visible inside the given view rectangle.

    `orientation` -

    Geodetic orientation at the target point.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") target, @NonNull [Rectangle2D](sdk-for-android-explore-api-reference-latestrectangle2d "class in com.here.sdk.core") viewRectangle)

    Creates an update to look at the given geo-box and fit it inside the given rectangle, preserving current orientation and zooming at the center of view rectangle.

    If geoBox is not valid, no update will be applied to the map camera.

    If the `viewRectangle` parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as `viewRectangle`. Thus, no padding will be applied. A `viewRectangle` is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.

    In cases where it is not possible to find a solution for the given parameters, the resulting MapCameraUpdate will not change the map camera.

    The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    Geodetic box that should be visible inside the given view rectangle.

    `viewRectangle` -

    View rectangle in viewport pixel coordinates.

    Returns:
    MapCameraUpdate instance.

### lookAt

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") lookAt(@NonNull [GeoBox](sdk-for-android-explore-api-reference-latestgeobox "class in com.here.sdk.core") target)

    Creates an update to look at the given geo-box, preserving current orientation and zooming at the center of viewport.

    If geoBox is not valid, no update will be applied to the map camera.

    The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.
Parameters:
    `target` -

    Geodetic box that should be visible inside the viewport rectangle.

    Returns:
    MapCameraUpdate instance.

### panBy

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") panBy(double xOffset, double yOffset)

    Creates an update to pan map camera over the map by the specified number of pixels in the x and y direction starting from current principal point position.
Parameters:
    `xOffset` -

    X offset in pixels

    `yOffset` -

    Y offset in pixels

    Returns:
    MapCameraUpdate instance.

### orbitBy

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") orbitBy(@NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") delta, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta. If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.

    Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].
Parameters:
    `delta` -

    Geodetic orientation delta update.

    `origin` -

    Screen pixel origin of rotation.

    Returns:
    MapCameraUpdate instance.

### rotateBy

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") rotateBy(@NonNull [GeoOrientationUpdate](sdk-for-android-explore-api-reference-latestgeoorientationupdate "class in com.here.sdk.core") delta)

    Creates an update to change map camera orientation by specified geodetic orientation delta. Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].
Parameters:
    `delta` -

    Geodetic orientation delta update.

    Returns:
    MapCameraUpdate instance.

### zoomBy

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") zoomBy(double factor, @NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") origin)

    Creates an update to zoom map camera by a given factor preserving a given focus point.

    Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out, which moves map camera further.

    If factor is zero, negative or not finite, no update will be applied to the map camera.

    If the focusPoint is not inside the viewport bounds, then the current principal point will be used.
Parameters:
    `factor` -

    Zooming factor.

    `origin` -

    Pixel location on the screen to use as zoom origin.

    Returns:
    MapCameraUpdate instance.

### zoomTo

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") zoomTo(double zoomLevel)

    Creates an update to move map camera's viewpoint to a particular zoom level by adjusting its position.

    If zoomLevel is not finite, no update will be applied to the map camera.
Parameters:
    `zoomLevel` -

    The desired zoom level.

    Returns:
    MapCameraUpdate instance.

### setPrincipalPoint

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") setPrincipalPoint(@NonNull [Point2D](sdk-for-android-explore-api-reference-latestpoint2d "class in com.here.sdk.core") principalPoint)

    Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is the center of the view). Point values are in screen coordinates and values that fall outside of the viewport, are clamped. (0,0) is top left of the viewport.
Parameters:
    `principalPoint` -

    Principal point in absolute viewport pixel coordinates.

    Returns:
    MapCameraUpdate instance.

### setNormalizedPrincipalPoint

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") setNormalizedPrincipalPoint(@NonNull [Anchor2D](sdk-for-android-explore-api-reference-latestanchor2d "class in com.here.sdk.core") principalPoint)

    Creates an update to change the map camera's principal point (where the view vector intersects the image plane - default is (0.5, 0.5)). Point values are in normalized screen coordinates.

    If the principalPoint is outside \[0,1\] interval, it is clamped. (0,0) is top left of the viewport, (1,1) is bottom right.
Parameters:
    `principalPoint` -

    Principal point in normalized screen coordinates.

    Returns:
    MapCameraUpdate instance.

### setVerticalFieldOfView

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") setVerticalFieldOfView(double verticalFieldOfView)

    Creates an update to change the vertical field of view of the map camera.

    If verticalFieldOfView is not finite, no update will be applied to the map camera.

    If the verticalFieldOfView is outside \[1, 150\] interval, it is clamped.
Parameters:
    `verticalFieldOfView` -

    Vertical field of view in degrees.

    Returns:
    MapCameraUpdate instance.

### compositeUpdate

@NonNull public static [MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview") compositeUpdate(@NonNull [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html)\<[MapCameraUpdate](sdk-for-android-explore-api-reference-latestmapcameraupdate "class in com.here.sdk.mapview")\> mapCameraUpdates) throws [MapCameraUpdate.InstantiationException](sdk-for-android-explore-api-reference-latestmapcameraupdate-instantiationexception "class in com.here.sdk.mapview")

    Creates a composite camera update from a list of camera updates. The result update will be equivalent to executing all given updates sequentially in the order they were provided.

    MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal when trying to apply such animations.
Parameters:
    `mapCameraUpdates` -

    List of MapCamera updates.

    Returns:
    MapCameraUpdate instance.

    Throws:
    [`MapCameraUpdate.InstantiationException`](sdk-for-android-explore-api-reference-latestmapcameraupdate-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.
