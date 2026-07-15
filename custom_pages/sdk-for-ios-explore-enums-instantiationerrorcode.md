---
title: "InstantiationErrorCode Enumeration Reference"
slug: "sdk-for-ios-explore-enums-instantiationerrorcode"
---

# InstantiationErrorCode

<div class="declaration">

<div class="language">

``` highlight
public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
```

``` highlight
extension InstantiationErrorCode : Error
```

</div>

</div>

Instantiation error.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO16illegalArgumentsyA2CmF"></span>` `<span id="//apple_ref/swift/Element/illegalArguments" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO16illegalArgumentsyA2CmF" class="token"><code>illegalArguments</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Illegal arguments.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case illegalArguments = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO6failedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/failed" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO6failedyA2CmF" class="token"><code>failed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation attempt failed. Please check log for error.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO30sharedSdkEngineNotInstantiatedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/sharedSdkEngineNotInstantiated" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO30sharedSdkEngineNotInstantiatedyA2CmF" class="token"><code>sharedSdkEngineNotInstantiated</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation attempt failed because the shared SDK engine is not instantiated. Please initialise the SDK.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sharedSdkEngineNotInstantiated
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO23cacheFolderAccessDeniedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/cacheFolderAccessDenied" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO23cacheFolderAccessDeniedyA2CmF" class="token"><code>cacheFolderAccessDenied</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access to the specified cache folder is denied

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cacheFolderAccessDenied
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO38persistentMapStorageFolderAccessDeniedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/persistentMapStorageFolderAccessDenied" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO38persistentMapStorageFolderAccessDeniedyA2CmF" class="token"><code>persistentMapStorageFolderAccessDenied</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access to the specified persistent map storage folder is denied

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case persistentMapStorageFolderAccessDenied
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO23failedToLockCacheFolderyA2CmF"></span>` `<span id="//apple_ref/swift/Element/failedToLockCacheFolder" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO23failedToLockCacheFolderyA2CmF" class="token"><code>failedToLockCacheFolder</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The cache folder for given access key id is locked by other instance of SDKNativeEngine

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failedToLockCacheFolder
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO30failedToCreateAnalyticsServiceyA2CmF"></span>` `<span id="//apple_ref/swift/Element/failedToCreateAnalyticsService" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO30failedToCreateAnalyticsServiceyA2CmF" class="token"><code>failedToCreateAnalyticsService</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Analytics service can not be created

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case failedToCreateAnalyticsService
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO30accessKeyContainsIllegalSymbolyA2CmF"></span>` `<span id="//apple_ref/swift/Element/accessKeyContainsIllegalSymbol" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO30accessKeyContainsIllegalSymbolyA2CmF" class="token"><code>accessKeyContainsIllegalSymbol</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access key contains illegal symbols. The below characters are not supported: A. ‘(single quote) B. “(double quote)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case accessKeyContainsIllegalSymbol
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO36accessKeySecretContainsIllegalSymbolyA2CmF"></span>` `<span id="//apple_ref/swift/Element/accessKeySecretContainsIllegalSymbol" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO36accessKeySecretContainsIllegalSymbolyA2CmF" class="token"><code>accessKeySecretContainsIllegalSymbol</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access key secret contains illegal symbols. The below characters are not supported: A. ‘(single quote) B. “(double quote)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case accessKeySecretContainsIllegalSymbol
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO26layerConfigurationMismatchyA2CmF"></span>` `<span id="//apple_ref/swift/Element/layerConfigurationMismatch" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO26layerConfigurationMismatchyA2CmF" class="token"><code>layerConfigurationMismatch</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Please check SDKOptions.layerConfiguration against SDK modules configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case layerConfigurationMismatch
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO24sdkEngineAlreadyDisposedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/sdkEngineAlreadyDisposed" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO24sdkEngineAlreadyDisposedyA2CmF" class="token"><code>sdkEngineAlreadyDisposed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Instantiation attempt failed because the

      dispose()

  method from <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a> was called already.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case sdkEngineAlreadyDisposed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO27invalidCatalogConfigurationyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidCatalogConfiguration" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO27invalidCatalogConfigurationyA2CmF" class="token"><code>invalidCatalogConfiguration</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  <a href="sdk-for-ios-explore-structs-catalogconfiguration">`CatalogConfiguration`</a> contains invalid parameters. Check the corectness of HRNs and versions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidCatalogConfiguration
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk22InstantiationErrorCodeO22dataFolderAccessDeniedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/dataFolderAccessDenied" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-enums-instantiationerrorcode#/s:7heresdk22InstantiationErrorCodeO22dataFolderAccessDeniedyA2CmF" class="token"><code>dataFolderAccessDenied</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access to the specified data folder is denied

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case dataFolderAccessDenied
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

