---
title: "RoadProfileCondition Structure Reference"
slug: "sdk-for-ios-navigate-structs-roadprofilecondition"
---

# RoadProfileCondition

<div class="declaration">

<div class="language">

``` highlight
public struct RoadProfileCondition : Hashable
```

</div>

</div>

Road profile conditions that must be met for a regulation to apply.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV8roadTypeAA017CommercialVehiclebF0Ovp"></span>` `<span id="//apple_ref/swift/Property/roadType" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV8roadTypeAA017CommercialVehiclebF0Ovp" class="token"><code>roadType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Required road type for the regulation to apply.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadType: CommercialVehicleRoadType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV25requiredFunctionalClassesSayAA0fB5ClassOSgGvp"></span>` `<span id="//apple_ref/swift/Property/requiredFunctionalClasses" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV25requiredFunctionalClassesSayAA0fB5ClassOSgGvp" class="token"><code>requiredFunctionalClasses</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Functional road classes on which the regulation applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredFunctionalClasses: [FunctionalRoadClass?]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV19requiredRouteLevelsSayAA0F4TypeOGvp"></span>` `<span id="//apple_ref/swift/Property/requiredRouteLevels" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV19requiredRouteLevelsSayAA0F4TypeOGvp" class="token"><code>requiredRouteLevels</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Route levels on which the regulation applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredRouteLevels: [RouteType]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV21requiredNumberOfLanesAA12IntegerRangeVvp"></span>` `<span id="//apple_ref/swift/Property/requiredNumberOfLanes" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV21requiredNumberOfLanesAA12IntegerRangeVvp" class="token"><code>requiredNumberOfLanes</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Range of lane counts for which the regulation applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var requiredNumberOfLanes: IntegerRange
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV18isControlledAccessSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isControlledAccess" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV18isControlledAccessSbSgvp" class="token"><code>isControlledAccess</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to controlled access roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isControlledAccess: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV015isLimitedAccessB0SbSgvp"></span>` `<span id="//apple_ref/swift/Property/isLimitedAccessRoad" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV015isLimitedAccessB0SbSgvp" class="token"><code>isLimitedAccessRoad</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to limited access roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isLimitedAccessRoad: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV21isMultiplyDigitilizedSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isMultiplyDigitilized" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV21isMultiplyDigitilizedSbSgvp" class="token"><code>isMultiplyDigitilized</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to multiply digitized roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isMultiplyDigitilized: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV02isB14LegallyDividedSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isRoadLegallyDivided" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV02isB14LegallyDividedSbSgvp" class="token"><code>isRoadLegallyDivided</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to legally divided roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRoadLegallyDivided: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV02isB17PhysicallyDividedSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isRoadPhysicallyDivided" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV02isB17PhysicallyDividedSbSgvp" class="token"><code>isRoadPhysicallyDivided</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to physically divided roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRoadPhysicallyDivided: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV010isPriorityB0SbSgvp"></span>` `<span id="//apple_ref/swift/Property/isPriorityRoad" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV010isPriorityB0SbSgvp" class="token"><code>isPriorityRoad</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to priority roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPriorityRoad: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV9isUnpavedSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isUnpaved" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV9isUnpavedSbSgvp" class="token"><code>isUnpaved</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to unpaved roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isUnpaved: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV23isMotorisedVehiclesOnlySbSgvp"></span>` `<span id="//apple_ref/swift/Property/isMotorisedVehiclesOnly" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV23isMotorisedVehiclesOnlySbSgvp" class="token"><code>isMotorisedVehiclesOnly</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to motorised vehicles only roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isMotorisedVehiclesOnly: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV7isUrbanSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isUrban" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV7isUrbanSbSgvp" class="token"><code>isUrban</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to urban roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isUrban: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk20RoadProfileConditionV7isRuralSbSgvp"></span>` `<span id="//apple_ref/swift/Property/isRural" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-structs-roadprofilecondition#/s:7heresdk20RoadProfileConditionV7isRuralSbSgvp" class="token"><code>isRural</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  If true, applies only to rural roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRural: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(roadType: requiredFunctionalClasses: requiredRouteLevels: requiredNumberOfLanes: isControlledAccess: isLimitedAccessRoad: isMultiplyDigitilized: isRoadLegallyDivided: isRoadPhysicallyDivided: isPriorityRoad: isUnpaved: isMotorisedVehiclesOnly: isUrban: isRural: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance with specified parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( roadType : CommercialVehicleRoadType , requiredFunctionalClasses : [ FunctionalRoadClass ?] = [], requiredRouteLevels : [ RouteType ] = [], requiredNumberOfLanes : IntegerRange , isControlledAccess : Bool ? = nil , isLimitedAccessRoad : Bool ? = nil , isMultiplyDigitilized : Bool ? = nil , isRoadLegallyDivided : Bool ? = nil , isRoadPhysicallyDivided : Bool ? = nil , isPriorityRoad : Bool ? = nil , isUnpaved : Bool ? = nil , isMotorisedVehiclesOnly : Bool ? = nil , isUrban : Bool ? = nil , isRural : Bool ? = nil )
  ```

  </pre>

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

