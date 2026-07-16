---
title: "DataAttributesAccessor Class Reference"
slug: "sdk-for-ios-explore-classes-dataattributesaccessor"
---

# DataAttributesAccessor

<div class="declaration">

<div class="language">

``` highlight
public class DataAttributesAccessor : DataAttributesBase
```

``` highlight
extension DataAttributesAccessor: NativeBase
```

``` highlight
extension DataAttributesAccessor: Hashable
```

</div>

Related types:

- <a href="sdk-for-ios-explore-protocols-dataattributesbase">DataAttributesBase</a>

</div>

Accessor used for manipulating data attributes.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC17getAttributeNamesSaySSGyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getAttributeNames" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC17getAttributeNamesSaySSGyF" class="token"><code>getAttributeNames()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a list of attribute names.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getAttributeNames() -> [String]
  ```

  </div>

  </div>

  <div>

  #### Return Value

  The list of attribute names.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12getValueTypeyAA0b9AttributeF0C0fG0OSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getValueType-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12getValueTypeyAA0b9AttributeF0C0fG0OSgSSF" class="token"><code>getValueType(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the value type of an attribute or `nil` if it is not contained.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getValueType(_ name: String) -> DataAttributeValue.ValueType?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value type or `nil` if it is not contained.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC11getAsStringySSSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getAsString-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC11getAsStringySSSgSSF" class="token"><code>getAsString(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the value of an attribute as a string or `nil` if it is not contained.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getAsString(_ name: String) -> String?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC9getStringySSSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getString-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC9getStringySSSgSSF" class="token"><code>getString(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the value of a string attribute or `nil` if it is not contained or the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getString(_ name: String) -> String?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC8getInt64ys0F0VSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getInt64-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC8getInt64ys0F0VSgSSF" class="token"><code>getInt64(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the value of a 64-bits integer attribute or `nil` if it is not contained or the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getInt64(_ name: String) -> Int64?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC8getFloatySfSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getFloat-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC8getFloatySfSgSSF" class="token"><code>getFloat(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the value of a single precision floating decimal attribute or `nil` if it is not contained or the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getFloat(_ name: String) -> Float?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC9getDoubleySdSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getDouble-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC9getDoubleySdSgSSF" class="token"><code>getDouble(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the value of a double precision floating decimal attribute or `nil` if it is not contained or the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getDouble(_ name: String) -> Double?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC10getBooleanySbSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getBoolean-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC10getBooleanySbSgSSF" class="token"><code>getBoolean(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the value of a boolean attribute or `nil` if it is not contained or the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBoolean(_ name: String) -> Bool?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC8getValueyAA0b9AttributeF0CSgSSF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getValue-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC8getValueyAA0b9AttributeF0CSgSSF" class="token"><code>getValue(_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the DataAttributeValue or `nil` if it is not contained.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getValue(_ name: String) -> DataAttributeValue?
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
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SStF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SStF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces a string attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: String)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_s5Int64VtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_s5Int64VtF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces a 64-bits integer attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: Int64)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SftF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SftF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces a single precision floating decimal attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: Float)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SdtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SdtF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces a double precision floating decimal attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: Double)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SbtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_SbtF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces a boolean attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: Bool)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_So7UIColorCtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_So7UIColorCtF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces a color attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: UIColor)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_AA0B14AttributeValueCtF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-addOrReplace-name-value" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC12addOrReplace4name5valueySS_AA0B14AttributeValueCtF" class="token"><code>addOrReplace(name:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Adds or replaces an attribute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func addOrReplace(name: String, value: DataAttributeValue)
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

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC6remove4nameySS_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-remove-name" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC6remove4nameySS_tF" class="token"><code>remove(name:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes an attribute by name.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func remove(name: String)
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
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC9removeAllyyF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-removeAll" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-dataattributesaccessor#sdk-for-ios-explore-s-7heresdk22DataAttributesAccessorC9removeAllyyF" class="token"><code>removeAll()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes all attributes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeAll()
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

