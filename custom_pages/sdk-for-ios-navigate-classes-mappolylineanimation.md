---
title: "MapPolylineAnimation Class Reference"
slug: "sdk-for-ios-navigate-classes-mappolylineanimation"
---

# MapPolylineAnimation

<div class="declaration">

<div class="language">

``` highlight
public class MapPolylineAnimation
```

``` highlight
extension MapPolylineAnimation: NativeBase
```

``` highlight
extension MapPolylineAnimation: Hashable
```

</div>

</div>

An animation that can be applied to the <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a> object.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC18InstantiationErrora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-InstantiationError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolylineanimation#sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC18InstantiationErrora" class="token"><code>InstantiationError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create a `MapPolylineAnimation`.

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

  - <a href="sdk-for-ios-navigate-classes-mappolylineanimation-instantiationerrorcode">InstantiationErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC5trackAcA0B17ItemKeyFrameTrackC_tKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-track" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolylineanimation#sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC5trackAcA0B17ItemKeyFrameTrackC_tKcfc" class="token"><code>init(track:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an animation of <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a> based on provided keyframe track. Supports tracks created with <a href="sdk-for-ios-navigate-classes-mapitemkeyframetrack">`MapItemKeyFrameTrack`</a> ‘polylineProgress\*’ methods. For starting the animation, see <a href="sdk-for-ios-navigate-classes-mappolyline#sdk-for-ios-navigate-s-7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF">`MapPolyline.startAnimation(...)`</a>.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mappolylineanimation#sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC18InstantiationErrora">`MapPolylineAnimation.InstantiationError`</a> If the specified keyframe track cannot be used to create animation of a <a href="sdk-for-ios-navigate-classes-mappolyline">`MapPolyline`</a>.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(track: MapItemKeyFrameTrack) throws
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a>

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
  <p>The track holding the keyframes for the animation.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC22InstantiationErrorCodeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-InstantiationErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mappolylineanimation#sdk-for-ios-navigate-s-7heresdk20MapPolylineAnimationC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a <a href="sdk-for-ios-navigate-classes-mappolylineanimation">`MapPolylineAnimation`</a>.

  <a href="sdk-for-ios-navigate-classes-mappolylineanimation-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapPolylineAnimation.InstantiationErrorCode : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mappolylineanimation">MapPolylineAnimation</a>

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

