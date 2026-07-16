---
title: "EVChargingTariffElementCondition Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingtariffelementcondition"
---

# EVChargingTariffElementCondition

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingTariffElementCondition : Hashable
```

</div>

</div>

Condition that the charging session needs to meet to apply the tariff element. Tariff elements may include conditions that define when they apply:

- Time of day (e.g., 22:00–06:00)
- Day of week (e.g., weekends only)

<div class="aside aside-date">

Date

Date range (e.g., seasonal pricing)

</div>

- Charging session duration
- Battery level thresholds (e.g., overstay fees)

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-date" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4dateAA9DateRangeVSgvp" class="token"><code>date</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Date range when the tariff element is valid. This is typically used to indicate seasonal tariffs or to announce an update to the tariff in advance. It may also be used to indicate spot prices, together with time period.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var date: DateRange?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-daterange">DateRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-days" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4daysSayAA9DayOfWeekOGvp" class="token"><code>days</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Day(s) of the week when the tariff element is valid. An example would be to specify lower prices for weekends

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var days: [DayOfWeek]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-dayofweek">DayOfWeek</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4timeAA14TimeOfDayRangeVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-time" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4timeAA14TimeOfDayRangeVSgvp" class="token"><code>time</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Time period when the tariff element is valid, in local time. The time period wraps around to the next day, when end time of the period <a href="sdk-for-ios-explore-structs-timeofdayrange#sdk-for-ios-explore-s-7heresdk14TimeOfDayRangeV2toSSvp">`TimeOfDayRange.to`</a> is smaller than the beginning <a href="sdk-for-ios-explore-structs-timeofdayrange#sdk-for-ios-explore-s-7heresdk14TimeOfDayRangeV4fromSSvp">`TimeOfDayRange.from`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var time: TimeOfDayRange?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-timeofdayrange">TimeOfDayRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV8durationAA0B13DurationRangeVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-duration" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV8durationAA0B13DurationRangeVSgvp" class="token"><code>duration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Duration of the charging session when the tariff element is valid, in seconds.

  Often only either one of the values is present, indicating the minimum or maximum duration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var duration: EVChargingDurationRange?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-evchargingdurationrange">EVChargingDurationRange</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV20overstayBatteryLevels5Int32VSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-overstayBatteryLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV20overstayBatteryLevels5Int32VSgvp" class="token"><code>overstayBatteryLevel</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum battery level when the tariff element is valid, in percentages. This can be used to set additional fees for charging a full or nearly full battery.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var overstayBatteryLevel: Int32?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4date4days4time8duration20overstayBatteryLevelAcA9DateRangeVSg_SayAA9DayOfWeekOGAA04TimepoN0VSgAA0b8DurationN0VSgs5Int32VSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-date-days-time-duration-overstayBatteryLevel" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-evchargingtariffelementcondition#sdk-for-ios-explore-s-7heresdk32EVChargingTariffElementConditionV4date4days4time8duration20overstayBatteryLevelAcA9DateRangeVSg_SayAA9DayOfWeekOGAA04TimepoN0VSgAA0b8DurationN0VSgs5Int32VSgtcfc" class="token"><code>init(date:</code><wbr></wbr><code>days:</code><wbr></wbr><code>time:</code><wbr></wbr><code>duration:</code><wbr></wbr><code>overstayBatteryLevel:</code><wbr></wbr><code>)</code></a> 

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

    <div class="aside aside-date">

    Date

    Date range when the tariff element is valid. This is typically used to indicate seasonal tariffs or to announce an update to the tariff in advance. It may also be used to indicate spot prices, together with time period.

    </div>

    - days: Day(s) of the week when the tariff element is valid. An example would be to specify lower prices for weekends
    - time: Time period when the tariff element is valid, in local time. The time period wraps around to the next day, when end time of the period <a href="sdk-for-ios-explore-structs-timeofdayrange#sdk-for-ios-explore-s-7heresdk14TimeOfDayRangeV2toSSvp">`TimeOfDayRange.to`</a> is smaller than the beginning <a href="sdk-for-ios-explore-structs-timeofdayrange#sdk-for-ios-explore-s-7heresdk14TimeOfDayRangeV4fromSSvp">`TimeOfDayRange.from`</a>.
    - duration: Duration of the charging session when the tariff element is valid, in seconds.

    Often only either one of the values is present, indicating the minimum or maximum duration.

    - overstayBatteryLevel: Minimum battery level when the tariff element is valid, in percentages. This can be used to set additional fees for charging a full or nearly full battery.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(date: DateRange? = nil, days: [DayOfWeek] = [], time: TimeOfDayRange? = nil, duration: EVChargingDurationRange? = nil, overstayBatteryLevel: Int32? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-daterange">DateRange</a>
  - <a href="sdk-for-ios-explore-enums-dayofweek">DayOfWeek</a>
  - <a href="sdk-for-ios-explore-structs-timeofdayrange">TimeOfDayRange</a>
  - <a href="sdk-for-ios-explore-structs-evchargingdurationrange">EVChargingDurationRange</a>

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

