---
title: "RoutingConnectionSettings Structure Reference"
slug: "sdk-for-ios-navigate-structs-routingconnectionsettings"
---

# RoutingConnectionSettings

<div class="declaration">

<div class="language">

``` highlight
public struct RoutingConnectionSettings : Hashable
```

</div>

</div>

Defines the settings for the retry logic when connecting to the HERE routing backend.

When a timeout is triggered, the next connection attempt starts with a increased timeout. new_timeout = initial_timeout + increment \* retry_count

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV07initialC7TimeoutSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-initialConnectionTimeout" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingconnectionsettings#sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV07initialC7TimeoutSdvp" class="token"><code>initialConnectionTimeout</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the initial time out for connection to the backend. By default, the initial connection timeout is 5 seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var initialConnectionTimeout: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV30connectionTimeoutRetryIncreaseSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-connectionTimeoutRetryIncrease" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingconnectionsettings#sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV30connectionTimeoutRetryIncreaseSdvp" class="token"><code>connectionTimeoutRetryIncrease</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the increase of the timeout for the transfer of data. By default, the initial connection increment per timeout 10 seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var connectionTimeoutRetryIncrease: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV22initialTransferTimeoutSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-initialTransferTimeout" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingconnectionsettings#sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV22initialTransferTimeoutSdvp" class="token"><code>initialTransferTimeout</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the initial time out for data transfer from the backend. By default, the initial transfer timeout is 10 seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var initialTransferTimeout: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV28transferTimeoutRetryIncreaseSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-transferTimeoutRetryIncrease" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingconnectionsettings#sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV28transferTimeoutRetryIncreaseSdvp" class="token"><code>transferTimeoutRetryIncrease</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the increase of the timeout for the connection. By default, the initial transfer increment per timeout is 2 seconds.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var transferTimeoutRetryIncrease: TimeInterval
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV13maxRetryCounts5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-maxRetryCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingconnectionsettings#sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV13maxRetryCounts5Int32Vvp" class="token"><code>maxRetryCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines the max amount of retries before the route request failes with connection related error codes. By default, the max amount of retries is 3.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var maxRetryCount: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV07initialC7Timeout010connectionF13RetryIncrease0e8TransferF008transferfhI003maxH5CountACSd_S3ds5Int32Vtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-initialConnectionTimeout-connectionTimeoutRetryIncrease-initialTransferTimeout-transferTimeoutRetryIncrease-maxRetryCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-routingconnectionsettings#sdk-for-ios-navigate-s-7heresdk25RoutingConnectionSettingsV07initialC7Timeout010connectionF13RetryIncrease0e8TransferF008transferfhI003maxH5CountACSd_S3ds5Int32Vtcfc" class="token"><code>init(initialConnectionTimeout:</code><wbr></wbr><code>connectionTimeoutRetryIncrease:</code><wbr></wbr><code>initialTransferTimeout:</code><wbr></wbr><code>transferTimeoutRetryIncrease:</code><wbr></wbr><code>maxRetryCount:</code><wbr></wbr><code>)</code></a> 

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
  public init(initialConnectionTimeout: TimeInterval = 5, connectionTimeoutRetryIncrease: TimeInterval = 10, initialTransferTimeout: TimeInterval = 10, transferTimeoutRetryIncrease: TimeInterval = 2, maxRetryCount: Int32 = 3)
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

