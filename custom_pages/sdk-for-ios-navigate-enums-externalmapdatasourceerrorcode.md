---
title: "ExternalMapDataSourceErrorCode Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode"
---

# ExternalMapDataSourceErrorCode

<div class="declaration">

<div class="language">

``` highlight
public enum ExternalMapDataSourceErrorCode : UInt32, CaseIterable, Codable
```

``` highlight
extension ExternalMapDataSourceErrorCode : Error
```

</div>

</div>

Describes the reason for failing to configure <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a> with external map data source. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO08internalF0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/internalError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode#/s:7heresdk30ExternalMapDataSourceErrorCodeO08internalF0yA2CmF" class="token"><code>internalError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Internal error occurred.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case internalError = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO010addCatalogF0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/addCatalogError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode#/s:7heresdk30ExternalMapDataSourceErrorCodeO010addCatalogF0yA2CmF" class="token"><code>addCatalogError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error while adding catalog to `DataStoreClient`. Verify the same catalogs are added to the `DataStoreServer` instance on the server side.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case addCatalogError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO18invalidCredentialsyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidCredentials" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode#/s:7heresdk30ExternalMapDataSourceErrorCodeO18invalidCredentialsyA2CmF" class="token"><code>invalidCredentials</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error while checking credentials. E.g. some field is empty but expected not empty

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidCredentials
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO015serviceRegisterF0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/serviceRegisterError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode#/s:7heresdk30ExternalMapDataSourceErrorCodeO015serviceRegisterF0yA2CmF" class="token"><code>serviceRegisterError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error while attempting to register OCM AM service

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serviceRegisterError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO014clientDisposedF0yA2CmF"></span>` `<span id="//apple_ref/swift/Element/clientDisposedError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode#/s:7heresdk30ExternalMapDataSourceErrorCodeO014clientDisposedF0yA2CmF" class="token"><code>clientDisposedError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  While attempting to register the connection, the client was being disposed

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case clientDisposedError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk30ExternalMapDataSourceErrorCodeO17serverUnavailableyA2CmF"></span>` `<span id="//apple_ref/swift/Element/serverUnavailable" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-externalmapdatasourceerrorcode#/s:7heresdk30ExternalMapDataSourceErrorCodeO17serverUnavailableyA2CmF" class="token"><code>serverUnavailable</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This means that server is not launched or configuration settings is wrong. Make sense only on client side

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serverUnavailable
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

