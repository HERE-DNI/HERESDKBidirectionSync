---
title: "MapCameraAnimationFactory Class Reference"
slug: "sdk-for-ios-navigate-classes-mapcameraanimationfactory"
---

# MapCameraAnimationFactory

<div class="declaration">

<div class="language">

``` highlight
public class MapCameraAnimationFactory
```

``` highlight
extension MapCameraAnimationFactory: NativeBase
```

``` highlight
extension MapCameraAnimationFactory: Hashable
```

</div>

</div>

Factory for creating MapCameraAnimation objects to change map’s camera over time.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC06createD04from8duration6easingAA0bcD0CAA0bC6UpdateC_SdAA6EasingCtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-createAnimation-from-duration-easing" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC06createD04from8duration6easingAA0bcD0CAA0bC6UpdateC_SdAA6EasingCtFZ" class="token"><code>createAnimation(from:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a <a href="sdk-for-ios-navigate-classes-mapcameraanimation">`MapCameraAnimation`</a> to gradually update the camera properties within a specified duration from its current values to the ones defined in the

      MapCameraAnimationFactory.createAnimation(MapCameraUpdate, TimeInterval, Easing).cameraUpdate

  . <a href="sdk-for-ios-navigate-classes-mapcameraanimation">`MapCameraAnimation`</a> instances created from <a href="sdk-for-ios-navigate-classes-mapcameraupdatefactory#sdk-for-ios-navigate-s-7heresdk22MapCameraUpdateFactoryC09compositeD0yAA0bcD0CSayAFGKFZ">`MapCameraUpdateFactory.compositeUpdate(...)`</a> instances are not supported. An <a href="sdk-for-ios-navigate-protocols-animationdelegate">`AnimationDelegate`</a> will receive an <a href="sdk-for-ios-navigate-enums-animationstate#sdk-for-ios-navigate-s-7heresdk14AnimationStateO9cancelledyA2CmF">`AnimationState.cancelled`</a> signal when trying to apply such animations.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func createAnimation(from cameraUpdate: MapCameraUpdate, duration: TimeInterval, easing: Easing) -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcameraupdate">MapCameraUpdate</a>
  - <a href="sdk-for-ios-navigate-classes-easing">Easing</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <p>Update which should be applied to the map camera.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>duration</code></em><code> </code></td>
  <td><div>
  <p>Duration of the animation. Negative duration results in no camera change when applied.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>Easing to apply.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC06createD05trackAA0bcD0CAA0bC13KeyframeTrackC_tFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-createAnimation-track" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC06createD05trackAA0bcD0CAA0bC13KeyframeTrackC_tFZ" class="token"><code>createAnimation(track:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a MapCameraAnimation for a movement defined by the supplied

      MapCameraAnimationFactory.createAnimation(MapCameraKeyframeTrack).track

  .
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func createAnimation(track: MapCameraKeyframeTrack) -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <td><code> </code><em><code>track</code></em><code> </code></td>
  <td><div>
  <p>The track</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC06createD06tracksAA0bcD0CSayAA0bC13KeyframeTrackCG_tKFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-createAnimation-tracks" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC06createD06tracksAA0bcD0CSayAA0bC13KeyframeTrackCG_tKFZ" class="token"><code>createAnimation(tracks:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a MapCameraAnimation for a movement defined by the supplied list of

      MapCameraAnimationFactory.createAnimation([MapCameraKeyframeTrack]).tracks

  . Keyframe tracks specify how the map camera properties change during the animation. For the animation to be possible, no two different tracks can affect the same map camera property. The input tracks are validated with that in mind.
  </p>

  However, the following cases can only be detected at the time when animation is started:

  - Changing altitude of camera position also changes camera look-at distance and at high altitudes, also camera look-at orientation.
  - Changing tilt of camera orientation also changes camera look-at distance and camera look-at target.
  - Changing bearing of camera orientation also changes camera look-at target if current tilt is not 0.
  - Changing tilt or bearing of camera look-at orientation also changes camera position.
  - Changing camera look-at orientation also changes camera look-at distance if tilt is not 0.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapcameraanimation#sdk-for-ios-navigate-s-7heresdk18MapCameraAnimationC18InstantiationErrora">`MapCameraAnimation.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func createAnimation(tracks: [MapCameraKeyframeTrack]) throws -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <td><code> </code><em><code>tracks</code></em><code> </code></td>
  <td><div>
  <p>The list of tracks</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_S2dtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-flyTo-target-bowFactor-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_S2dtFZ" class="token"><code>flyTo(target:</code><wbr></wbr><code>bowFactor:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

  The beginning and end of the animation will use the current zoom.

  Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func flyTo(target: GeoCoordinatesUpdate, bowFactor: Double, duration: TimeInterval) -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <p>The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bowFactor</code></em><code> </code></td>
  <td><div>
  <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>duration</code></em><code> </code></td>
  <td><div>
  <p>Duration of the flight. Negative duration results in no camera change when applied.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0m11OrientationO0VS2dtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-flyTo-target-orientation-bowFactor-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0m11OrientationO0VS2dtFZ" class="token"><code>flyTo(target:</code><wbr></wbr><code>orientation:</code><wbr></wbr><code>bowFactor:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

  The beginning and end of the animation will use the current zoom.

  Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func flyTo(target: GeoCoordinatesUpdate, orientation: GeoOrientationUpdate, bowFactor: Double, duration: TimeInterval) -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-navigate-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <p>The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>The orientation at destination.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bowFactor</code></em><code> </code></td>
  <td><div>
  <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>duration</code></em><code> </code></td>
  <td><div>
  <p>Duration of the flight. Negative duration results in no camera change when applied.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0B7MeasureVS2dtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-flyTo-target-zoom-bowFactor-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0B7MeasureVS2dtFZ" class="token"><code>flyTo(target:</code><wbr></wbr><code>zoom:</code><wbr></wbr><code>bowFactor:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.

  The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.

  Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func flyTo(target: GeoCoordinatesUpdate, zoom: MapMeasure, bowFactor: Double, duration: TimeInterval) -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-navigate-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <p>The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>zoom</code></em><code> </code></td>
  <td><div>
  <p>The zoom at the end of the animation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bowFactor</code></em><code> </code></td>
  <td><div>
  <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>duration</code></em><code> </code></td>
  <td><div>
  <p>Duration of the flight. Negative duration results in no camera change when applied.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0n11OrientationP0VAA0B7MeasureVS2dtFZ"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-flyTo-target-orientation-zoom-bowFactor-duration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapcameraanimationfactory#sdk-for-ios-navigate-s-7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0n11OrientationP0VAA0B7MeasureVS2dtFZ" class="token"><code>flyTo(target:</code><wbr></wbr><code>orientation:</code><wbr></wbr><code>zoom:</code><wbr></wbr><code>bowFactor:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.

  The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.

  Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func flyTo(target: GeoCoordinatesUpdate, orientation: GeoOrientationUpdate, zoom: MapMeasure, bowFactor: Double, duration: TimeInterval) -> MapCameraAnimation
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a>
  - <a href="sdk-for-ios-navigate-structs-geoorientationupdate">GeoOrientationUpdate</a>
  - <a href="sdk-for-ios-navigate-structs-mapmeasure">MapMeasure</a>
  - <a href="sdk-for-ios-navigate-classes-mapcameraanimation">MapCameraAnimation</a>

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
  <p>The coordinates of the camera destination point. Any target sub-element value that is not finite will be set to the current camera target sub-element value. Note: The altitude of the target point is ignored. Any subsequent camera updates and animations will consider the target point as being located on the ground.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>orientation</code></em><code> </code></td>
  <td><div>
  <p>The orientation at destination.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>zoom</code></em><code> </code></td>
  <td><div>
  <p>The zoom at the end of the animation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>bowFactor</code></em><code> </code></td>
  <td><div>
  <p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>duration</code></em><code> </code></td>
  <td><div>
  <p>Duration of the flight. Negative duration results in no camera change when applied.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapCameraAnimation instance

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

