---
title: "MapSceneLoadOptionsBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder"
---

# MapSceneLoadOptionsBuilder

<div class="declaration">

<div class="language">

``` highlight
public class MapSceneLoadOptionsBuilder
```

``` highlight
extension MapSceneLoadOptionsBuilder: NativeBase
```

``` highlight
extension MapSceneLoadOptionsBuilder: Hashable
```

</div>

</div>

Builder for creating <a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC">`MapSceneLoadOptions`</a> instances. This builder ensures that either a MapScheme or a configuration file is set, but not both.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk26MapSceneLoadOptionsBuilderC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder#/s:7heresdk26MapSceneLoadOptionsBuilderC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when failing to build a <a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC">`MapSceneLoadOptions`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorDetails
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26MapSceneLoadOptionsBuilderC22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder#/s:7heresdk26MapSceneLoadOptionsBuilderC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to build a <a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC">`MapSceneLoadOptions`</a>.

  <a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder-instantiationerrorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum InstantiationErrorCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk26MapSceneLoadOptionsBuilderC25InstantiationErrorDetailsV"></span>` `<span id="//apple_ref/swift/Struct/InstantiationErrorDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder#/s:7heresdk26MapSceneLoadOptionsBuilderC25InstantiationErrorDetailsV" class="token"><code>InstantiationErrorDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the reason for failing to build a <a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC">`MapSceneLoadOptions`</a>.

  <a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder-instantiationerrordetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstantiationErrorDetails
  ```

  ``` highlight
  extension MapSceneLoadOptionsBuilder.InstantiationErrorDetails : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      withMapScheme(mapScheme: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the map scheme to load. Any configuration file set through

      MapSceneLoadOptionsBuilder.withConfigurationFile(...)

  will be discarded.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withMapScheme ( mapScheme : MapScheme ) -> MapSceneLoadOptionsBuilder
  ```

  </pre>

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
  <td><code> </code><em><code>mapScheme</code></em><code> </code></td>
  <td><div>
  <p>Map scheme to load.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      withConfigurationFile(configurationFile: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the configuration file path to load. Any map scheme set through

      MapSceneLoadOptionsBuilder.withMapScheme(...)

  will be discarded.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withConfigurationFile ( configurationFile : String ) -> MapSceneLoadOptionsBuilder
  ```

  </pre>

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
  <td><code> </code><em><code>configurationFile</code></em><code> </code></td>
  <td><div>
  <p>Configuration file path to load.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      withEnabledFeatures(enabledFeatures: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the features to enable in the new configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withEnabledFeatures ( enabledFeatures : [ String : String ]) -> MapSceneLoadOptionsBuilder
  ```

  </pre>

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
  <td><code> </code><em><code>enabledFeatures</code></em><code> </code></td>
  <td><div>
  <p>Features to enable. Key = feature name, value = mode name.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      withDisabledFeatures(disabledFeatures: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the features to disable in the new configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withDisabledFeatures ( disabledFeatures : [ String ]) -> MapSceneLoadOptionsBuilder
  ```

  </pre>

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
  <td><code> </code><em><code>disabledFeatures</code></em><code> </code></td>
  <td><div>
  <p>Features to disable.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      withWatermarkStyle(watermarkStyle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the watermark style.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withWatermarkStyle ( watermarkStyle : WatermarkStyle ) -> MapSceneLoadOptionsBuilder
  ```

  </pre>

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
  <td><code> </code><em><code>watermarkStyle</code></em><code> </code></td>
  <td><div>
  <p>Watermark style to use.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      withOverridingMapStyle(overridingMapStyle: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the style to override what is defined in the scene configuration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withOverridingMapStyle ( overridingMapStyle : Style ) -> MapSceneLoadOptionsBuilder
  ```

  </pre>

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
  <td><code> </code><em><code>overridingMapStyle</code></em><code> </code></td>
  <td><div>
  <p>Map style to override the scene configuration.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      build()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds the <a href="sdk-for-ios-navigate-maps#/s:7heresdk19MapSceneLoadOptionsC">`MapSceneLoadOptions`</a> instance.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-mapsceneloadoptionsbuilder#/s:7heresdk26MapSceneLoadOptionsBuilderC18InstantiationErrora">`MapSceneLoadOptionsBuilder.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build () throws -> MapSceneLoadOptions
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  A new MapSceneLoadOptions instance.

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

