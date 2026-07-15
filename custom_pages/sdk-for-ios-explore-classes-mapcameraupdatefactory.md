---
title: "MapCameraUpdateFactory Class Reference"
slug: "sdk-for-ios-explore-classes-mapcameraupdatefactory"
---

# MapCameraUpdateFactory

<div class="declaration">

<div class="language">

``` highlight
public class MapCameraUpdateFactory
```

``` highlight
extension MapCameraUpdateFactory: NativeBase
```

``` highlight
extension MapCameraUpdateFactory: Hashable
```

</div>

</div>

Factory for creating MapCameraUpdate to change map’s camera.

For some factory methods you can apply an additional padding in pixels by setting a `viewRectangle` parameter based on the current size of the map view:

``` highlight
let leftPaddingInPixels = 5 let rightPaddingInPixels = 5 let topPaddingInPixels = 5 let bottomPaddingInPixels = 5 let horizontalPaddingInPixels = leftPaddingInPixels + rightPaddingInPixels let verticalPaddingInPixels = topPaddingInPixels + bottomPaddingInPixels let origin = Point2D ( leftPaddingInPixels , topPaddingInPixels ) let sizeInPixels = Size2D ( width : mapView . viewportSize . width - horizontalPaddingInPixels , height : mapView . viewportSize . height - verticalPaddingInPixels ) let paddedViewRectangle = Rectangle2D ( origin : origin , size : sizeInPixels )
```

</pre>

The origin indicates the top-left corner of the rectangle. An origin of (0, 0) indicates also the top-left corner of the map’s viewport.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      lookAt(point: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the map camera to look at the given target, preserving the current orientation at look-at target and map measure.

  Any target sub-element value that is not finite will be excluded from the update.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( point target : GeoCoordinatesUpdate ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>The look-at target position in geodetic coordinates, altitude is ignored, the target is considered to be located on the ground.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(point: orientation: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the map camera to look at the given target with the given orientation preserving the current map measure (zoom level/distance/scale) Any target or orientation sub-element value that is not finite will be excluded from the update.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( point target : GeoCoordinatesUpdate , orientation : GeoOrientationUpdate ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>The look-at target position in geodetic coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation at look-at target.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(point: measure: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the map camera to look at the given target with the given map measure preserving the current orientation at look-at target. Any target sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( point target : GeoCoordinatesUpdate , measure : MapMeasure ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>The look-at target position in geodetic coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>measure</code></em><code> </code></td>
  <td><div>
  <p>The desired map measure.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(point: orientation: measure: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the map camera to look at the given target with the given orientation and map measure. Any target or orientation sub-element value that is not finite will be excluded from the update. If the map measure is not valid, the current map camera distance to the target point is preserved.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( point target : GeoCoordinatesUpdate , orientation : GeoOrientationUpdate , measure : MapMeasure ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>The look-at target position in geodetic coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation at look-at target.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>measure</code></em><code> </code></td>
  <td><div>
  <p>The desired map measure.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookToMatch(point: viewPoint: orientation: measure: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the map camera to look at the map with the given orientation and map measure and with the given geo point located at the given view point.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookToMatch ( point geoPoint : GeoCoordinates , viewPoint : Point2D , orientation : GeoOrientationUpdate , measure : MapMeasure ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>geoPoint</code></em><code> </code></td>
  <td><div>
  <p>The geo point that will be matched to the given view point. Note: the geo point will differ from the look at target of the camera. After this update the camera will still look at the principal point and therefore the look at target will be different from the geo point, since the geo point will correspond to the given view point and the look at target will correspond to the principal point. Look at target and the geo point will be identical only if the given view point is identical to the principal point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewPoint</code></em><code> </code></td>
  <td><div>
  <p>View point coordinates in pixels.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation at look-at target.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>measure</code></em><code> </code></td>
  <td><div>
  <p>The desired map measure.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookToMatch(point: viewPoint: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the map camera to look at the map with the given geo point located at the given view point. Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookToMatch ( point geoPoint : GeoCoordinates , viewPoint : Point2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>geoPoint</code></em><code> </code></td>
  <td><div>
  <p>The geo point that will be matched to the given view point. Note: the geo point will differ from the look at target of the camera. After this update the camera will still look at the principal point and therefore the look at target will be different from the geo point, since the geo point will correspond to the given view point and the look at target will correspond to the principal point. Look at target and the geo point will be identical only if the given view point is identical to the principal point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewPoint</code></em><code> </code></td>
  <td><div>
  <p>View point coordinates in pixels.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(_: viewRectangle: orientation: measureLimit: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create an update to look at the given geo locations and fit them inside the given rectangle, in accordance with a map measure limit.

  If the provided

      MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).points

  list is empty, no update will be applied to the camera.
  </p>

  If the

      MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle

  parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as
      MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle

  . Thus, no padding will be applied. A
      MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle

  is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.
  </p>

  All

      MapCameraUpdateFactory.lookAt([GeoCoordinates], Rectangle2D, GeoOrientationUpdate, MapMeasure).viewRectangle

  values need to be finite to be considered as valid. If measure limit is not valid, no update will be applied to the map camera.
  </p>

  The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( _ points : [ GeoCoordinates ], viewRectangle : Rectangle2D , orientation : GeoOrientationUpdate , measureLimit : MapMeasure ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>points</code></em><code> </code></td>
  <td><div>
  <p>Array of points in geodetic space that should be visible inside the given view rectangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewRectangle</code></em><code> </code></td>
  <td><div>
  <p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation at the new calculated target point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>measureLimit</code></em><code> </code></td>
  <td><div>
  <p>Map measure limit:</p>
  <ul>
  <li>as distance: the minimum distance from map camera to earth surface at the center of the view rectangle in meters. The map camera should not be positioned closer to the center of view rectangle than this.</li>
  <li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the center of view rectangle in meters. This is not the zoom level for the calculated lookAt target point. Can be used to not zoom closer than a given level.</li>
  <li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the center of view rectangle in meters. This is not the scale for the calculated lookAt target point.</li>
  </ul>
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(_: orientation: points: viewRectangle: minMeasure: maxMeasure: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to position the camera to look at the given target with the given orientation and obeying map measure limits, so that the given geo locations are inside the given rectangle. Such position update can possibly not be found.

  Any target or orientation sub-element value that is not finite will be excluded from the update.

  If the provided

      MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).points

  list is empty, no update will be applied to the map camera.
  </p>

  If the

      MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).viewRectangle

  parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as
      MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).viewRectangle

  . Thus, no padding will be applied. A
      MapCameraUpdateFactory.lookAt(GeoCoordinatesUpdate, GeoOrientationUpdate, [GeoCoordinates], Rectangle2D, MapMeasure, MapMeasure).viewRectangle

  is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.
  </p>

  If map measures are not valid, no update will be applied to the map camera.

  The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( _ target : GeoCoordinatesUpdate , orientation : GeoOrientationUpdate , points : [ GeoCoordinates ], viewRectangle : Rectangle2D , minMeasure : MapMeasure , maxMeasure : MapMeasure ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>The look-at target position in geodetic coordinates.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation at look-at target.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>points</code></em><code> </code></td>
  <td><div>
  <p>Array of points in geodetic space that should be visible inside the given view rectangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewRectangle</code></em><code> </code></td>
  <td><div>
  <p>View rectangle in viewport pixel coordinates inside which the geographical points are displayed.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>minMeasure</code></em><code> </code></td>
  <td><div>
  <p>Minimum map measure:</p>
  <ul>
  <li>as distance: the minimum distance from map camera to earth surface at the look-at target in meters. The map camera should not be positioned closer to target than this.</li>
  <li>as zoom level: the maximum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters. Can be used to not zoom closer than a given level.</li>
  <li>as scale: the minimum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters.</li>
  </ul>
  </p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>maxMeasure</code></em><code> </code></td>
  <td><div>
  <p>Maximum map measure:</p>
  <ul>
  <li>as distance: the maximum distance from map camera to earth surface at the look-at target in meters. The map camera should not be positioned further from target than this.</li>
  <li>as zoom level: the minimum zoom level for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters. Can be used to not zoom further than a given level.</li>
  <li>as scale: the maximum scale for the new map camera state. Internally converted to minimum distance from map camera to earth surface at the look-at target in meters.</li>
  </ul>
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(area: orientation: viewRectangle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Create an update to look at the given geo-box and fit it inside the given rectangle.

  If geoBox is not valid, no update will be applied to the map camera.

  If the

      MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle

  parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as
      MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle

  . Thus, no padding will be applied. A
      MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle

  is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.
  </p>

  All

      MapCameraUpdateFactory.lookAt(GeoBox, GeoOrientationUpdate, Rectangle2D).viewRectangle

  values need to be finite to be considered as valid.
  </p>

  In cases where it is not possible to find a solution for the given parameters, the resulting MapCameraUpdate will not change the map camera.

  The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( area target : GeoBox , orientation : GeoOrientationUpdate , viewRectangle : Rectangle2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>Geodetic box that should be visible inside the given view rectangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation at the target point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewRectangle</code></em><code> </code></td>
  <td><div>
  <p>View rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(area: viewRectangle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to look at the given geo-box and fit it inside the given rectangle, preserving current orientation and zooming at the center of view rectangle.

  If geoBox is not valid, no update will be applied to the map camera.

  If the

      MapCameraUpdateFactory.lookAt(GeoBox, Rectangle2D).viewRectangle

  parameter is invalid, fully or partially outside the map view, then the entire map viewport will be used as
      MapCameraUpdateFactory.lookAt(GeoBox, Rectangle2D).viewRectangle

  . Thus, no padding will be applied. A
      MapCameraUpdateFactory.lookAt(GeoBox, Rectangle2D).viewRectangle

  is considered invalid, when its width or height are negative or zero, its origin coordinates (x, y) are invalid, when they are negative.
  </p>

  In cases where it is not possible to find a solution for the given parameters, the resulting MapCameraUpdate will not change the map camera.

  The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( area target : GeoBox , viewRectangle : Rectangle2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>Geodetic box that should be visible inside the given view rectangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewRectangle</code></em><code> </code></td>
  <td><div>
  <p>View rectangle in viewport pixel coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      lookAt(area: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to look at the given geo-box, preserving current orientation and zooming at the center of viewport.

  If geoBox is not valid, no update will be applied to the map camera.

  The altitude of the target points is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func lookAt ( area target : GeoBox ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>target</code></em><code> </code></td>
  <td><div>
  <p>Geodetic box that should be visible inside the viewport rectangle.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      panBy(xOffset: yOffset: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to pan map camera over the map by the specified number of pixels in the x and y direction starting from current principal point position.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func panBy ( xOffset : Double , yOffset : Double ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>xOffset</code></em><code> </code></td>
  <td><div>
  <p>X offset in pixels</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>yOffset</code></em><code> </code></td>
  <td><div>
  <p>Y offset in pixels</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      orbitBy(_: around: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to orbit map camera around a pixel origin by specified geodetic orientation delta. If the origin cannot be converted to geo coordinates, no update will be applied to the map camera.

  Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func orbitBy ( _ delta : GeoOrientationUpdate , around origin : Point2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>delta</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation delta update.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>origin</code></em><code> </code></td>
  <td><div>
  <p>Screen pixel origin of rotation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      rotateBy(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to change map camera orientation by specified geodetic orientation delta. Orientation elements that are not valid will be excluded from the update. Resulting bearing values are wrapped around degrees range \[0, 360\]. Resulting tilt values are clamped inside degrees range \[0, 180\]. Resulting roll values are wrapped around degrees range \[-180, 180\].

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func rotateBy ( _ delta : GeoOrientationUpdate ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>delta</code></em><code> </code></td>
  <td><div>
  <p>Geodetic orientation delta update.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      zoomBy(_: around: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to zoom map camera by a given factor preserving a given focus point.

  Values greater than 1 zoom in map camera, by moving it closer to the ground; less than 1 - zoom out, which moves map camera further.

  If factor is zero, negative or not finite, no update will be applied to the map camera.

  If the focusPoint is not inside the viewport bounds, then the current principal point will be used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func zoomBy ( _ factor : Double , around origin : Point2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>factor</code></em><code> </code></td>
  <td><div>
  <p>Zooming factor.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>origin</code></em><code> </code></td>
  <td><div>
  <p>Pixel location on the screen to use as zoom origin.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      zoomTo(zoomLevel: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to move map camera’s viewpoint to a particular zoom level by adjusting its position.

  If zoomLevel is not finite, no update will be applied to the map camera.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func zoomTo ( zoomLevel : Double ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>zoomLevel</code></em><code> </code></td>
  <td><div>
  <p>The desired zoom level.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      setPrincipalPoint(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to change the map camera’s principal point (where the view vector intersects the image plane - default is the center of the view). Point values are in screen coordinates and values that fall outside of the viewport, are clamped. (0,0) is top left of the viewport.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setPrincipalPoint ( _ principalPoint : Point2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>principalPoint</code></em><code> </code></td>
  <td><div>
  <p>Principal point in absolute viewport pixel coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      setNormalizedPrincipalPoint(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to change the map camera’s principal point (where the view vector intersects the image plane - default is (0.5, 0.5)). Point values are in normalized screen coordinates.

  If the principalPoint is outside \[0,1\] interval, it is clamped. (0,0) is top left of the viewport, (1,1) is bottom right.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setNormalizedPrincipalPoint ( _ principalPoint : Anchor2D ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>principalPoint</code></em><code> </code></td>
  <td><div>
  <p>Principal point in normalized screen coordinates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      setVerticalFieldOfView(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an update to change the vertical field of view of the map camera.

  If verticalFieldOfView is not finite, no update will be applied to the map camera.

  If the verticalFieldOfView is outside \[1, 150\] interval, it is clamped.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func setVerticalFieldOfView ( _ verticalFieldOfView : Double ) -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>verticalFieldOfView</code></em><code> </code></td>
  <td><div>
  <p>Vertical field of view in degrees.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

- <div>

      compositeUpdate(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a composite camera update from a list of camera updates. The result update will be equivalent to executing all given updates sequentially in the order they were provided.

  MapCameraAnimation instances derived from the MapCameraAnimationFactory and a composite camera update are not supported. An AnimationListener will receive an AnimationState.Cancelled signal when trying to apply such animations.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mapcameraupdate#/s:7heresdk15MapCameraUpdateC18InstantiationErrora">`MapCameraUpdate.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func compositeUpdate ( _ mapCameraUpdates : [ MapCameraUpdate ]) throws -> MapCameraUpdate
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>mapCameraUpdates</code></em><code> </code></td>
  <td><div>
  <p>List of MapCamera updates.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraUpdate instance.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

