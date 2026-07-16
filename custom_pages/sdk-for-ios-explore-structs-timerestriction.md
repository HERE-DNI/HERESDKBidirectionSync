---
title: "TimeRestriction Structure Reference"
slug: "sdk-for-ios-explore-structs-timerestriction"
---

# TimeRestriction

<div class="declaration">

<div class="language">

``` highlight
public struct TimeRestriction : Hashable
```

</div>

</div>

Represents restriction based on time.

**Note:** This is a beta release of this feature. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8categoryAC8CategoryOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-category" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-timerestriction#sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8categoryAC8CategoryOvp" class="token"><code>category</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The category of the time restriction.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var category: TimeRestriction.Category
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-timerestriction-category">Category</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TimeRestrictionV13applicabilitySayAA13TransportTypeOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-applicability" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-timerestriction#sdk-for-ios-explore-s-7heresdk15TimeRestrictionV13applicabilitySayAA13TransportTypeOGvp" class="token"><code>applicability</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies to which transportation types the time rules apply.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var applicability: [TransportType]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-transporttype">TransportType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8timeRuleAA0bE0CSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timeRule" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-timerestriction#sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8timeRuleAA0bE0CSgvp" class="token"><code>timeRule</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time rule in TimeDomain format, which is part of the GDF specification.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRule: TimeRule?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8category13applicability8timeRuleA2C8CategoryO_SayAA13TransportTypeOGAA0bG0CSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-category-applicability-timeRule" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-timerestriction#sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8category13applicability8timeRuleA2C8CategoryO_SayAA13TransportTypeOGAA0bG0CSgtcfc" class="token"><code>init(category:</code><wbr></wbr><code>applicability:</code><wbr></wbr><code>timeRule:</code><wbr></wbr><code>)</code></a> 

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
  public init(category: TimeRestriction.Category = TimeRestriction.Category.prohibited, applicability: [TransportType] = [], timeRule: TimeRule? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-timerestriction-category">Category</a>
  - <a href="sdk-for-ios-explore-enums-transporttype">TransportType</a>
  - <a href="sdk-for-ios-explore-classes-timerule">TimeRule</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8CategoryO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-Category" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-timerestriction#sdk-for-ios-explore-s-7heresdk15TimeRestrictionV8CategoryO" class="token"><code>Category</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Category of time restriction.

  <a href="sdk-for-ios-explore-structs-timerestriction-category" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum Category : UInt32, CaseIterable, Codable
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

