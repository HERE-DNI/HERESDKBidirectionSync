---
title: "MapItemKeyFrameTrack Class Reference"
slug: "sdk-for-ios-explore-classes-mapitemkeyframetrack"
---

# MapItemKeyFrameTrack

<div class="declaration">

<div class="language">

``` highlight
public class MapItemKeyFrameTrack
```

``` highlight
extension MapItemKeyFrameTrack: NativeBase
```

``` highlight
extension MapItemKeyFrameTrack: Hashable
```

</div>

</div>

Stores keyframes for interpolation of a map item property using a specific easing function and interpolation mode.

The keyframe track object is used to create animations, see <a href="sdk-for-ios-explore-classes-mapmarkeranimation">`MapMarkerAnimation`</a> and <a href="sdk-for-ios-explore-classes-mappolylineanimation">`MapPolylineAnimation`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC18InstantiationErrora"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-InstantiationError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack#sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC18InstantiationErrora" class="token"><code>InstantiationError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create `MapItemKeyFrameTrack`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorCode
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack-instantiationerrorcode">InstantiationErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC22InstantiationErrorCodeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-InstantiationErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack#sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack">`MapItemKeyFrameTrack`</a>.

  <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapItemKeyFrameTrack.InstantiationErrorCode : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC6moveTo9keyframes6easing17interpolationModeACSayAA22GeoCoordinatesKeyframeVG_AA6EasingCAA0o13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-moveTo-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack#sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC6moveTo9keyframes6easing17interpolationModeACSayAA22GeoCoordinatesKeyframeVG_AA6EasingCAA0o13InterpolationL0OtKFZ" class="token"><code>moveTo(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a map item position keyframe track. It enables animations over the geographical coordinates where the map item is positioned.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack#sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC18InstantiationErrora">`MapItemKeyFrameTrack.InstantiationError`</a> If the supplied keyframe list is empty or first keyframe duration is not 0.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func moveTo(keyframes: [GeoCoordinatesKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapItemKeyFrameTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-easing">Easing</a>
  - <a href="sdk-for-ios-explore-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the map item position changes over time.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapItemKeyFrameTrack instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC16polylineProgress9keyframes6easing17interpolationModeACSayAA14ScalarKeyframeVG_AA6EasingCAA0n13InterpolationL0OtKFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-polylineProgress-keyframes-easing-interpolationMode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack#sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC16polylineProgress9keyframes6easing17interpolationModeACSayAA14ScalarKeyframeVG_AA6EasingCAA0n13InterpolationL0OtKFZ" class="token"><code>polylineProgress(keyframes:</code><wbr></wbr><code>easing:</code><wbr></wbr><code>interpolationMode:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a keyframe track used to animate the progress of a polyline.

  Each scalar keyframe specifies the value of <a href="sdk-for-ios-explore-classes-mappolyline#sdk-for-ios-explore-s-7heresdk11MapPolylineC8progressSdvp">`MapPolyline.progress`</a> at key points of the animation.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-mapitemkeyframetrack#sdk-for-ios-explore-s-7heresdk20MapItemKeyFrameTrackC18InstantiationErrora">`MapItemKeyFrameTrack.InstantiationError`</a> If the supplied keyframe list is empty or first keyframe duration is not 0.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func polylineProgress(keyframes: [ScalarKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -> MapItemKeyFrameTrack
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-scalarkeyframe">ScalarKeyframe</a>
  - <a href="sdk-for-ios-explore-classes-easing">Easing</a>
  - <a href="sdk-for-ios-explore-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a>

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
  <td><code> </code><em><code>keyframes</code></em><code> </code></td>
  <td><div>
  <p>The list of keyframes that specify how the polyline progress changes over time.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>easing</code></em><code> </code></td>
  <td><div>
  <p>The easing to apply during keyframe interpolation.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>interpolationMode</code></em><code> </code></td>
  <td><div>
  <p>The type of interpolation done between keyframe values.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  MapItemKeyFrameTrack instance.

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

