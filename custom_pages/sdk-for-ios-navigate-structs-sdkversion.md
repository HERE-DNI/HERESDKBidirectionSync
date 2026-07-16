---
title: "SDKVersion Structure Reference"
slug: "sdk-for-ios-navigate-structs-sdkversion"
---

# SDKVersion

<div class="declaration">

<div class="language">

``` highlight
public struct SDKVersion : Hashable
```

</div>

</div>

The `SDKVersion` represents version information for an SDK product. It encapsulates various attributes related to the version, including product variant, version details and backend configuration. Please note, `sdk.core.engine.SDKBuildInformation` can be used to get `SDKVersion`.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV14productVariantSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-productVariant" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV14productVariantSSvp" class="token"><code>productVariant</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Product variant.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var productVariant: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV11versionNameSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionName" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV11versionNameSSvp" class="token"><code>versionName</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Version information as string.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionName: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV17versionGenerations5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionGeneration" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV17versionGenerations5Int32Vvp" class="token"><code>versionGeneration</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Generation number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionGeneration: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionMajors5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionMajor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionMajors5Int32Vvp" class="token"><code>versionMajor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Major version number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionMajor: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionMinors5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionMinor" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionMinors5Int32Vvp" class="token"><code>versionMinor</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Minor version number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionMinor: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionPatchs5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionPatch" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionPatchs5Int32Vvp" class="token"><code>versionPatch</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Patch number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionPatch: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionBuilds5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionBuild" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV12versionBuilds5Int32Vvp" class="token"><code>versionBuild</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Build number.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionBuild: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV10versionTagSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-versionTag" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV10versionTagSSvp" class="token"><code>versionTag</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Version tag.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var versionTag: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV13backendConfigSSvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-backendConfig" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV13backendConfigSSvp" class="token"><code>backendConfig</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Backend config

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var backendConfig: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk10SDKVersionV14productVariant11versionName0E10Generation0E5Major0E5Minor0E5Patch0E5Build0E3Tag13backendConfigACSS_SSs5Int32VA4NS2Stcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-productVariant-versionName-versionGeneration-versionMajor-versionMinor-versionPatch-versionBuild-versionTag-backendConfig" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-sdkversion#sdk-for-ios-navigate-s-7heresdk10SDKVersionV14productVariant11versionName0E10Generation0E5Major0E5Minor0E5Patch0E5Build0E3Tag13backendConfigACSS_SSs5Int32VA4NS2Stcfc" class="token"><code>init(productVariant:</code><wbr></wbr><code>versionName:</code><wbr></wbr><code>versionGeneration:</code><wbr></wbr><code>versionMajor:</code><wbr></wbr><code>versionMinor:</code><wbr></wbr><code>versionPatch:</code><wbr></wbr><code>versionBuild:</code><wbr></wbr><code>versionTag:</code><wbr></wbr><code>backendConfig:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new SDK version instance from the provided parameter values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(productVariant: String, versionName: String, versionGeneration: Int32, versionMajor: Int32, versionMinor: Int32, versionPatch: Int32, versionBuild: Int32, versionTag: String, backendConfig: String)
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

