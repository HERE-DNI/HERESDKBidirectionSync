---
title: "DataAttributesBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-dataattributesbuilder"
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

      init()

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
  public init ()
  ```

  </pre>

  </div>

  </div>

  </div>

  </div>

- <div>

      with(name: value: )

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
  public func with ( name : String , value : String ) -> DataAttributesBuilder
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

      with(name: value: )

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
  public func with ( name : String , value : Int64 ) -> DataAttributesBuilder
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

      with(name: value: )

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
  public func with ( name : String , value : Float ) -> DataAttributesBuilder
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

      with(name: value: )

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
  public func with ( name : String , value : Double ) -> DataAttributesBuilder
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

      with(name: value: )

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
  public func with ( name : String , value : Bool ) -> DataAttributesBuilder
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

      with(name: value: )

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
  public func with ( name : String , value : DataAttributeValue ) -> DataAttributesBuilder
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

      build()

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
  public func build () -> DataAttributes
  ```

  </pre>

  </div>

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

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

