---
title: "JsonStyleFactory Class Reference"
slug: "sdk-for-ios-explore-classes-jsonstylefactory"
---

# JsonStyleFactory

<div class="declaration">

<div class="language">

``` highlight
public class JsonStyleFactory
```

``` highlight
extension JsonStyleFactory: NativeBase
```

``` highlight
extension JsonStyleFactory: Hashable
```

</div>

</div>

A factory of <a href="sdk-for-ios-explore-classes-style">`Style`</a> objects from styles defined in JSON format. For more details see Custom Layer Style Reference in the documentation.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC18InstantiationErrora"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Alias-InstantiationError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-jsonstylefactory#sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC18InstantiationErrora" class="token"><code>InstantiationError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when failing to create a <a href="sdk-for-ios-explore-classes-style">`Style`</a> from a JSON source.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = InstantiationErrorDetails
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrordetails">InstantiationErrorDetails</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC22InstantiationErrorCodeO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-InstantiationErrorCode" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-jsonstylefactory#sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes reasons for failing to create a <a href="sdk-for-ios-explore-classes-style">`Style`</a> from a JSON source.

  <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrorcode" class="slightly-smaller">See more</a>

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

   <span id="sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC25InstantiationErrorDetailsV"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Struct-InstantiationErrorDetails" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-jsonstylefactory#sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC25InstantiationErrorDetailsV" class="token"><code>InstantiationErrorDetails</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the reason for failing to create a <a href="sdk-for-ios-explore-classes-style">`Style`</a> from a JSON source.

  <a href="sdk-for-ios-explore-classes-jsonstylefactory-instantiationerrordetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstantiationErrorDetails
  ```

  ``` highlight
  extension JsonStyleFactory.InstantiationErrorDetails : Error
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-jsonstylefactory">JsonStyleFactory</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC16createFromStringyAA0C0CSSKFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-createFromString-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-jsonstylefactory#sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC16createFromStringyAA0C0CSSKFZ" class="token"><code>createFromString(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of Style from a JSON string.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-classes-jsonstylefactory#sdk-for-ios-explore-s-7heresdk16JsonStyleFactoryC18InstantiationErrora">`JsonStyleFactory.InstantiationError`</a> Indicates failure to create <a href="sdk-for-ios-explore-classes-style">`Style`</a> from JSON string.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func createFromString(_ styleString: String) throws -> Style
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-style">Style</a>

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
  <td><code> </code><em><code>styleString</code></em><code> </code></td>
  <td><div>
  <p>JSON style string.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Style instance.

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

