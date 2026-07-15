---
title: "EVChargingOpeningHours Structure Reference"
slug: "sdk-for-ios-explore-structs-evchargingopeninghours"
---

# EVChargingOpeningHours

<div class="declaration">

<div class="language">

``` highlight
public struct EVChargingOpeningHours : Hashable
```

</div>

</div>

Represents the times when the EVSEs at the charging location can be accessed for charging. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk22EVChargingOpeningHoursV8open24x7Sbvp"></span>` `<span id="//apple_ref/swift/Property/open24x7" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingopeninghours#/s:7heresdk22EVChargingOpeningHoursV8open24x7Sbvp" class="token"><code>open24x7</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if the charging location is open 24 hours a day, 7 days per week. If true, <a href="sdk-for-ios-explore-structs-evchargingopeninghours#/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp">`EVChargingOpeningHours.regularSchedule`</a> and <a href="sdk-for-ios-explore-structs-evchargingopeninghours#/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp">`EVChargingOpeningHours.exceptions`</a> will be empty.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var open24x7: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22EVChargingOpeningHoursV18chargingWhenClosedSbvp"></span>` `<span id="//apple_ref/swift/Property/chargingWhenClosed" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingopeninghours#/s:7heresdk22EVChargingOpeningHoursV18chargingWhenClosedSbvp" class="token"><code>chargingWhenClosed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates if it is allowed to leave vehicles in the charging location to continue charging outside opening hours.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var chargingWhenClosed: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp"></span>` `<span id="//apple_ref/swift/Property/regularSchedule" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingopeninghours#/s:7heresdk22EVChargingOpeningHoursV15regularScheduleSayAA0bcdF0VGvp" class="token"><code>regularSchedule</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of regular opening hours schedule for EV charging locations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var regularSchedule: [EVChargingOpeningHoursSchedule]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp"></span>` `<span id="//apple_ref/swift/Property/exceptions" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-structs-evchargingopeninghours#/s:7heresdk22EVChargingOpeningHoursV10exceptionsSayAA0bcD9ExceptionVGvp" class="token"><code>exceptions</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of opening hours exceptions for EV charging locations.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var exceptions: [EVChargingOpeningHoursException]
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(open24x7: chargingWhenClosed: regularSchedule: exceptions: )

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
  public init ( open24x7 : Bool = false , chargingWhenClosed : Bool = true , regularSchedule : [ EVChargingOpeningHoursSchedule ] = [], exceptions : [ EVChargingOpeningHoursException ] = [])
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

