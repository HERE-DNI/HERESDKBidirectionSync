---
title: "TruckRestrictionWarning Structure Reference"
slug: "sdk-for-ios-explore-structs-truckrestrictionwarning"
---

# TruckRestrictionWarning

<div class="declaration">

<div class="language">

``` highlight
public struct TruckRestrictionWarning : Hashable
```

</div>

</div>

Represents truck restrictions. For example, there can be a bridge ahead not high enough to pass a big truck or there can be a road ahead where the truck’s weight exceeds the permissible limit.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV2ids5Int32Vvp"></span>` `<span id="//apple_ref/swift/Property/id" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV2ids5Int32Vvp" class="token"><code>id</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific truck restriction warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV16distanceInMetersSdvp"></span>` `<span id="//apple_ref/swift/Property/distanceInMeters" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV16distanceInMetersSdvp" class="token"><code>distanceInMeters</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance from the current location to the restriction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV06weightC0AA06WeightC0VSgvp"></span>` `<span id="//apple_ref/swift/Property/weightRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV06weightC0AA06WeightC0VSgvp" class="token"><code>weightRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Weight restriction. It is `nil` when there is no known weight restriction ahead.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var weightRestriction: WeightRestriction?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV09dimensionC0AA09DimensionC0VSgvp"></span>` `<span id="//apple_ref/swift/Property/dimensionRestriction" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV09dimensionC0AA09DimensionC0VSgvp" class="token"><code>dimensionRestriction</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Vehicle dimension restrictions. It is `nil` when there is no known dimension restriction ahead.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dimensionRestriction: DimensionRestriction?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV12distanceTypeAA08DistanceF0Ovp"></span>` `<span id="//apple_ref/swift/Property/distanceType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the specified truck restriction is ahead of the vehicle or has just passed by. If it is ahead, then <a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV16distanceInMetersSdvp">`TruckRestrictionWarning.distanceInMeters`</a> is greater than 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV12trailerCountAA12IntegerRangeVSgvp"></span>` `<span id="//apple_ref/swift/Property/trailerCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV12trailerCountAA12IntegerRangeVSgvp" class="token"><code>trailerCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The trailer count for which the current restriction applies. If the field is ‘null’ then the current restriction does not have a condition based on trailers count.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var trailerCount: IntegerRange?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV8timeRuleAA04TimeF0CSgvp"></span>` `<span id="//apple_ref/swift/Property/timeRule" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV8timeRuleAA04TimeF0CSgvp" class="token"><code>timeRule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time rule indicating the time periods for which the restriction applies. If the field is ‘null’ then the restriction is applicable at anytime.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRule: TimeRule?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV13truckRoadTypeAA0bfG0OSgvp"></span>` `<span id="//apple_ref/swift/Property/truckRoadType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV13truckRoadTypeAA0bfG0OSgvp" class="token"><code>truckRoadType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Truck road type restriction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckRoadType: TruckRoadType?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></span>` `<span id="//apple_ref/swift/Property/hazardousMaterials" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV18hazardousMaterialsSayAA17HazardousMaterialOGvp" class="token"><code>hazardousMaterials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of hazardous materials which are restricted on the road section for which the warning applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hazardousMaterials: [HazardousMaterial]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV14tunnelCategoryAA06TunnelF0OSgvp"></span>` `<span id="//apple_ref/swift/Property/tunnelCategory" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV14tunnelCategoryAA06TunnelF0OSgvp" class="token"><code>tunnelCategory</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tunnel category.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tunnelCategory: TunnelCategory?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk23TruckRestrictionWarningV9axleCountAA12IntegerRangeVSgvp"></span>` `<span id="//apple_ref/swift/Property/axleCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-truckrestrictionwarning#/s:7heresdk23TruckRestrictionWarningV9axleCountAA12IntegerRangeVSgvp" class="token"><code>axleCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The axle count for which the current restriction applies. If this field is `nil`, the restriction does not depend on axle count.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var axleCount: IntegerRange?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(id: distanceInMeters: weightRestriction: dimensionRestriction: distanceType: trailerCount: timeRule: truckRoadType: hazardousMaterials: tunnelCategory: axleCount: )

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
  public init ( id : Int32 = 0 , distanceInMeters : Double , weightRestriction : WeightRestriction ? = nil , dimensionRestriction : DimensionRestriction ? = nil , distanceType : DistanceType , trailerCount : IntegerRange ? = nil , timeRule : TimeRule ? = nil , truckRoadType : TruckRoadType ? = nil , hazardousMaterials : [ HazardousMaterial ] = [], tunnelCategory : TunnelCategory ? = nil , axleCount : IntegerRange ? = nil )
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      isGeneral()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Checks if this truck restriction warning is general. A general warning has no specific restriction conditions set. Please note that time rule still might be set for a general warning, but it is not considered as a specific restriction condition. This method only checks that no specific conditions are set for the warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func isGeneral () -> Bool
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  `true` if all restriction fields are null or empty, `false` otherwise.

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

