---
title: "Metadata Class Reference"
slug: "sdk-for-ios-navigate-classes-metadata"
---

# Metadata

<div class="declaration">

<div class="language">

``` highlight
public class Metadata
```

``` highlight
extension Metadata: NativeBase
```

``` highlight
extension Metadata: Hashable
```

</div>

</div>

Holds metadata on behalf of a map item. An instance of this class can contain metadata items of varying types, such as String, Integer, Double, GeoCoordinates etc. and can also hold arbitrary metadata types by the use of the CustomMetadataValue protocol.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataCACycfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataCACycfc" class="token"><code>init()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of this class.

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

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC14getCustomValue3keyAA0dbE0_pSgSS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getCustomValue-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC14getCustomValue3keyAA0dbE0_pSgSS_tF" class="token"><code>getCustomValue(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Obtains an instance of the CustomMetadataValue class associated with a given key.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getCustomValue(key: String) -> CustomMetadataValue?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-custommetadatavalue">CustomMetadataValue</a>

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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key for which to obtain the value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The value associated with the key.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC9getDouble3keySdSgSS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getDouble-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC9getDouble3keySdSgSS_tF" class="token"><code>getDouble(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Obtains a Double value associated with a given key.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getDouble(key: String) -> Double?
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key for which to obtain the value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The value associated with the key.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC17getGeoCoordinates3keyAA0dE0VSgSS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getGeoCoordinates-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC17getGeoCoordinates3keyAA0dE0VSgSS_tF" class="token"><code>getGeoCoordinates(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Obtains a GeoCoordinates value associated with a given key.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getGeoCoordinates(key: String) -> GeoCoordinates?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key for which to obtain the value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The value associated with the key.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC10getInteger3keys5Int32VSgSS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getInteger-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC10getInteger3keys5Int32VSgSS_tF" class="token"><code>getInteger(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Obtains an Integer value associated with a given key.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getInteger(key: String) -> Int32?
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key for which to obtain the value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The value associated with the key.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC9getString3keySSSgSS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getString-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC9getString3keySSSgSS_tF" class="token"><code>getString(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Obtains a String value associated with a given key.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getString(key: String) -> String?
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key for which to obtain the value.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  The value associated with the key.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC7getType3keyAA0bD0OSgSS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-getType-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC7getType3keyAA0bD0OSgSS_tF" class="token"><code>getType(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Determines the type of a metadata value. If the type of a metadata value associated with a key is not known, this method will enable the type to be queried, in order to know which get method to call. i.e. getDouble(), getInteger() etc.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getType(key: String) -> MetadataType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-metadatatype">MetadataType</a>

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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key for which to obtain the type.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  An enumeration describing the type of the value associated with the key.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC11removeValue3keyySS_tF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-removeValue-key" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC11removeValue3keyySS_tF" class="token"><code>removeValue(key:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Removes a metadata key and its associated value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func removeValue(key: String)
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key to be removed.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC14setCustomValue3key5valueySS_AA0dbE0_ptF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setCustomValue-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC14setCustomValue3key5valueySS_AA0dbE0_ptF" class="token"><code>setCustomValue(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a key:value pair, where the value is a type derived from CustomMetadataValue. If the given key already exists, its value will be replaced by the new one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setCustomValue(key: String, value: CustomMetadataValue)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-protocols-custommetadatavalue">CustomMetadataValue</a>

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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key to be created or replaced.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>The value to be assigned to the key.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC9setDouble3key5valueySS_SdtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setDouble-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC9setDouble3key5valueySS_SdtF" class="token"><code>setDouble(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a key:value pair, where the value is of type Double. If the given key already exists, its value will be replaced by the new one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setDouble(key: String, value: Double)
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key to be created or replaced.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>The value to be assigned to the key.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC17setGeoCoordinates3key5valueySS_AA0dE0VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setGeoCoordinates-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC17setGeoCoordinates3key5valueySS_AA0dE0VtF" class="token"><code>setGeoCoordinates(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a key:value pair, where the value is of type GeoCoordinates. If the given key already exists, its value will be replaced by the new one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setGeoCoordinates(key: String, value: GeoCoordinates)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a>

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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key to be created or replaced.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>The value to be assigned to the key.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC10setInteger3key5valueySS_s5Int32VtF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setInteger-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC10setInteger3key5valueySS_s5Int32VtF" class="token"><code>setInteger(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a key:value pair, where the value is of type Integer. If the given key already exists, its value will be replaced by the new one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setInteger(key: String, value: Int32)
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key to be created or replaced.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>The value to be assigned to the key.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk8MetadataC9setString3key5valueySS_SStF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-setString-key-value" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-classes-metadata#sdk-for-ios-navigate-s-7heresdk8MetadataC9setString3key5valueySS_SStF" class="token"><code>setString(key:</code><wbr></wbr><code>value:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a key:value pair, where the value is of type String. If the given key already exists, its value will be replaced by the new one.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setString(key: String, value: String)
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
  <td><code> </code><em><code>key</code></em><code> </code></td>
  <td><div>
  <p>The name of the key to be created or replaced.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>value</code></em><code> </code></td>
  <td><div>
  <p>The value to be assigned to the key.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

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

