---
title: "MapMarkerAnimation Class Reference"
slug: "sdk-for-ios-navigate-classes-mapmarkeranimation"
---

# MapMarkerAnimation

<div class="declaration">

<div class="language">

``` highlight
public class MapMarkerAnimation
```

``` highlight
extension MapMarkerAnimation: NativeBase
```

``` highlight
extension MapMarkerAnimation: Hashable
```

</div>

</div>

An animation that can be applied to the <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> object.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC18InstantiationErrora"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Alias-InstantiationError" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarkeranimation#sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC18InstantiationErrora" class="token"><code>InstantiationError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when a problem occurs while trying to create a `MapMarkerAnimation`.

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

  - <a href="sdk-for-ios-navigate-classes-mapmarkeranimation-instantiationerrorcode">InstantiationErrorCode</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC5trackAcA0B17ItemKeyFrameTrackC_tKcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-track" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarkeranimation#sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC5trackAcA0B17ItemKeyFrameTrackC_tKcfc" class="token"><code>init(track:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an animation of <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a> based on provided keyframe track.

  Supports tracks created with <a href="sdk-for-ios-navigate-classes-mapitemkeyframetrack">`MapItemKeyFrameTrack`</a> ‘moveTo\*’ methods.

  For starting the animation see <a href="sdk-for-ios-navigate-classes-mapmarker#sdk-for-ios-navigate-s-7heresdk9MapMarkerC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_pSgtF">`MapMarker.startAnimation(...)`</a>.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapmarkeranimation#sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC18InstantiationErrora">`MapMarkerAnimation.InstantiationError`</a> If the specified keyframe track cannot be used to create animation of a <a href="sdk-for-ios-navigate-classes-mapmarker">`MapMarker`</a>.

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

   <span id="sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC22InstantiationErrorCodeO"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Enum-InstantiationErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-mapmarkeranimation#sdk-for-ios-navigate-s-7heresdk18MapMarkerAnimationC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to create a <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">`MapMarkerAnimation`</a>.

  <a href="sdk-for-ios-navigate-classes-mapmarkeranimation-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  ``` highlight
  extension MapMarkerAnimation.InstantiationErrorCode : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-classes-mapmarkeranimation">MapMarkerAnimation</a>

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

