---
title: "DataAttributeValue Class Reference"
slug: "sdk-for-ios-explore-classes-dataattributevalue"
---

# DataAttributeValue

<div class="declaration">

<div class="language">

``` highlight
public class DataAttributeValue
```

``` highlight
extension DataAttributeValue: NativeBase
```

``` highlight
extension DataAttributeValue: Hashable
```

</div>

</div>

Encapsulates a data attribute value. Supports basic types and arrays of basic types.

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a string data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : String )
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

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a 64-bit integer data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : Int64 )
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

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a single precision floating decimal data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : Float )
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

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a double precision floating decimal data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : Double )
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

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a boolean data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : Bool )
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

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a color data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : UIColor )
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

      init(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an aggregated data attribute value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( _ value : [ DataAttributeValue ])
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

  ` `<span id="/s:7heresdk18DataAttributeValueC0D4TypeO"></span>` `<span id="//apple_ref/swift/Enum/ValueType" class="dashAnchor"></span>` `<a href="sdk-for-ios-explore-classes-dataattributevalue#/s:7heresdk18DataAttributeValueC0D4TypeO" class="token"><code>ValueType</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Supported types of the data attribute values.

  <a href="sdk-for-ios-explore-classes-dataattributevalue-valuetype" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ValueType : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      getType()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns the type of the value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getType () -> DataAttributeValue . ValueType
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  The type of the value.

  </div>

  </div>

  </div>

- <div>

      getString()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the string value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getString () -> String ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getInt64()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets 64-bits integer value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getInt64 () -> Int64 ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getFloat()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the single precision floating decimal value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getFloat () -> Float ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getDouble()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the double precision floating decimal value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getDouble () -> Double ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getBoolean()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the boolean value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getBoolean () -> Bool ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getColor()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the color value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getColor () -> UIColor ?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getArray()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the array value or `nil` if the type doesn’t match.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getArray () -> [ DataAttributeValue ]?
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

  </div>

  </div>

  </div>

- <div>

      getAsString()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a string representation of the contained value.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getAsString () -> String
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Attribute value.

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

