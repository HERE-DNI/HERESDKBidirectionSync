---
title: "MapCamera Class Reference"
slug: "sdk-for-ios-explore-classes-mapcamera"
---

# MapCamera

<div class="declaration">

<div class="language">

``` highlight
public class MapCamera
```

``` highlight
extension MapCamera: NativeBase
```

``` highlight
extension MapCamera: Hashable
```

</div>

</div>

Represents the camera looking onto the map view.

Each map instance has exactly one camera that is used to manipulate the way the map is displayed.

Any updates to the state of the camera will be applied while drawing the next map view frame and the current state of the camera reflects what is currently drawn inside the map view.

Note: The camera can be configured and positioned even before a map scene is loaded for the first time. This allows for pre-setting the desired camera position, orientation, and zoom level, which will be applied once the map scene becomes available.

**Camera Model**

*Camera Concepts and Units*

By default, HERE SDK uses an idealized Earth globe with a 3D-capable camera model. Being a 3D camera model means that the world position can be freely specified in geodetic 3D space (i.e. Earth centric) and the orientation can be freely changed around two axes - bearing (also known as head) and tilt (also known as pitch).

The camera supports the look-at target with orientation on the ground way of setting up the camera in space. The camera is placed so that it looks at a specific geo-coordinates (placed at the `principal point`) from a given orientation and distance.

- the look-at target in geo-coordinates (latitude, longitude) in degrees and an `altitude` in meters above MSL (mean sea level) at the `principal point`
- the `orientation` at the look-at target
- the distance of the camera from the look-at target, given as `distance` in meters or as `zoom-level`

*Getting the current camera state*

The current camera state can be obtained by the <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC5stateAC5StateVvp">`MapCamera.state`</a> call. It contains information about the camera look-at target (geo-coordinates and orientation) in geodetic space. The values are returned for the current `principal point`. This can lead to surprising or unexpected values in cases where the camera position/orientation was specified for another screen point, e.g. when using

    MapCameraUpdateFactory.lookAt(GeoBox)

with a view rectangle, whose center does not coincide with the `principal point`. In this case, the geo-coordinates of the look-at target will differ from the center of the geo-box used in the `lookAt` call.
</p>

*Geo coordinates*

Geo-coordinates are given in degrees and follow the common nomenclature of positive northern latitudes and positive eastern longitudes.

*Altitude*

When `altitude` is specified, it is always in meters above mean sea level (MSL). If this value is invalid (not-a-number) or not specified, then the terrain height at the given geo-coordinates will be looked up from the map. This is especially interesting in cases where terrain elevation is used within the map display.

*Distance vs zoom-level vs scale*

Map camera `distance, zoom-level` and `scale` determine how much of the world is visible on the HERE map. `Distance, zoom-level` and `scale` are directly connected and changing one will automatically change the others as well (except for `distance`/`scale` changes that map to `zoom-level` values \< 0 or \> 23).

- `distance`: the distance from the camera to the look-at target on the surface of the Earth, in meters

- `zoom-level`: the map zoom level, in the range \[0, 3\]. The relation between the width of the equator in logical pixels `w` and the zoom level `z` is:

      w = 256 * 2^(z)

- `scale`: the scale of the map at the look-at target in meters on screen per meters on Earth. So a scale of 0.001 shows 10 meters on Earth within 1 cm on screen.

The following mapping represents the `zoom-level` values:

| zoom-level | ~ scale on screen (130dpi) | width of the equator in logical pixels | what can be seen |
|----|:--:|:--:|:--:|
| 0 | 1:800 million | 256 | Earth |
| 1 | 1:400 million | 512 |  |
| 2 | 1:200 million | 1024 |  |
| 3 | 1:100 million | 2048 |  |
| 4 | 1:50 million | 4096 | A continent |
| 5 | 1:25 million | 8192 | Large roads |
| 6 | 1:12 million | 16384 | Large rivers |
| 7 | 1:6 million | 32768 | A country |
| 8 | 1:3 million | 65536 |  |
| 9 | 1:1 million | 131072 |  |
| 10 | 1:780 thousand | 262144 |  |
| 11 | 1:390 thousand | 524288 |  |
| 12 | 1:195 thousand | 1048576 |  |
| 13 | 1:100 thousand | 2097152 |  |
| 14 | 1:50 thousand | 4194304 | A city |
| 15 | 1:25 thousand | 8388608 |  |
| 16 | 1:12 thousand | 16777216 | Buildings |
| 17 | 1:6 thousand | 33554432 | Landmarks |
| 18 | 1:3 thousand | 67108864 |  |
| 19 | 1:1 thousand | 134217728 |  |
| 20 | 1:7 hundred | 268435456 | Streets |
| 21 | 1:3 hundred | 536870912 |  |
| 22 | 1:1 hundred | 1073741824 |  |
| 23 | 1:95 | 2147483648 |  |

*Orientation*

The camera `orientation` is composed of two parts:

- `bearing`: also known as azimuth, the view direction in clockwise degrees; 0° = north, 90° = east, 180° = south, 270° = west
- `tilt`: the angle in degrees from the vertical that the camera is looking down at the Earth; 0° = straight down.

*Changing the Camera*

All changes to the camera are encapsulated in camera updates that are created using the methods in the <a href="sdk-for-ios-explore-classes-mapcameraupdatefactory">`MapCameraUpdateFactory`</a> class.

These updates can then be applied to the <a href="sdk-for-ios-explore-classes-heremap">`HereMap`</a> using <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF">`MapCamera.applyUpdate(...)`</a>.

Camera updates are queued and executed when the next frame is rendered. They are executed in the order in which they were applied.

*Animating the Camera*

Camera updates can be animated by first creating a camera animation using the methods in the <a href="sdk-for-ios-explore-classes-mapcameraanimationfactory">`MapCameraAnimationFactory`</a> class and then applying this animation to the <a href="sdk-for-ios-explore-classes-heremap">`HereMap`</a> using

    MapCamera.startAnimation(MapCameraAnimation, AnimationDelegate)

.
</p>

Only one camera animation for one camera component at a time is supported. Applying a new animation will cancel the active animation before the new one is started. The start position in this case is where ever the active animation happened to be at the time. Different components are camera state (`target pose` and `distance/zoom level/scale`) and camera projection (`field of view, focal length` and `principal point`).

The running animations can also be canceled using <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC16cancelAnimationsyyF">`MapCamera.cancelAnimations(...)`</a> or individual ones using <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF">`MapCamera.cancelAnimation(...)`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC03DryC13UpdateHandlera"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-DryCameraUpdateHandler" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC03DryC13UpdateHandlera" class="token"><code>DryCameraUpdateHandler</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Used to report back results of dry update application to camera.

  Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias DryCameraUpdateHandler = (_ cameraState: MapCamera.State?) -> Void
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcamera-state">State</a>

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
  <td><code> </code><em><code>cameraState</code></em><code> </code></td>
  <td><div>
  <p>Map camera state after dry application of update</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5stateAC5StateVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-state" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC5stateAC5StateVvp" class="token"><code>state</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Current state of the camera that reflects what is currently drawn by the map view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var state: MapCamera.State { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcamera-state">State</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC14principalPointAA7Point2DVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-principalPoint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC14principalPointAA7Point2DVvp" class="token"><code>principalPoint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines the pixel point where the target is placed within the map view. Setting a new principal point instantly moves the map to render the current target coordinates at the new principal point. By default, the principal point is located at the center of the map view. It is set in pixels relative to the map view’s origin top-left (0, 0). Values outside the map view’s dimensions (x \< 0 \|\| x \> width, y \< 0 \|\| y \> height) will be rejected silently and the current principal point is kept.

  The value of the principal point is adjusted when the dimensions of the map view change, so that it stays in the same point relative to width and height. Meaning that when a principal point it set to bottom middle of the map view, it will stay in the bottom middle regardless of the changes to dimensions and orientation of the view.

  Note: The principal point affects all programmatical map transformations (rotate, orbit, tilt and zoom) and the two-finger-pan gesture to tilt the map. Other gestures, like pinch-rotate, are not affected.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var principalPoint: Point2D { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-point2d">Point2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-boundingBox" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp" class="token"><code>boundingBox</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Currently visible map area encompassed in a GeoBox. Note that this bounding box is always rectangular, and its sides are always parallel to the latitude and longitude. If the camera is rotated, the returned bounding box will be a circumscribed rectangle that is larger than the visible map area. Similarly, when the map is tilted (for example, if the map is tilted by 45 degrees), the visible map area represents a trapezoidal area in the world. Resulting value will then be a larger circumscribed rectangle that contains this trapezoid area. Because on this, corners of the resulting bounding box may be located outside of the currently visible area.

  When the map area does not fully fill the viewport, `nil` is returned.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var boundingBox: GeoBox? { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6limitsAA0bC6LimitsCvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-limits" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6limitsAA0bC6LimitsCvp" class="token"><code>limits</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controls limits for the camera settings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var limits: MapCameraLimits { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcameralimits">MapCameraLimits</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-State" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV" class="token"><code>State</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Encapsulates state of the camera.

  <a href="sdk-for-ios-explore-classes-mapcamera-state" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct State
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC21FarPlaneConfigurationV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-FarPlaneConfiguration" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC21FarPlaneConfigurationV" class="token"><code>FarPlaneConfiguration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Far plane distance configuration for a zoom level.

  Effective far plane is computed from both parameters as: farPlaneInMeters = max( minDistanceInMeters, distanceToTargetInMeters \* distanceFactor )

  <a href="sdk-for-ios-explore-classes-mapcamera-farplaneconfiguration" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct FarPlaneConfiguration : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC24setFarPlaneConfigurationyySDySdAC0efG0VGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setFarPlaneConfiguration-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC24setFarPlaneConfigurationyySDySdAC0efG0VGF" class="token"><code>setFarPlaneConfiguration(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets far plane distance configs per zoom level.

  Values are linearly interpolated between provided zoom levels. For z between z0 and z1: t = (z - z0) / (z1 - z0) distanceFactor(z) = lerp(distanceFactor0, distanceFactor1, t) minDistance(z) = lerp(minDistance0, minDistance1, t)

  Effective far plane for the current frame is: farPlaneInMeters = max( minDistance(z), distanceToTargetInMeters \* distanceFactor(z) )

  Sample Configuration (balanced quality/performance, tune per zoom level): 14.4 -\> FarPlaneConfiguration(1.3) 18.34 -\> FarPlaneConfiguration(2.0) 19.60 -\> FarPlaneConfiguration(1.3) minDistanceInMeters remains default in this case. Passing an empty map clears the per-zoom override and restores the default behavior. Non-finite zoom levels or values are ignored. Distance factors are clamped to 0.1 to 10.0. The minimum distance is clamped to a range of \[100, 3000\] meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setFarPlaneConfiguration(_ configs: [Double : MapCamera.FarPlaneConfiguration])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcamera-farplaneconfiguration">FarPlaneConfiguration</a>

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
  <td><code> </code><em><code>configs</code></em><code> </code></td>
  <td><div>
  <p>Per-zoom override mapping from zoom level to distance configuration.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF" class="token"><code>addDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds a delegate to this camera that will be notified on the main thread every time the map is redrawn with new camera parameters.

  Adding the same delegate multiple times has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addDelegate(_ delegate: MapCameraDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapcameradelegate">MapCameraDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>The delegate to add.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC14removeDelegateyyAA0bcE0_pF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeDelegate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC14removeDelegateyyAA0bcE0_pF" class="token"><code>removeDelegate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes the delegate from the camera.

  Trying to remove a delegate that is not currently registered has no effect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeDelegate(_ delegate: MapCameraDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-protocols-mapcameradelegate">MapCameraDelegate</a>

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
  <td><code> </code><em><code>delegate</code></em><code> </code></td>
  <td><div>
  <p>Delegate to be removed from receiving state notifications.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC15removeDelegatesyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeDelegates" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC15removeDelegatesyyF" class="token"><code>removeDelegates()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all registered delegates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeDelegates()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-applyUpdate-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC11applyUpdateyyAA0bcE0CF" class="token"><code>applyUpdate(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Applies camera update to the map camera.

  Any ongoing camera animations will be cancelled and the corresponding camera animation delegate will be notified.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func applyUpdate(_ cameraUpdate: MapCameraUpdate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcameraupdate">MapCameraUpdate</a>

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
  <td><code> </code><em><code>cameraUpdate</code></em><code> </code></td>
  <td><div>
  <p>The update that gets applied to camera.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC14dryApplyUpdate_10completionyAA0bcF0C_yAC5StateVSgctF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-dryApplyUpdate-_-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC14dryApplyUpdate_10completionyAA0bcF0C_yAC5StateVSgctF" class="token"><code>dryApplyUpdate(_:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Computes result of applying camera update without changing state of the map camera.

  Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func dryApplyUpdate(_ cameraUpdate: MapCameraUpdate, completion: @escaping MapCamera.DryCameraUpdateHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcameraupdate">MapCameraUpdate</a>
  - <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC03DryC13UpdateHandlera">DryCameraUpdateHandler</a>

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
  <td><code> </code><em><code>cameraUpdate</code></em><code> </code></td>
  <td><div>
  <p>The update that gets dryly applied to camera.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Called upon completion with computed map state.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC14startAnimationyyAA0bcE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-startAnimation-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC14startAnimationyyAA0bcE0CF" class="token"><code>startAnimation(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts a given camera animation.

  Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties, like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length). The corresponding delegate of an ongoing animation will be notified about the cancellation in these cases.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func startAnimation(_ cameraAnimation: MapCameraAnimation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <td><code> </code><em><code>cameraAnimation</code></em><code> </code></td>
  <td><div>
  <p>The animation to be started.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-startAnimation-_-animationDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF" class="token"><code>startAnimation(_:</code><wbr></wbr><code>animationDelegate:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Starts a given camera animation. The state of the animation can be tracked with the provided listener.

  Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties, like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length). The corresponding delegate of an ongoing animation will be notified about the cancellation in these cases.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func startAnimation(_ cameraAnimation: MapCameraAnimation, animationDelegate: AnimationDelegate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>
  - <a href="sdk-for-ios-explore-protocols-animationdelegate">AnimationDelegate</a>

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
  <td><code> </code><em><code>cameraAnimation</code></em><code> </code></td>
  <td><div>
  <p>The animation to be started.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>animationDelegate</code></em><code> </code></td>
  <td><div>
  <p>Animation delegate. A strong reference is kept internally up until the animation gets cancelled or completed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-cancelAnimation-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC15cancelAnimationyyAA0bcE0CF" class="token"><code>cancelAnimation(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Cancels an ongoing camera animation.

  Upon cancellation, the corresponding delegate will be notified.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func cancelAnimation(_ cameraAnimation: MapCameraAnimation)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <td><code> </code><em><code>cameraAnimation</code></em><code> </code></td>
  <td><div>
  <p>The animation to be cancelled.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC16cancelAnimationsyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-cancelAnimations" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC16cancelAnimationsyyF" class="token"><code>cancelAnimations()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Cancels any ongoing camera animation.

  Upon cancellation, the corresponding delegate of any cancelled animation will be notified.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func cancelAnimations()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC7orbitBy_6aroundyAA20GeoOrientationUpdateV_AA7Point2DVtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-orbitBy-_-around" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC7orbitBy_6aroundyAA20GeoOrientationUpdateV_AA7Point2DVtF" class="token"><code>orbitBy(_:</code><wbr></wbr><code>around:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Orbits the camera around a specified view point by increasing tilt and bearing by specified delta values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func orbitBy(_ delta: GeoOrientationUpdate, around origin: Point2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-explore-structs-point2d">Point2D</a>

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
  <p>Camera orientation change, containing tilt and bearing angle deltas.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>origin</code></em><code> </code></td>
  <td><div>
  <p>Pixel point in view coordinates around which orbiting occurs.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6zoomBy_6aroundySd_AA7Point2DVtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-zoomBy-_-around" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6zoomBy_6aroundySd_AA7Point2DVtF" class="token"><code>zoomBy(_:</code><wbr></wbr><code>around:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zooms in or out by a specified factor.

  This effectively changes the distance from the camera to the <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV17targetCoordinatesAA03GeoF0Vvp">`MapCamera.State.targetCoordinates`</a> by the specified factor, which changes <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV9zoomLevelSdvp">`MapCamera.State.zoomLevel`</a> as well.

  Values above 1.0 will zoom in and values below will zoom out.

  The relation with <a href="sdk-for-ios-explore-classes-mapcamera-state#sdk-for-ios-explore-s-7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">`MapCamera.State.distanceToTargetInMeters`</a> is inversely linear, meaning that zooming by 4 will decrease distance to target by 4 while zooming by 0.5 will increase distance to target by 2.

  The relation with zoom level is logarithmic. Meaning that zooming by a factor of 4 will increase zoom level by 2 (because log2(4) == 2). So to zoom in by X zoom levels, the zoom factor needs to be 2^X. To zoom out by X zoom levels, zoom factor needs to be 1/(2^X).

  The zooming occurs around the specified origin inside the view.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func zoomBy(_ factor: Double, around origin: Point2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-point2d">Point2D</a>

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
  <p>The zoom factor. Values above 1.0 will zoom in and values below will zoom out.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>origin</code></em><code> </code></td>
  <td><div>
  <p>Pixel point in view coordinates around which zooming occurs.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6zoomTo0D5LevelySd_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-zoomTo-zoomLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6zoomTo0D5LevelySd_tF" class="token"><code>zoomTo(zoomLevel:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Zooms to the specified zoom level. The supplied value will be clamped to the range of \[0, 22\], where 0 is a view of whole globe and 22 is street level.

  This effectively changes the distance from the camera to the target. The zooming occurs around the current target point.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func zoomTo(zoomLevel: Double)
  ```

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
  <p>The zoom level to set, clamped to the range of [0, 22].</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt5pointyAA14GeoCoordinatesV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-lookAt-point" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt5pointyAA14GeoCoordinatesV_tF" class="token"><code>lookAt(point:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes the camera look at a new geodetic target, while preserving the current orientation and distance to the target.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func lookAt(point target: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>

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
  <p>Geodetic coordinates at which the camera will point.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt5point4zoomyAA14GeoCoordinatesV_AA0B7MeasureVtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-lookAt-point-zoom" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt5point4zoomyAA14GeoCoordinatesV_AA0B7MeasureVtF" class="token"><code>lookAt(point:</code><wbr></wbr><code>zoom:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes the camera look at the geodetic target with the given zoom.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func lookAt(point target: GeoCoordinates, zoom: MapMeasure)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>

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
  <p>Geodetic coordinates at which the camera will point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>zoom</code></em><code> </code></td>
  <td><div>
  <p>The zoom level which can be provided as distance to the target point, scale or zoom level.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt5point11orientation4zoomyAA14GeoCoordinatesV_AA0I17OrientationUpdateVAA0B7MeasureVtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-lookAt-point-orientation-zoom" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt5point11orientation4zoomyAA14GeoCoordinatesV_AA0I17OrientationUpdateVAA0B7MeasureVtF" class="token"><code>lookAt(point:</code><wbr></wbr><code>orientation:</code><wbr></wbr><code>zoom:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes the camera look at the geodetic target with the given zoom and orientation.

  The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method.

  The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func lookAt(point target: GeoCoordinates, orientation: GeoOrientationUpdate, zoom: MapMeasure)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinates">GeoCoordinates</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-explore-structs-mapmeasure">MapMeasure</a>

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
  <p>Geodetic coordinates at which the camera will point.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Desired orientation of the camera.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>zoom</code></em><code> </code></td>
  <td><div>
  <p>The zoom level which can be provided as distance to the target point, scale or zoom level.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt4area11orientationyAA6GeoBoxV_AA0H17OrientationUpdateVtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-lookAt-area-orientation" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt4area11orientationyAA6GeoBoxV_AA0H17OrientationUpdateVtF" class="token"><code>lookAt(area:</code><wbr></wbr><code>orientation:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes the camera look at the specified geodetic area.

  The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method.

  The altitude of the target points is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func lookAt(area target: GeoBox, orientation: GeoOrientationUpdate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>

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
  <p>Geodetic area at which the camera will point</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Desired orientation of the camera</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt4area11orientation13viewRectangleyAA6GeoBoxV_AA0J17OrientationUpdateVAA11Rectangle2DVtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-lookAt-area-orientation-viewRectangle" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC6lookAt4area11orientation13viewRectangleyAA6GeoBoxV_AA0J17OrientationUpdateVAA11Rectangle2DVtF" class="token"><code>lookAt(area:</code><wbr></wbr><code>orientation:</code><wbr></wbr><code>viewRectangle:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes the camera look at the specified geodetic area and pass a rectangle which specifies where the area should appear inside of the map view.

  The supplied orientation is the orientation of the camera looking at the target, so the resulting camera state will have the same orientation as the one supplied to this method. Please note that the resulting orientation might deviate from the provided orientation. This is particularly the case if a large geobox on world level and a view rectangle which is relatively small was passed to the method.

  The altitude of the target points is ignored.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func lookAt(area target: GeoBox, orientation: GeoOrientationUpdate, viewRectangle: Rectangle2D)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geobox">GeoBox</a>
  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-explore-structs-rectangle2d">Rectangle2D</a>

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
  <p>Geodetic area which will be shown in the viewRectangle.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Desired orientation of the camera.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>viewRectangle</code></em><code> </code></td>
  <td><div>
  <p>The view rectangle in viewport pixel coordinates inside which the geographical target area is displayed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC19setDistanceToTarget16distanceInMetersySd_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setDistanceToTarget-distanceInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC19setDistanceToTarget16distanceInMetersySd_tF" class="token"><code>setDistanceToTarget(distanceInMeters:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Makes the camera look at current target from certain distance

  This function neither modifies target coordinates nor target orientation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setDistanceToTarget(distanceInMeters: Double)
  ```

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
  <td><code> </code><em><code>distanceInMeters</code></em><code> </code></td>
  <td><div>
  <p>Distance in meters to the target point. Minimal distance value is clamped to 100 meters.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk9MapCameraC22setOrientationAtTargetyyAA03GeoE6UpdateVF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setOrientationAtTarget-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapcamera#sdk-for-ios-explore-s-7heresdk9MapCameraC22setOrientationAtTargetyyAA03GeoE6UpdateVF" class="token"><code>setOrientationAtTarget(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Changes camera orientation in relation to target location.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setOrientationAtTarget(_ orientation: GeoOrientationUpdate)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geoorientationupdate">GeoOrientationUpdate</a>

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
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>Desired orientation of the camera.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

