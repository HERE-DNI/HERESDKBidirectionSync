---
title: "TranslucentMapLayerGroup Class Reference"
slug: "sdk-for-ios-navigate-classes-translucentmaplayergroup"
---

# TranslucentMapLayerGroup

<div class="declaration">

<div class="language">

``` highlight
public class TranslucentMapLayerGroup
```

``` highlight
extension TranslucentMapLayerGroup: NativeBase
```

``` highlight
extension TranslucentMapLayerGroup: Hashable
```

</div>

</div>

A translucent layer group that can be the target for

    MapLayerPriorityBuilder.inGroup(...)

. Currently, only custom line layers can be added to a translucent layer group. Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so that overlapping translucent line geometry is not alpha blended with itself. At creation, the layer group gets added to a map. The layer group gets removed from the map upon instance destruction and any layer (categories) still in the group are not rendered anymore, therefore it is recommended to keep a group alive as long as layers using the group are alive and in use.
</p>

Conceptual example to place line layers into a translucent group:

``` highlight
// Create a translucent group with a unique name and a render priority let groupPriority = MapLayerPriorityBuilder () . renderedLast () . build () let group = TranslucentMapLayerGroup ( name : "TranslucentGroupName" , map , groupPriority ) // Create a line layer to be rendered as part of the translucent group let lineLayerPriority = MapLayerPriorityBuilder () . inGroup ( "TranslucentGroupName" ) // places the line layer into the group . renderedFirst () // to be rendered first when the group is rendered . withCategory ( "SomeCategory" ) // places the line layer category 'SomeCategory' . inGroup ( "TranslucentGroupName" ) // into the group . renderedLast () // to be rendered last when the group is rendered . build () let lineLayer = MapLayerBuilder () . withDataSource ( named : "DataSourceName" , contentType : MapContentType . line ) . forMap ( map ) . withName ( "LineLayerName" ) . withPriority ( lineLayerPriority ) . withStyle ( translucentLineStyle ) // E.g. "technique": "line" ... "color": "#FFFFFF80" . build () // Create a second line layer to be rendered as part of the translucent group let secondLineLayerPriority = MapLayerPriorityBuilder () . inGroup ( "TranslucentGroupName" ) // places the second line layer into the group . renderedBeforeLayer ( "LineLayerName" ) // to be rendered before first layer // when the group is rendered . build () let secondLineLayer = MapLayerBuilder () . withDataSource ( named : "SecondDataSourceName" , contentType : MapContentType . line ) . forMap ( map ) . withName ( "SecondLineLayerName" ) . withPriority ( secondLineLayerPriority ) . withStyle ( secondTranslucentLineStyle ) // E.g. "technique": "line" ... "color": "#FFFFFF80" . build ()
```

</pre>

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-translucentmaplayergroup#/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when failing to build the group.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public typealias InstantiationError = TranslucentMapLayerGroup.ErrorDetails
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      init(name: aMap: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of the group.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-translucentmaplayergroup#/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora">`TranslucentMapLayerGroup.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( name : String , aMap : HereMap ) throws
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
  <p>Name of the group. Must be unique across <a href="sdk-for-ios-navigate-classes-maplayer"><code>MapLayer</code></a> and <code>TranslucentMapLayerGroup</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>aMap</code></em><code> </code></td>
  <td><div>
  <p>The map to attach the group to.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      init(name: aMap: _: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates an instance of the group.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-translucentmaplayergroup#/s:7heresdk24TranslucentMapLayerGroupC18InstantiationErrora">`TranslucentMapLayerGroup.InstantiationError`</a> In case of invalid input parameters.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init ( name : String , aMap : HereMap , _ priority : MapLayerPriority ) throws
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
  <p>Name of the group. Must be unique across <a href="sdk-for-ios-navigate-classes-maplayer"><code>MapLayer</code></a> and <code>TranslucentMapLayerGroup</code>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>aMap</code></em><code> </code></td>
  <td><div>
  <p>The map to attach the group to.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>priority</code></em><code> </code></td>
  <td><div>
  <p>The <a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapLayerPriorityC"><code>MapLayerPriority</code></a> which should be applied to position the group. The <a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapLayerPriorityC"><code>MapLayerPriority</code></a> must contain only one priority and this priority must have no category and no group, i.e.</p>
  <pre><code>MapLayerPriorityBuilder.inGroup(...)</code></pre>
  and
  <pre><code>MapLayerPriorityBuilder.withCategory(...)</code></pre>
  should not be used when building the <a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapLayerPriorityC"><code>MapLayerPriority</code></a>. Example:
  </p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24TranslucentMapLayerGroupC9ErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/ErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-translucentmaplayergroup#/s:7heresdk24TranslucentMapLayerGroupC9ErrorCodeO" class="token"><code>ErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error codes for creating the group.

  <a href="sdk-for-ios-navigate-classes-translucentmaplayergroup-errorcode" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum ErrorCode : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk24TranslucentMapLayerGroupC12ErrorDetailsV"></span>` `<span id="//apple_ref/swift/Struct/ErrorDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-translucentmaplayergroup#/s:7heresdk24TranslucentMapLayerGroupC12ErrorDetailsV" class="token"><code>ErrorDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the reason for failing to create the group.

  <a href="sdk-for-ios-navigate-classes-translucentmaplayergroup-errordetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct ErrorDetails
  ```

  ``` highlight
  extension TranslucentMapLayerGroup.ErrorDetails : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      setPriority(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the render priority for the layer group which replaces any previously defined priority.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setPriority ( _ priority : MapLayerPriority )
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
  <td><code> </code><em><code>priority</code></em><code> </code></td>
  <td><div>
  <p>The priority to position the group. The <a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapLayerPriorityC"><code>MapLayerPriority</code></a> must contain only one priority and this priority must have no category and no group, i.e.</p>
  <pre><code>MapLayerPriorityBuilder.inGroup(...)</code></pre>
  and
  <pre><code>MapLayerPriorityBuilder.withCategory(...)</code></pre>
  should not be used when building the <a href="sdk-for-ios-navigate-maps#/s:7heresdk16MapLayerPriorityC"><code>MapLayerPriority</code></a>. Example:
  </p>
  <p>new MapLayerPriorityBuilder().renderedAfterLayer(“water”).build()</p>
  <pre><code>MapLayerPriorityBuilder().renderedAfterLayer(named: &quot;water&quot;).build()</code></pre>
  </p>
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

