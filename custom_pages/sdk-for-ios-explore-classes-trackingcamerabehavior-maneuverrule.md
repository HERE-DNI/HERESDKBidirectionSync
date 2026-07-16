---
title: "ManeuverRule Structure Reference"
slug: "sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule"
---

# ManeuverRule

<div class="declaration">

<div class="language">

``` highlight
public struct ManeuverRule
```

</div>

</div>

Defines a single rule that determines how <a href="sdk-for-ios-explore-classes-trackingcamerabehavior">`TrackingCameraBehavior`</a> reacts to nearby maneuvers when the current position matches this rule.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClassesSayAA010FunctionalH5ClassOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-functionalRoadClasses" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClassesSayAA010FunctionalH5ClassOGvp" class="token"><code>functionalRoadClasses</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of functional road classes for which this rule applies. The list is unordered. When empty, this rule applies to all functional road classes. Defaults to an empty list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var functionalRoadClasses: [FunctionalRoadClass]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV15maneuverActionsSayAA0E6ActionOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverActions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV15maneuverActionsSayAA0E6ActionOGvp" class="token"><code>maneuverActions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of maneuver actions for which this rule applies. The list is unordered. When empty, this rule applies to all maneuver actions. Defaults to an empty list.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverActions: [ManeuverAction]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-maneuveraction">ManeuverAction</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV08maneuverF7OptionsAC0efH0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-maneuverRuleOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV08maneuverF7OptionsAC0efH0VSgvp" class="token"><code>maneuverRuleOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The options for this rule. When set to `nil`, the camera does not react to maneuvers that match this rule. Defaults to `nil`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maneuverRuleOptions: TrackingCameraBehavior.ManeuverRuleOptions?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverruleoptions">ManeuverRuleOptions</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClasses15maneuverActions0jF7OptionsAESayAA010FunctionalH5ClassOG_SayAA0E6ActionOGAC0efL0VSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-functionalRoadClasses-maneuverActions-maneuverRuleOptions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverrule#sdk-for-ios-explore-s-7heresdk22TrackingCameraBehaviorC12ManeuverRuleV21functionalRoadClasses15maneuverActions0jF7OptionsAESayAA010FunctionalH5ClassOG_SayAA0E6ActionOGAC0efL0VSgtcfc" class="token"><code>init(functionalRoadClasses:</code><wbr></wbr><code>maneuverActions:</code><wbr></wbr><code>maneuverRuleOptions:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(functionalRoadClasses: [FunctionalRoadClass] = [], maneuverActions: [ManeuverAction] = [], maneuverRuleOptions: TrackingCameraBehavior.ManeuverRuleOptions? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-functionalroadclass">FunctionalRoadClass</a>
  - <a href="sdk-for-ios-explore-enums-maneuveraction">ManeuverAction</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
  - <a href="sdk-for-ios-explore-classes-trackingcamerabehavior-maneuverruleoptions">ManeuverRuleOptions</a>

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

