---
title: "TollFarePass Structure Reference"
slug: "sdk-for-ios-explore-structs-tollfarepass"
---

# TollFarePass

<div class="declaration">

<div class="language">

``` highlight
public struct TollFarePass : Hashable
```

</div>

</div>

<a href="sdk-for-ios-explore-structs-tollfare">`TollFare`</a> multi-travel pass characteristics.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TollFarePassV13returnJourneySbSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-returnJourney" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfarepass#sdk-for-ios-explore-s-7heresdk12TollFarePassV13returnJourneySbSgvp" class="token"><code>returnJourney</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This pass includes the fare for the return journey.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var returnJourney: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TollFarePassV14validityPeriodAA0cd8ValidityF0VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-validityPeriod" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfarepass#sdk-for-ios-explore-s-7heresdk12TollFarePassV14validityPeriodAA0cd8ValidityF0VSgvp" class="token"><code>validityPeriod</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies a temporal validity period for a pass.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var validityPeriod: FarePassValidityPeriod?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-farepassvalidityperiod">FarePassValidityPeriod</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TollFarePassV7travelss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-travels" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfarepass#sdk-for-ios-explore-s-7heresdk12TollFarePassV7travelss5Int32VSgvp" class="token"><code>travels</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This pass allows for the specified number of travels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var travels: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TollFarePassV9transferss5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-transfers" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfarepass#sdk-for-ios-explore-s-7heresdk12TollFarePassV9transferss5Int32VSgvp" class="token"><code>transfers</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if transfers are permitted with this pass, and if so, how many.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transfers: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TollFarePassV06seniorD0SbSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-seniorPass" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfarepass#sdk-for-ios-explore-s-7heresdk12TollFarePassV06seniorD0SbSgvp" class="token"><code>seniorPass</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This pass is valid only if presented by a senior person.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var seniorPass: Bool?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12TollFarePassV13returnJourney14validityPeriod7travels9transfers06seniorD0ACSbSg_AA0cd8ValidityH0VSgs5Int32VSgAoItcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-returnJourney-validityPeriod-travels-transfers-seniorPass" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-tollfarepass#sdk-for-ios-explore-s-7heresdk12TollFarePassV13returnJourney14validityPeriod7travels9transfers06seniorD0ACSbSg_AA0cd8ValidityH0VSgs5Int32VSgAoItcfc" class="token"><code>init(returnJourney:</code><wbr></wbr><code>validityPeriod:</code><wbr></wbr><code>travels:</code><wbr></wbr><code>transfers:</code><wbr></wbr><code>seniorPass:</code><wbr></wbr><code>)</code></a> 

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
  public init(returnJourney: Bool? = nil, validityPeriod: FarePassValidityPeriod? = nil, travels: Int32? = nil, transfers: Int32? = nil, seniorPass: Bool? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-farepassvalidityperiod">FarePassValidityPeriod</a>

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

