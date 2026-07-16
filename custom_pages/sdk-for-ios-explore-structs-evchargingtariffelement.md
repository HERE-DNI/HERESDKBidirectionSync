---
title: "EVChargingTariffElement Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingtariffelement"
---

# EVChargingTariffElement

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingTariffElement : Hashable
```

</div>

</div>

Represents a tariff element, which defines how pricing is applied. The associated condition assists the client in selecting the appropriate element for a charging session. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk23EVChargingTariffElementV10componentsSayAA0bC14PriceComponentVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-components" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelement#sdk-for-ios-explore-s-7heresdk23EVChargingTariffElementV10componentsSayAA0bC14PriceComponentVGvp" class="token"><code>components</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of price components that describe the tariff. Each of the components should have a different <a href="sdk-for-ios-explore-enums-evchargingtariffdimension">`EVChargingTariffDimension`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var components: [EVChargingTariffPriceComponent]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk23EVChargingTariffElementV9conditionAA0bcD9ConditionVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-condition" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelement#sdk-for-ios-explore-s-7heresdk23EVChargingTariffElementV9conditionAA0bcD9ConditionVSgvp" class="token"><code>condition</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Condition that the charging session needs to meet to apply the tariff element. An element without any condition is typically present for charging sessions that do not meet any of the conditions.

  For example, a tariff element with a lower price can be valid only during nighttime, while a generic tariff element without conditions applies for daytime charging sessions. The conditions are listed in priority order. I.e., when <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp">`EVChargingTariffElementCondition.date`</a> is present, it should be matched first, followed by <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp">`EVChargingTariffElementCondition.days`</a> and so on.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var condition: EVChargingTariffElementCondition?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk23EVChargingTariffElementV10components9conditionACSayAA0bC14PriceComponentVG_AA0bcD9ConditionVSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-components-condition" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelement#sdk-for-ios-explore-s-7heresdk23EVChargingTariffElementV10components9conditionACSayAA0bC14PriceComponentVG_AA0bcD9ConditionVSgtcfc" class="token"><code>init(components:</code><wbr></wbr><code>condition:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  - Parameters

    - components: List of price components that describe the tariff. Each of the components should have a different <a href="sdk-for-ios-explore-enums-evchargingtariffdimension">`EVChargingTariffDimension`</a>.
    - condition: Condition that the charging session needs to meet to apply the tariff element. An element without any condition is typically present for charging sessions that do not meet any of the conditions.

    For example, a tariff element with a lower price can be valid only during nighttime, while a generic tariff element without conditions applies for daytime charging sessions. The conditions are listed in priority order. I.e., when <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp">`EVChargingTariffElementCondition.date`</a> is present, it should be matched first, followed by <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp">`EVChargingTariffElementCondition.days`</a> and so on.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(components: [EVChargingTariffPriceComponent] = [], condition: EVChargingTariffElementCondition? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evchargingtariffpricecomponent">EVChargingTariffPriceComponent</a>
  - <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition">EVChargingTariffElementCondition</a>

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

