---
title: "ViolatedRestriction Structure Reference"
slug: "sdk-for-ios-explore-structs-violatedrestriction"
---

# ViolatedRestriction

<div class="declaration">

<div class="language">

``` highlight
public struct ViolatedRestriction : Hashable
```

</div>

</div>

`ViolatedRestriction` contains all the violated restriction details for the planned trip.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV5causeSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-cause" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-violatedrestriction#sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV5causeSSvp" class="token"><code>cause</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Cause of the notice. Human readable description of the notice, for example “Route violates vehicle restriction”. It will be EN-US text only.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var cause: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV13timeDependentSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timeDependent" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-violatedrestriction#sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV13timeDependentSbvp" class="token"><code>timeDependent</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates that restriction depends on time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeDependent: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV7detailsAC7DetailsVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-details" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-violatedrestriction#sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV7detailsAC7DetailsVSgvp" class="token"><code>details</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The detailed information of restriction depending on the specific violation. For time dependent restriction or transport mode restriction, this property will be null. For vehicle restriction, the corresponding member will be set, for example, if the vehicle violates the maximum allowed gross weight for a specific route, the max_gross_weight_in_kilograms will be set with the maximum allowed gross weight for this route.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var details: ViolatedRestriction.Details?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-violatedrestriction-details">Details</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV5cause13timeDependent7detailsACSS_SbAC7DetailsVSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-cause-timeDependent-details" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-violatedrestriction#sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV5cause13timeDependent7detailsACSS_SbAC7DetailsVSgtcfc" class="token"><code>init(cause:</code><wbr></wbr><code>timeDependent:</code><wbr></wbr><code>details:</code><wbr></wbr><code>)</code></a> 

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
  public init(cause: String, timeDependent: Bool, details: ViolatedRestriction.Details? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-violatedrestriction-details">Details</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV7DetailsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-Details" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-violatedrestriction#sdk-for-ios-explore-s-7heresdk19ViolatedRestrictionV7DetailsV" class="token"><code>Details</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set. For example, if the vehicle violates the maximum allowed height during the trip, then the member `max_height_in_centimeters` will be set with the maximum allowed height value.

  <a href="sdk-for-ios-explore-structs-violatedrestriction-details" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Details : Hashable
  ```

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

