---
title: "WarnerEngine  Reference"
slug: "sdk-for-ios-navigate-warnerengine"
---

# WarnerEngine

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13CustomWarningV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-CustomWarning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk13CustomWarningV" class="token"><code>CustomWarning</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  struct container for custom warning data.

  This structure represents the type-specific payload associated with a custom warning.

  Instances of this structure are typically produced by custom warning evaluation logic and may also be retrieved from the `WarningRegistry`.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-customwarning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct CustomWarning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk21CustomWarningProviderP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-CustomWarningProvider" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk21CustomWarningProviderP" class="token"><code>CustomWarningProvider</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A protocol representing a provider of custom warnings based on vehicle position.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-customwarningprovider" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol CustomWarningProvider : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk7WarningV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-Warning" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk7WarningV" class="token"><code>Warning</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct which represents a warning.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-warning" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct Warning : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk12WarnerEngineC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-WarnerEngine" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk12WarnerEngineC" class="token"><code>WarnerEngine</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Provides the core functionality for generating and managing navigation warnings.

  `WarnerEngine` processes Electronic Horizon data and determines when various types of warnings should be issued. It is used with <a href="sdk-for-ios-navigate-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a>, which supply the road topology and positional updates required for warning evaluation.

  The engine monitors enabled warning types and notifies registered listeners when new warnings become available.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-warnerengine" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class WarnerEngine : ElectronicHorizonDelegate
  ```

  ``` highlight
  extension WarnerEngine: NativeBase
  ```

  ``` highlight
  extension WarnerEngine: Hashable
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-electronichorizondelegate">ElectronicHorizonDelegate</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk15WarningDelegateP"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Protocol-WarningDelegate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk15WarningDelegateP" class="token"><code>WarningDelegate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A generic listener interface protocol for receiving warning notifications.

  Implementations of this interface are notified whenever the <a href="sdk-for-ios-navigate-classes-warnerengine">`WarnerEngine`</a> detects new warnings. The listener receives a list of <a href="sdk-for-ios-navigate-structs-warning">`Warning`</a> objects, each describing a specific event or condition that requires user attention.

  Classes interested in warning updates should implement this listener and register themselves via `WarnerEngine.addWarningListener`.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-protocols-warningdelegate" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public protocol WarningDelegate : AnyObject
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk14WarningOptionsV"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Struct-WarningOptions" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk14WarningOptionsV" class="token"><code>WarningOptions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A struct with options to configure <a href="sdk-for-ios-navigate-classes-warnerengine#sdk-for-ios-navigate-s-7heresdk12WarnerEngineC14warningOptionsAA07WarningE0Vvp">`WarnerEngine.warningOptions`</a>

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-structs-warningoptions" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct WarningOptions : Hashable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Class-WarningsRegistry" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-warnerengine#sdk-for-ios-navigate-s-7heresdk16WarningsRegistryC" class="token"><code>WarningsRegistry</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A class that store warning metadata for different warning types. Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.). Provided by <a href="sdk-for-ios-navigate-classes-warnerengine">`WarnerEngine`</a> so callers can lookup detailed information about specific warnings.

  **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

  <a href="sdk-for-ios-navigate-classes-warningsregistry" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public class WarningsRegistry
  ```

  ``` highlight
  extension WarningsRegistry: NativeBase
  ```

  ``` highlight
  extension WarningsRegistry: Hashable
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

