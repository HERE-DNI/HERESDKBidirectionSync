---
title: "OpeningHours Structure Reference"
slug: "sdk-for-ios-explore-structs-openinghours"
---

# OpeningHours

<div class="declaration">

<div class="language">

``` highlight
public struct OpeningHours : Hashable
```

</div>

</div>

Represents opening hours information.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12OpeningHoursV4textSaySSGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-text" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-openinghours#sdk-for-ios-explore-s-7heresdk12OpeningHoursV4textSaySSGvp" class="token"><code>text</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of opening hours presented as localized text.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var text: [String]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12OpeningHoursV6isOpenSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isOpen" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-openinghours#sdk-for-ios-explore-s-7heresdk12OpeningHoursV6isOpenSbvp" class="token"><code>isOpen</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Boolean flag informing if the place is open or closed at the time when the search request was initiated. For offline search, this is calculated using device’s time, so it may give incorrect value if device and place are located in different time zones.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isOpen: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12OpeningHoursV19scheduleDetailsListSayAA08ScheduleE0VGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-scheduleDetailsList" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-openinghours#sdk-for-ios-explore-s-7heresdk12OpeningHoursV19scheduleDetailsListSayAA08ScheduleE0VGvp" class="token"><code>scheduleDetailsList</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of schedule details.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var scheduleDetailsList: [ScheduleDetails]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12OpeningHoursV10categoriesSayAA13PlaceCategoryCGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-categories" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-openinghours#sdk-for-ios-explore-s-7heresdk12OpeningHoursV10categoriesSayAA13PlaceCategoryCGvp" class="token"><code>categories</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The list of categories related to opening hours information. This data is not available in offline search.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var categories: [PlaceCategory]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk12OpeningHoursV4text6isOpen19scheduleDetailsList10categoriesACSaySSG_SbSayAA08ScheduleH0VGSayAA13PlaceCategoryCGtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-text-isOpen-scheduleDetailsList-categories" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-openinghours#sdk-for-ios-explore-s-7heresdk12OpeningHoursV4text6isOpen19scheduleDetailsList10categoriesACSaySSG_SbSayAA08ScheduleH0VGSayAA13PlaceCategoryCGtcfc" class="token"><code>init(text:</code><wbr></wbr><code>isOpen:</code><wbr></wbr><code>scheduleDetailsList:</code><wbr></wbr><code>categories:</code><wbr></wbr><code>)</code></a> 

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
  public init(text: [String], isOpen: Bool, scheduleDetailsList: [ScheduleDetails], categories: [PlaceCategory])
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-scheduledetails">ScheduleDetails</a>
  - <a href="sdk-for-ios-explore-classes-placecategory">PlaceCategory</a>

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

