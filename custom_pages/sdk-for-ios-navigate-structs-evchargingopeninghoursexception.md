---
title: "EVChargingOpeningHoursException Structure Reference"
slug: "sdk-for-ios-navigate-structs-evchargingopeninghoursexception"
---

# EVChargingOpeningHoursException

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingOpeningHoursException : Hashable
```

</div>

</div>

Represents exceptions to the regular opening hours schedule for EV charging locations, such as special closures or extended hours. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV4date10Foundation4DateVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-date" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursexception#sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV4date10Foundation4DateVvp" class="token"><code>date</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Date of special opening hours.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var date: Date
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV7periodsSayAA14TimeOfDayRangeVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-periods" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursexception#sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV7periodsSayAA14TimeOfDayRangeVGvp" class="token"><code>periods</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A list of time periods when the charging location is open on the specified date. The time periods are in the local time zone of the charging location, and are represented as a list of objects with <a href="sdk-for-ios-navigate-structs-timeofdayrange#sdk-for-ios-navigate-s-7heresdk14TimeOfDayRangeV4fromSSvp">`TimeOfDayRange.from`</a> and <a href="sdk-for-ios-navigate-structs-timeofdayrange#sdk-for-ios-navigate-s-7heresdk14TimeOfDayRangeV2toSSvp">`TimeOfDayRange.to`</a> properties.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var periods: [TimeOfDayRange]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-timeofdayrange">TimeOfDayRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV6closedSbvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-closed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursexception#sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV6closedSbvp" class="token"><code>closed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  True if the charging location is closed on particular date, in which case <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursexception#sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV7periodsSayAA14TimeOfDayRangeVGvp">`EVChargingOpeningHoursException.periods`</a> is empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var closed: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV4date7periods6closedAC10Foundation4DateV_SayAA14TimeOfDayRangeVGSbtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-date-periods-closed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-evchargingopeninghoursexception#sdk-for-ios-navigate-s-7heresdk31EVChargingOpeningHoursExceptionV4date7periods6closedAC10Foundation4DateV_SayAA14TimeOfDayRangeVGSbtcfc" class="token"><code>init(date:</code><wbr></wbr><code>periods:</code><wbr></wbr><code>closed:</code><wbr></wbr><code>)</code></a> 

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
  public init(date: Date = Date(timeIntervalSince1970: 0), periods: [TimeOfDayRange] = [], closed: Bool = false)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-timeofdayrange">TimeOfDayRange</a>

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

