---
title: "Toll Structure Reference"
slug: "sdk-for-ios-explore-structs-toll"
---

# Toll

<div class="declaration">

<div class="language">

``` highlight
public struct Toll : Hashable
```

</div>

</div>

This struct presents all the data for a toll.

**Note**: If you’re using the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a>, be aware that this feature is currently in **beta**. As a result, there may be some bugs or unexpected behaviors. Additionally, this feature and related APIs may be updated in future releases without going through the deprecation process. Note that the <a href="sdk-for-ios-explore-classes-offlineroutingengine">`OfflineRoutingEngine`</a> is only available for the Navigate license. If you’re using the <a href="sdk-for-ios-explore-classes-routingengine">`RoutingEngine`</a>, this feature is considered to be stable.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk4TollV11countryCodeSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-countryCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-toll#sdk-for-ios-explore-s-7heresdk4TollV11countryCodeSSvp" class="token"><code>countryCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The country in which the toll is to be paid in ISO-3166-1 alpha-3 format, e.g. “USA”.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var countryCode: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk4TollV11tollSystemsSaySSGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-tollSystems" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-toll#sdk-for-ios-explore-s-7heresdk4TollV11tollSystemsSaySSGvp" class="token"><code>tollSystems</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Names of the multiple toll systems which are associated with the toll, e.g. \[“ATLANDES“, "ASF”, “COFIROUTE”\]. When the toll information covers several toll roads and the toll system of the each road is different, all toll system names are listed here and the last element will be one of the exit toll booth.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollSystems: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk4TollV5faresSayAA0B4FareVGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-fares" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-toll#sdk-for-ios-explore-s-7heresdk4TollV5faresSayAA0B4FareVGvp" class="token"><code>fares</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of toll fares possible for the toll which may depend on time of day, payment method, vehicle characteristics, etc. If there are multiple toll fares that the router cannot disambiguate, then the list will contain more than one toll fare. Note that this list contains at least one element, i.e. it is never empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var fares: [TollFare]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tollfare">TollFare</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk4TollV11countryCode11tollSystems5faresACSS_SaySSGSayAA0B4FareVGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-countryCode-tollSystems-fares" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-toll#sdk-for-ios-explore-s-7heresdk4TollV11countryCode11tollSystems5faresACSS_SaySSGSayAA0B4FareVGtcfc" class="token"><code>init(countryCode:</code><wbr></wbr><code>tollSystems:</code><wbr></wbr><code>fares:</code><wbr></wbr><code>)</code></a> 

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
  public init(countryCode: String, tollSystems: [String], fares: [TollFare])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-tollfare">TollFare</a>

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

