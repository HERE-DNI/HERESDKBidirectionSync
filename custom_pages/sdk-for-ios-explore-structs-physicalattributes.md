---
title: "PhysicalAttributes Structure Reference"
slug: "sdk-for-ios-explore-structs-physicalattributes"
---

# PhysicalAttributes

<div class="declaration">

<div class="language">

``` highlight
public struct PhysicalAttributes : Hashable
```

</div>

</div>

Physical attributes of the segment.

***Note*** a road can have more than one attribute at the same time.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV10isDirtRoadSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isDirtRoad" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV10isDirtRoadSbvp" class="token"><code>isDirtRoad</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates whether the navigable segment is paved. Paved is primarily used for map display and routing by assigning higher penalties to unpaved roads. Paved roads are made of concrete, asphalt, cobblestone or brick. Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isDirtRoad: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV8isTunnelSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isTunnel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV8isTunnelSbvp" class="token"><code>isTunnel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies an enclosed (on all sides) passageway through or under an obstruction. This attribute can be used for display or route guidance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTunnel: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV8isBridgeSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isBridge" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV8isBridgeSbvp" class="token"><code>isBridge</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a structure that allows a road, railway, or walkway to pass over another road, railway, waterway, or valley serving map display and route guidance functionalities. Bridge is published on segments that represent significant bridges and/or overpasses; elevated roads are not published as bridge.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isBridge: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV9isPrivateSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isPrivate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV9isPrivateSbvp" class="token"><code>isPrivate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Private identifies roads that are not maintained by an organization responsible for maintenance of public roads. Allows for unique cartographic representation of roads that restrict public use. May be used to avoid routing through a private road.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPrivate: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV12isRoundaboutSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isRoundabout" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV12isRoundaboutSbvp" class="token"><code>isRoundabout</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the presence of a roundabout.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRoundabout: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV19isMultiplyDigitizedSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isMultiplyDigitized" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV19isMultiplyDigitizedSbvp" class="token"><code>isMultiplyDigitized</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies separately digitised roads, i.e., roads that are digitised with one line per direction of traffic instead of one line per road. It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus lane) are located between the separately digitised opposing roadbeds if driver perception remains unchanged.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isMultiplyDigitized: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV7dividerAA11RoadDividerOSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-divider" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV7dividerAA11RoadDividerOSgvp" class="token"><code>divider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the presence of a road divider.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var divider: RoadDivider?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-roaddivider">RoadDivider</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV11isBoatFerrySbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isBoatFerry" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV11isBoatFerrySbvp" class="token"><code>isBoatFerry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a generalised route of a boat ferry for passengers or vehicles over water.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isBoatFerry: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV11isRailFerrySbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isRailFerry" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV11isRailFerrySbvp" class="token"><code>isRailFerry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied on a segment that represent a ferry route for vehicles over rail such as: a route for ferrying passengers over rail, if destination is not accessible by the road network or prohibits the use of automobiles.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRailFerry: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV10isDirtRoad0D6Tunnel0D6Bridge0D7Private0D10Roundabout0D17MultiplyDigitized7divider0D9BoatFerry0d4RailO0ACSb_S5bAA0F7DividerOSgS2btcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-isDirtRoad-isTunnel-isBridge-isPrivate-isRoundabout-isMultiplyDigitized-divider-isBoatFerry-isRailFerry" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-physicalattributes#sdk-for-ios-explore-s-7heresdk18PhysicalAttributesV10isDirtRoad0D6Tunnel0D6Bridge0D7Private0D10Roundabout0D17MultiplyDigitized7divider0D9BoatFerry0d4RailO0ACSb_S5bAA0F7DividerOSgS2btcfc" class="token"><code>init(isDirtRoad:</code><wbr></wbr><code>isTunnel:</code><wbr></wbr><code>isBridge:</code><wbr></wbr><code>isPrivate:</code><wbr></wbr><code>isRoundabout:</code><wbr></wbr><code>isMultiplyDigitized:</code><wbr></wbr><code>divider:</code><wbr></wbr><code>isBoatFerry:</code><wbr></wbr><code>isRailFerry:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance with default values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(isDirtRoad: Bool = false, isTunnel: Bool = false, isBridge: Bool = false, isPrivate: Bool = false, isRoundabout: Bool = false, isMultiplyDigitized: Bool = false, divider: RoadDivider? = nil, isBoatFerry: Bool = false, isRailFerry: Bool = false)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-roaddivider">RoadDivider</a>

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

