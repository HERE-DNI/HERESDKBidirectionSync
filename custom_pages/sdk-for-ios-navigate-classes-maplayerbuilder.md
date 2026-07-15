---
title: "MapLayerBuilder Class Reference"
slug: "sdk-for-ios-navigate-classes-maplayerbuilder"
---

# MapLayerBuilder

<div class="declaration">

<div class="language">

``` highlight
public class MapLayerBuilder
```

``` highlight
extension MapLayerBuilder: NativeBase
```

``` highlight
extension MapLayerBuilder: Hashable
```

</div>

</div>

MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.

For example, after loading a scene configuration file, the renderer is setup to draw layers in the following order:

- background
- water
- roads:outline
- roads
- labels

Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer’s default, main category is unnamed.

The concept of ‘category’ is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category ‘bridges’ and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer differently then it should opt for a layer with only the default category (e.g. for a raster layer, only the default category makes sense, since the layer has no other stylable elements apart from the raster image).

A new layer called ‘zone’ and its category ‘background’ can be added dynamically so that the rendering order gets modified in the following way:

- background
- water
- zone:background
- zone
- roads:outline
- roads
- labels

This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the following example:

``` highlight
let layerPriority = MapLayerPriorityBuilder () . renderedAfterLayer ( named : "water" ) // places main category after 'water' . withCategory ( "background" ) . renderedAfterLayer ( named : "water" ) // places 'background' category after 'water' and before the // layer's main category. . build (); let layer = MapLayerBuilder () . withDataSource ( named : "DataSourceName" , contentType : MapContentType . line ) . forMap ( map ) . withName ( "zone" ) . withPriority ( layerPriority ) . build ();
```

</pre>

In case no layer priority or an empty one is provided, or if a reference layer-category pair is not present in the rendering order, the layer is going to be rendered last with respect to the rendering order at the time of its creation.

Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers. All labels will be rendered within the “labels” layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

- ‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
- ‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed to overlap with other labels of the same categoty and block map labels.
- ‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of content: point, line, polygon.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk15MapLayerBuilderC18InstantiationErrora"></span>` `<span id="//apple_ref/swift/Alias/InstantiationError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-maplayerbuilder#/s:7heresdk15MapLayerBuilderC18InstantiationErrora" class="token"><code>InstantiationError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Thrown when failing to build a <a href="sdk-for-ios-navigate-classes-maplayer">`MapLayer`</a>.

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

  Creates an instance of the layer builder interface.

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

  ` `<span id="/s:7heresdk15MapLayerBuilderC22InstantiationErrorCodeO"></span>` `<span id="//apple_ref/swift/Enum/InstantiationErrorCode" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-maplayerbuilder#/s:7heresdk15MapLayerBuilderC22InstantiationErrorCodeO" class="token"><code>InstantiationErrorCode</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes a reason for failing to build a <a href="sdk-for-ios-navigate-classes-maplayer">`MapLayer`</a>.

  <a href="sdk-for-ios-navigate-classes-maplayerbuilder-instantiationerrorcode" class="slightly-smaller">See more</a>

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

  ` `<span id="/s:7heresdk15MapLayerBuilderC25InstantiationErrorDetailsV"></span>` `<span id="//apple_ref/swift/Struct/InstantiationErrorDetails" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-maplayerbuilder#/s:7heresdk15MapLayerBuilderC25InstantiationErrorDetailsV" class="token"><code>InstantiationErrorDetails</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Describes the reason for failing to build a <a href="sdk-for-ios-navigate-classes-maplayer">`MapLayer`</a>.

  <a href="sdk-for-ios-navigate-classes-maplayerbuilder-instantiationerrordetails" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public struct InstantiationErrorDetails
  ```

  ``` highlight
  extension MapLayerBuilder.InstantiationErrorDetails : Error
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      withName(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures builder to use the given name as a layer name. The name is a mandatory layer creation parameter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withName ( _ name : String ) -> MapLayerBuilder
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
  <p>Name of the layer. Must be unique.</p>
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

      withDataSource(named: contentType: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to use a data source with the given name as the source of data for the layer. The datasource name and content type are mandatory layer creation parameters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withDataSource ( named dataSourceName : String , contentType : MapContentType ) -> MapLayerBuilder
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
  <td><code> </code><em><code>dataSourceName</code></em><code> </code></td>
  <td><div>
  <p>Name of the data source.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>contentType</code></em><code> </code></td>
  <td><div>
  <p>The renderable content type supplied by the data source.</p>
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

      withStyle(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to use a style. Providing a style during layer creation is not mandatory. The style can also be set/updated after the layer creation. For more details see Custom Layer Style Reference in the documentation. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withStyle ( _ style : Style ) -> MapLayerBuilder
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
  <td><code> </code><em><code>style</code></em><code> </code></td>
  <td><div>
  <p>Style for the layer.</p>
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

      forMap(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to display a layer in the given map. The map is a mandatory layer creation parameter.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func forMap ( _ targetMap : HereMap ) -> MapLayerBuilder
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
  <td><code> </code><em><code>targetMap</code></em><code> </code></td>
  <td><div>
  <p>The map.</p>
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

      withPriority(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to set the MapLayerPriority to be used by the layer.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withPriority ( _ priority : MapLayerPriority ) -> MapLayerBuilder
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
  <p>MapLayerPriority which should be applied to the layer.</p>
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

      withVisibilityRange(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to set the layer visible in the given zoom levels range. Values outside the map zoom level range (0, 24) will be ignored. Providing the visibility range is optional. If not provided, the layer will be visible on all zoom levels.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withVisibilityRange ( _ visibilityRange : MapLayerVisibilityRange ) -> MapLayerBuilder
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
  <td><code> </code><em><code>visibilityRange</code></em><code> </code></td>
  <td><div>
  <p>Visibility range which should be applied to the layer.</p>
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

      withMapMeasureDependentStorageLevels(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Applies a mapping from the map measure to the storage level. This mapping is used by the layer to request data for the specified storage level corresponding to the map measure from the datasource. This can be used for example to fine-tune the resolution of raster layers. Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon. Note: Mappings that request higher storage levels will lead to an increased number of requests to the raster tile service. Providing the map measure to storage level mapping is optional. If not provided, the default mapping will use a storage level that is for raster layers one and for others three levels lower than the zoom level, corresponding to an offset of -1 and -3.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withMapMeasureDependentStorageLevels ( _ mapLayerMapMeasureDependentStorageLevels : MapLayerMapMeasureDependentStorageLevels ) -> MapLayerBuilder
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
  <td><code> </code><em><code>mapLayerMapMeasureDependentStorageLevels</code></em><code> </code></td>
  <td><div>
  <p>The map measure to storage level mapping that should be applied for the layer.</p>
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

      withLoadPriority(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Configures the builder to set the layer load priority. Higher load priority values lead to layer being scheduled for loading before layers with lesser values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withLoadPriority ( _ loadPriority : Double ) -> MapLayerBuilder
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
  <td><code> </code><em><code>loadPriority</code></em><code> </code></td>
  <td><div>
  <p>Load priority for layer.</p>
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

  Constructs, registers and configures a new map layer showing specified content type according to the configured parameters. After this call this instance is reset to the initial state. It could be used to build another map layer, but will not keep any previously configured properties.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-classes-maplayerbuilder#/s:7heresdk15MapLayerBuilderC18InstantiationErrora">`MapLayerBuilder.InstantiationError`</a> Indicates an instantiation issue.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build () throws -> MapLayer
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  A new MapLayer instance.

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

