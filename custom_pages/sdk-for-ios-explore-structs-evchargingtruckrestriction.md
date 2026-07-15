---
title: "EVChargingTruckRestriction Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingtruckrestriction"
---

# EVChargingTruckRestriction

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingTruckRestriction : Hashable
```

</div>

</div>

Represents access restrictions for trucks and light commercial vehicles. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk26EVChargingTruckRestrictionV11truckAccessSayAA0C5ClassOGvp"></span>` `<span id="//apple_ref/swift/Property/truckAccess" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtruckrestriction#/s:7heresdk26EVChargingTruckRestrictionV11truckAccessSayAA0C5ClassOGvp" class="token"><code>truckAccess</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access categories for trucks and light commercial vehicles that the EV charging location is designed to serve.

  While the classifications used as basis for the categories are solely based on vehicle mass, in EV charging context they can be interpreted to give an idea of the dimensional class too, as well as possible other restrictions set by the operator. If there are true dimensional or weight limits at the EV charging location, they are specified separately in vehicleLimitations.

  The classification is available only to a subset of EV charging locations, depending on the information available from the operators. Hence, at least vehicles belonging to the <a href="sdk-for-ios-explore-enums-truckclass#/s:7heresdk10TruckClassO05lightC0yA2CmF">`TruckClass.lightClass`</a> category can be charged also in many EV charging locations not having explicit signaling for the <a href="sdk-for-ios-explore-enums-truckclass#/s:7heresdk10TruckClassO05lightC0yA2CmF">`TruckClass.lightClass`</a> category.

  Furthermore, although the classification is based on mass/weight ranges in growing order, an upper class does not automatically mean that also all lower class vehicles are welcome to charge. For example, a location marked only with category <a href="sdk-for-ios-explore-enums-truckclass#/s:7heresdk10TruckClassO05heavyC0yA2CmF">`TruckClass.heavyClass`</a> is reserved for long-haul trucks only.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var truckAccess: [TruckClass]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26EVChargingTruckRestrictionV24hazardousGoodsRestrictedSbSgvp"></span>` `<span id="//apple_ref/swift/Property/hazardousGoodsRestricted" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingtruckrestriction#/s:7heresdk26EVChargingTruckRestrictionV24hazardousGoodsRestrictedSbSgvp" class="token"><code>hazardousGoodsRestricted</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indication if vehicles carrying hazardous / dangerous goods (ADR) can enter the EV Charging Location.

  - True means the access is restricted. The client should assume the restriction covers all ADR classes.
  - False means there are no restrictions.
  - Absence means the information is not known.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var hazardousGoodsRestricted: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(truckAccess: hazardousGoodsRestricted: )

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

    - truckAccess: Access categories for trucks and light commercial vehicles that the EV charging location is designed to serve.

    While the classifications used as basis for the categories are solely based on vehicle mass, in EV charging context they can be interpreted to give an idea of the dimensional class too, as well as possible other restrictions set by the operator. If there are true dimensional or weight limits at the EV charging location, they are specified separately in vehicleLimitations.

    The classification is available only to a subset of EV charging locations, depending on the information available from the operators. Hence, at least vehicles belonging to the <a href="sdk-for-ios-explore-enums-truckclass#/s:7heresdk10TruckClassO05lightC0yA2CmF">`TruckClass.lightClass`</a> category can be charged also in many EV charging locations not having explicit signaling for the <a href="sdk-for-ios-explore-enums-truckclass#/s:7heresdk10TruckClassO05lightC0yA2CmF">`TruckClass.lightClass`</a> category.

    Furthermore, although the classification is based on mass/weight ranges in growing order, an upper class does not automatically mean that also all lower class vehicles are welcome to charge. For example, a location marked only with category <a href="sdk-for-ios-explore-enums-truckclass#/s:7heresdk10TruckClassO05heavyC0yA2CmF">`TruckClass.heavyClass`</a> is reserved for long-haul trucks only.

    - hazardousGoodsRestricted: Indication if vehicles carrying hazardous / dangerous goods (ADR) can enter the EV Charging Location.
      - True means the access is restricted. The client should assume the restriction covers all ADR classes.
      - False means there are no restrictions.
      - Absence means the information is not known.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( truckAccess : [ TruckClass ] = [], hazardousGoodsRestricted : Bool ? = nil )
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

