---
title: "DataAttributesBuilder Class Reference"
slug: "sdk-for-ios-explore-classes-dataattributesbuilder"
---

# DataAttributesBuilder

<div class="declaration">

<div class="language">

``` highlight
public class DataAttributesBuilder
```

``` highlight
extension DataAttributesBuilder: NativeBase
```

``` highlight
extension DataAttributesBuilder: Hashable
```

</div>

</div>

Data attributes collection builder.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderCACycfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a data attributes builder instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init()
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SStF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-with-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SStF" class="token"><code>with(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to add the given attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func with(name: String, value: String) -> DataAttributesBuilder
  ```

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Attribute name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Attribute value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data attributes builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_s5Int64VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-with-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_s5Int64VtF" class="token"><code>with(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to add the given attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func with(name: String, value: Int64) -> DataAttributesBuilder
  ```

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Attribute name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Attribute value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data attributes builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SftF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-with-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SftF" class="token"><code>with(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to add the given attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func with(name: String, value: Float) -> DataAttributesBuilder
  ```

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Attribute name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Attribute value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data attributes builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SdtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-with-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SdtF" class="token"><code>with(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to add the given attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func with(name: String, value: Double) -> DataAttributesBuilder
  ```

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Attribute name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Attribute value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data attributes builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SbtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-with-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_SbtF" class="token"><code>with(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to add the given attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func with(name: String, value: Bool) -> DataAttributesBuilder
  ```

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Attribute name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Attribute value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data attributes builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_AA0B14AttributeValueCtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-with-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC4with4name5valueACSS_AA0B14AttributeValueCtF" class="token"><code>with(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to add the given attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func with(name: String, value: DataAttributeValue) -> DataAttributesBuilder
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-dataattributevalue">DataAttributeValue</a>

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
  <td><code> </code><em><code>name</code></em><code> </code></td>
  <td><div>
  <p>Attribute name.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>Attribute value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  This data attributes builder instance.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC5buildAA0bC0CyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-build" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesbuilder#sdk-for-ios-explore-s-7heresdk21DataAttributesBuilderC5buildAA0bC0CyF" class="token"><code>build()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Builds instance of DataAttributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build() -> DataAttributes
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-dataattributes">DataAttributes</a>

  </div>

  <div>

  #### Return Value

  Instance of the data attributes created with the given attributes.

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

