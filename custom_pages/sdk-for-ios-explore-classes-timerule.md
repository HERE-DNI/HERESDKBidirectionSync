---
title: "TimeRule Class Reference"
slug: "sdk-for-ios-explore-classes-timerule"
---

# TimeRule

<div class="declaration">

<div class="language">

``` highlight
public class TimeRule
```

``` highlight
extension TimeRule: NativeBase
```

``` highlight
extension TimeRule: Hashable
```

</div>

</div>

Used to indicate a time period of one or more intervals in <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/concepts/time-domain.html">GDF</a> specification. For example: -\*(M3f21h2){M9}(M11f12h2){-M9}+(h15){h2}(h20){h2}, which represents: March 2nd Sunday 02h:00m for 9 months ONLY DURING November 1st Sunday 02h:00m from 9 months ago BUT NOT from 15:00 to 17:00 OR 20:00 to 22:00

The operator \* represents reccuring occurrence, `+` represents a logical OR operation and `-` represents exclusion meaning, BUT NOT operations.

This example string represents a time period that meets the following criteria:

- `M3f21h2`: M3 denotes third month of the year, i.e. March, f2 stands for the second Sunday of the month (as “f” might indicate “first”, “second”, “third”, etc.), 1 stands for the day of the week (1…7, Day of week, Sunday = day 1), and h2 represents the hour of the day (02:00) in 24 hour format.

- `{M9}`: This denotes “for 9 months”, with “M9” standing for nine months. The brackets {} indicate a duration.

- `M11f12h2`: M11 denotes 11th month of the year, i.e. November, f1 stands for the first Monday of the month, 2 stands for the day of the week (1…7, Day of week, Monday = day 2), and h2 represents the hour of the day (02:00) in 24 hour format.

- {-M9}: This denotes “9 months ago from the current stated time”, with “-M9” standing for nine months in the past.

-     (h15){h2}(h20){h2}

  : 15:00 to 17:00 OR 20:00 to 22:00 The brackets {} denotes duration, and the negative sign - represents a past duration.

Note: The time period is a logical AND (&&) combination of two components or points in time and it only applies if a point in time is in both components.

For more advanced examples of `TimeRule` see <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/time-domain.html#time-domain-advanced-examples">here</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TimeRuleC04timeC00D17ZoneOffsetSeconds7dstSpecACSS_s5Int32VSStcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-timeRule-timeZoneOffsetSeconds-dstSpec" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-timerule#sdk-for-ios-explore-s-7heresdk8TimeRuleC04timeC00D17ZoneOffsetSeconds7dstSpecACSS_s5Int32VSStcfc" class="token"><code>init(timeRule:</code><wbr></wbr><code>timeZoneOffsetSeconds:</code><wbr></wbr><code>dstSpec:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance of this class.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(timeRule: String, timeZoneOffsetSeconds: Int32, dstSpec: String)
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>timeRule</code></em><code> </code></td>
  <td><div>
  <p>The time rule as a string in ISO 14825 format.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>timeZoneOffsetSeconds</code></em><code> </code></td>
  <td><div>
  <p>The time zone offset in seconds for the location where the time rule applies.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>dstSpec</code></em><code> </code></td>
  <td><div>
  <p>Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TimeRuleC04timeC6StringSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timeRuleString" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-timerule#sdk-for-ios-explore-s-7heresdk8TimeRuleC04timeC6StringSSvp" class="token"><code>timeRuleString</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time rule as a string in ISO 14825 format.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeRuleString: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TimeRuleC21timeZoneOffsetSecondss5Int32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-timeZoneOffsetSeconds" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-timerule#sdk-for-ios-explore-s-7heresdk8TimeRuleC21timeZoneOffsetSecondss5Int32Vvp" class="token"><code>timeZoneOffsetSeconds</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The time zone offset in seconds for the location where the time rule applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var timeZoneOffsetSeconds: Int32 { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TimeRuleC7dstSpecSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-dstSpec" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-timerule#sdk-for-ios-explore-s-7heresdk8TimeRuleC7dstSpecSSvp" class="token"><code>dstSpec</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dstSpec: String { get }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk8TimeRuleC9appliesTo04dateB0Sb10Foundation4DateV_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-appliesTo-dateTime" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-timerule#sdk-for-ios-explore-s-7heresdk8TimeRuleC9appliesTo04dateB0Sb10Foundation4DateV_tF" class="token"><code>appliesTo(dateTime:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func appliesTo(dateTime: Date) -> Bool
  ```

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>dateTime</code></em><code> </code></td>
  <td><div>
  <p>date and time that should be used for rule verification.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  `true` if the time domain rules applies to the given date and time., `false` - otherwise.

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

