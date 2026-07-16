---
title: "DriveRestRegulation Structure Reference"
slug: "sdk-for-ios-navigate-structs-driverestregulation"
---

# DriveRestRegulation

<div class="declaration">

<div class="language">

``` highlight
public struct DriveRestRegulation : Hashable
```

</div>

</div>

Drive-rest regulation defining mandatory rest requirements for commercial vehicle drivers.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxDailyDriveTimeInMinutes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-driverestregulation#sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutesSdSgvp" class="token"><code>maxDailyDriveTimeInMinutes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum continuous or accumulated daily driving time in minutes before a rest is required.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxDailyDriveTimeInMinutes: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV05dailyC12MinInMinutesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-dailyRestMinInMinutes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-driverestregulation#sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV05dailyC12MinInMinutesSdSgvp" class="token"><code>dailyRestMinInMinutes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum daily rest duration in minutes that must be taken.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var dailyRestMinInMinutes: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV03midbC9InMinutesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-midDriveRestInMinutes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-driverestregulation#sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV03midbC9InMinutesSdSgvp" class="token"><code>midDriveRestInMinutes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Maximum driving time in minutes allowed before a mid-drive rest must be taken.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var midDriveRestInMinutes: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV03midbC12MinInMinutesSdSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-midDriveRestMinInMinutes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-driverestregulation#sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV03midbC12MinInMinutesSdSgvp" class="token"><code>midDriveRestMinInMinutes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minimum duration in minutes of the required mid-drive rest.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var midDriveRestMinInMinutes: TimeInterval?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutes05dailyc3MinhI003midbchI00lbckhI0ACSdSg_A3Htcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-maxDailyDriveTimeInMinutes-dailyRestMinInMinutes-midDriveRestInMinutes-midDriveRestMinInMinutes" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-driverestregulation#sdk-for-ios-navigate-s-7heresdk19DriveRestRegulationV08maxDailyB13TimeInMinutes05dailyc3MinhI003midbchI00lbckhI0ACSdSg_A3Htcfc" class="token"><code>init(maxDailyDriveTimeInMinutes:</code><wbr></wbr><code>dailyRestMinInMinutes:</code><wbr></wbr><code>midDriveRestInMinutes:</code><wbr></wbr><code>midDriveRestMinInMinutes:</code><wbr></wbr><code>)</code></a> 

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
  public init(maxDailyDriveTimeInMinutes: TimeInterval? = nil, dailyRestMinInMinutes: TimeInterval? = nil, midDriveRestInMinutes: TimeInterval? = nil, midDriveRestMinInMinutes: TimeInterval? = nil)
  ```

  </div>

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

