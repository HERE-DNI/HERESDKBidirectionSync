---
title: "LocationEngineStatus Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-locationenginestatus"
---

# LocationEngineStatus

<div class="declaration">

<div class="language">

``` highlight
public enum LocationEngineStatus : UInt32, CaseIterable, Codable
```

</div>

</div>

Indicates the status of the LocationEngine.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO13engineStartedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-engineStarted" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO13engineStartedyA2CmF" class="token"><code>engineStarted</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  LocationEngine successfully started.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case engineStarted
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-alreadyStarted" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO14alreadyStartedyA2CmF" class="token"><code>alreadyStarted</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tried to start LocationEngine that is already started.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case alreadyStarted
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO13engineStoppedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-engineStopped" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO13engineStoppedyA2CmF" class="token"><code>engineStopped</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  LocationEngine has been stopped.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case engineStopped
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO11startFailedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-startFailed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO11startFailedyA2CmF" class="token"><code>startFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Start failed due to an internal error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case startFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO21userConsentNotHandledyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-userConsentNotHandled" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO21userConsentNotHandledyA2CmF" class="token"><code>userConsentNotHandled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  User consent has not been handled yet.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case userConsentNotHandled
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO18missingPermissionsyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-missingPermissions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO18missingPermissionsyA2CmF" class="token"><code>missingPermissions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Missing one or more user permissions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case missingPermissions
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO20authenticationFailedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-authenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO20authenticationFailedyA2CmF" class="token"><code>authenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Authentication failed. Check your credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case authenticationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO12notSupportedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-notSupported" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO12notSupportedyA2CmF" class="token"><code>notSupported</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Request is not supported.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case notSupported
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO10notAllowedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-notAllowed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO10notAllowedyA2CmF" class="token"><code>notAllowed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Request is not supported in current region.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case notAllowed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO8notReadyyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-notReady" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO8notReadyyA2CmF" class="token"><code>notReady</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Engine is not ready for the requested action.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case notReady
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO24locationServicesDisabledyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-locationServicesDisabled" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO24locationServicesDisabledyA2CmF" class="token"><code>locationServicesDisabled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Location services are disabled in the system settings.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case locationServicesDisabled
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO24privacyNoticeUnconfirmedyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-privacyNoticeUnconfirmed" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO24privacyNoticeUnconfirmedyA2CmF" class="token"><code>privacyNoticeUnconfirmed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Method confirmHEREPrivacyNoticeInclusion() (or alternatively confirmHEREPrivacyNoticeException()) was not called before starting the <a href="sdk-for-ios-navigate-classes-locationengine">`LocationEngine`</a> or HERE privacy notice exception was not permitted.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case privacyNoticeUnconfirmed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO2okyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-ok" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-locationenginestatus#sdk-for-ios-navigate-s-7heresdk20LocationEngineStatusO2okyA2CmF" class="token"><code>ok</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Requested operation succeeded.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case ok
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

