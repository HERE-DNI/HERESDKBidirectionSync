---
title: "Metadata Class Reference"
slug: "sdk-for-ios-explore-classes-metadata"
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

      init()

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
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      getCustomValue(key: )

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
  public func getCustomValue ( key : String ) -> CustomMetadataValue ?
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

      getDouble(key: )

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
  public func getDouble ( key : String ) -> Double ?
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

      getGeoCoordinates(key: )

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
  public func getGeoCoordinates ( key : String ) -> GeoCoordinates ?
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

      getInteger(key: )

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
  public func getInteger ( key : String ) -> Int32 ?
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

      getString(key: )

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
  public func getString ( key : String ) -> String ?
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

      getType(key: )

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
  public func getType ( key : String ) -> MetadataType ?
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

      removeValue(key: )

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
  public func removeValue ( key : String )
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

      setCustomValue(key: value: )

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
  public func setCustomValue ( key : String , value : CustomMetadataValue )
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

      setDouble(key: value: )

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
  public func setDouble ( key : String , value : Double )
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

      setGeoCoordinates(key: value: )

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
  public func setGeoCoordinates ( key : String , value : GeoCoordinates )
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

      setInteger(key: value: )

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
  public func setInteger ( key : String , value : Int32 )
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

      setString(key: value: )

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
  public func setString ( key : String , value : String )
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

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

