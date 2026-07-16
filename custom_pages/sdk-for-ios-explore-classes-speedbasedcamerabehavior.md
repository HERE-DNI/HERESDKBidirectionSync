---
title: "SpeedBasedCameraBehavior Class Reference"
slug: "sdk-for-ios-explore-classes-speedbasedcamerabehavior"
---

# SpeedBasedCameraBehavior

<div class="declaration">

<div class="language">

``` highlight
public class SpeedBasedCameraBehavior : CameraBehavior
```

``` highlight
extension SpeedBasedCameraBehavior: NativeBase
```

``` highlight
extension SpeedBasedCameraBehavior: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-camerabehavior">CameraBehavior</a>

</div>

Use this class to follow the current location of the user, zooming in and out and changing camera tilt according to the current speed.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorCACycfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-normalizedPrincipalPoint" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp" class="token"><code>normalizedPrincipalPoint</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var normalizedPrincipalPoint: Anchor2D { get set }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-anchor2d">Anchor2D</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-ProfileValue" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV" class="token"><code>ProfileValue</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A single profile value which indicates the speed range in which it applies to its zoom and tilt configuration.

  <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ProfileValue
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC10setProfileyySayAC0G5ValueVGF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setProfile-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC10setProfileyySayAC0G5ValueVGF" class="token"><code>setProfile(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the profile. The speed ranges within the profile can overlap in order to prevent oscillations between adjacent levels. Provided profile must satisfy following conditions:

  - profile must not be empty
  - each speed range must be valid (fromMetersPerSecond must be less then toMetersPerSecond)
  - ranges must be sorted by fromMetersPerSecond and toMetersPerSecond
  - gaps between ranges are not allowed Invalid profile will be rejected and error message logged with explanation of violated restriction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setProfile(_ profile: [SpeedBasedCameraBehavior.ProfileValue])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a>

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
  <td><code> </code><em><code>profile</code></em><code> </code></td>
  <td><div>
  <p>The new profile value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC10getProfileSayAC0G5ValueVGyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC10getProfileSayAC0G5ValueVGyF" class="token"><code>getProfile()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the profile. The speed ranges within the profile can overlap in order to prevent oscillations between adjacent levels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getProfile() -> [SpeedBasedCameraBehavior.ProfileValue]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a>

  </div>

  <div>

  #### Return Value

  The profile.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC16default3DProfileSayAC12ProfileValueVGyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-default3DProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC16default3DProfileSayAC12ProfileValueVGyFZ" class="token"><code>default3DProfile()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func default3DProfile() -> [SpeedBasedCameraBehavior.ProfileValue]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a>

  </div>

  <div>

  #### Return Value

  the default 3D profile.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC16default2DProfileSayAC12ProfileValueVGyFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-default2DProfile" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior#sdk-for-ios-explore-s-7heresdk24SpeedBasedCameraBehaviorC16default2DProfileSayAC12ProfileValueVGyFZ" class="token"><code>default2DProfile()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func default2DProfile() -> [SpeedBasedCameraBehavior.ProfileValue]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-speedbasedcamerabehavior-profilevalue">ProfileValue</a>

  </div>

  <div>

  #### Return Value

  the default 2D profile.

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

