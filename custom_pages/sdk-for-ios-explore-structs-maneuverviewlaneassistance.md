---
title: "ManeuverViewLaneAssistance Structure Reference"
slug: "sdk-for-ios-explore-structs-maneuverviewlaneassistance"
---

# ManeuverViewLaneAssistance

<div class="declaration">

<div class="language">

``` highlight
public struct ManeuverViewLaneAssistance : Hashable
```

</div>

</div>

A struct that provides lane assistance information for the next maneuver(s). During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes in order to complete the upcoming maneuvers. The notifications are synchronized with the <a href="sdk-for-ios-explore-protocols-eventtextdelegate">`EventTextDelegate`</a>. <a href="sdk-for-ios-explore-protocols-eventtextdelegate">`EventTextDelegate`</a> has 4 notification types for each maneuver: Range, Reminder, Distance and Action. Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object (e.g. “After 400 meters, turn right onto Invalidenstraße”). The notification will not be sent when other types of maneuver notification are given. The notification will not be sent when no lane data is available. During tracking mode, no notifications are delivered. This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp"></span>` `<span id="//apple_ref/swift/Property/lanesForNextManeuver" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-maneuverviewlaneassistance#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp" class="token"><code>lanesForNextManeuver</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of lanes on the current road that leads to the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. The list is guaranteed to be non-empty. <a href="sdk-for-ios-explore-structs-roadattributes#/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp">`RoadAttributes.isRightDrivingSide`</a> indicates if this is a left-hand driving country or not.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lanesForNextManeuver: [Lane]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNexthB0SayAA0D0VGvp"></span>` `<span id="//apple_ref/swift/Property/lanesForNextNextManeuver" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-maneuverviewlaneassistance#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNexthB0SayAA0D0VGvp" class="token"><code>lanesForNextNextManeuver</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of lanes on the road that leads to the maneuver after the upcoming maneuver. The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and the last index represents the rightmost lane. This is valid for both right-hand and left-hand driving countries. Contraflow lanes are not included in the list. <a href="sdk-for-ios-explore-structs-roadattributes#/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp">`RoadAttributes.isRightDrivingSide`</a> indicates if this is a left-hand driving country or not. By default, this list is empty. It will be filled when the next two maneuvers are too close to each other, or when the next two maneuvers are roundabout maneuvers. Note: This notification is delivered at the same time as the <a href="sdk-for-ios-explore-structs-maneuverviewlaneassistance#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp">`ManeuverViewLaneAssistance.lanesForNextManeuver`</a>. There is no separate maneuver notification on the second maneuver when two maneuvers are are too close to each other.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lanesForNextNextManeuver: [Lane]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(lanesForNextManeuver: lanesForNextNextManeuver: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( lanesForNextManeuver : [ Lane ], lanesForNextNextManeuver : [ Lane ])
  ```

  </pre>

  </div>

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

