---
title: "SpecialSpeedType Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-specialspeedtype"
---

# SpecialSpeedType

<div class="declaration">

<div class="language">

``` highlight
public enum SpecialSpeedType : UInt32, CaseIterable, Codable
```

</div>

</div>

Represents the speed situation type.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO7unknownyA2CmF"></span>` `<span id="//apple_ref/swift/Element/unknown" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO7unknownyA2CmF" class="token"><code>unknown</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unknown special speed type

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unknown
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO08advisoryC0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/advisorySpeed" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO08advisoryC0yA2CmF" class="token"><code>advisorySpeed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  These posted speeds are not the legal limit, but rather serve to warn a driver that road conditions indicate a lower speed is practical. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road.

  - Advisory speed signs due to construction are not included.
  - A speed value is published for advisory signs.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case advisorySpeed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO17speedBumpsPresentyA2CmF"></span>` `<span id="//apple_ref/swift/Element/speedBumpsPresent" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO17speedBumpsPresentyA2CmF" class="token"><code>speedBumpsPresent</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This indicates that for a stretch of road, speed bumps are present or chicanes are present that effectively reduce the posted speed.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case speedBumpsPresent
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO6schoolyA2CmF"></span>` `<span id="//apple_ref/swift/Element/school" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO6schoolyA2CmF" class="token"><code>school</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  School zone signs are often placed to slow drivers before reaching an intersection where children are crossing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case school
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO13timeDependentyA2CmF"></span>` `<span id="//apple_ref/swift/Element/timeDependent" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO13timeDependentyA2CmF" class="token"><code>timeDependent</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. Speed limit that is in effect considering the current local time provided by the device’s clock.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case timeDependent
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO23approximateSeasonalTimeyA2CmF"></span>` `<span id="//apple_ref/swift/Element/approximateSeasonalTime" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO23approximateSeasonalTimeyA2CmF" class="token"><code>approximateSeasonalTime</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Speed limit that is in effect considering the season

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case approximateSeasonalTime
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO13laneDependentyA2CmF"></span>` `<span id="//apple_ref/swift/Element/laneDependent" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO13laneDependentyA2CmF" class="token"><code>laneDependent</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  These are situations where a road has different speed limits per lane.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case laneDependent
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO4rainyA2CmF"></span>` `<span id="//apple_ref/swift/Element/rain" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO4rainyA2CmF" class="token"><code>rain</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when it is raining or there is water on the road.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case rain
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO4snowyA2CmF"></span>` `<span id="//apple_ref/swift/Element/snow" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO4snowyA2CmF" class="token"><code>snow</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when there is snow on the road.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case snow
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk16SpecialSpeedTypeO3fogyA2CmF"></span>` `<span id="//apple_ref/swift/Element/fog" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-specialspeedtype#/s:7heresdk16SpecialSpeedTypeO3fogyA2CmF" class="token"><code>fog</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility decreases due to fog.

  A possible usage example can be to show an icon on the device’s screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case fog
  ```

  </div>

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

