---
title: "MapLayerPriorityBuilder Class Reference"
slug: "sdk-for-ios-explore-classes-maplayerprioritybuilder"
---

# MapLayerPriorityBuilder

<div class="declaration">

<div class="language">

``` highlight
public class MapLayerPriorityBuilder
```

``` highlight
extension MapLayerPriorityBuilder: NativeBase
```

``` highlight
extension MapLayerPriorityBuilder: Hashable
```

</div>

</div>

MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.

Map layers are rendered in an order according to specified priorities. Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer’s default, main category is unnamed.

The concept of ‘category’ is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category ‘bridges’ and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer diffenrently then it should opt for a layer with only the default category (e.g. raster layer).

One way to define layers’ priorities is by using a layer priority list in the scene configuration.

For example, a priority list in a scene configuration could define:

- background
- water
- roads:outline
- roads
- labels

This means layer “background” is rendered first. Next up is layer “water”. Then category “outline” of layer “roads”, followed by the main category of layer “roads”. Layer “labels” is then rendered last.

Now let’s consider a newly created layer ‘zone’ and its categories:

- zone
- zone:background
- zone:lines-outline
- zone:lines

The user wants to alter the rendering order so that it looks like:

- background
- water
- zone:background
- zone
- road:outline
- road
- zone:lines-outline
- zone:lines
- labels

This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its

    renderedBeforeLayer()

and

    renderedAfterLayer()

member functions.
</p>

Note that the order of calls matters and one can use a previously defined layer or category as a reference:

``` highlight
let zoneLayerPriority = MapLayerPriorityBuilder () . renderedAfterLayer ( named : "water" ) // places "zone" after "water" // in the rendering order . withCategory ( named : "background" ) . renderedAfterLayer ( named : "water" ) // places "zone:background" after "water" // in the rendering order and thus shifts // "zone" to be rendered later . withCategory ( named : "lines-outline" ) . renderedAfterLayer ( named : "road" ) // places "zone:lines-outline" after "road" // in the rendering order . withCategory ( named : "lines" ) . renderedAfterLayer ( named : "zone" , categoryName : "lines-outline" ) // places "zone:lines" after // "zone:lines-outline" in the rendering order . build (); zoneLayer . setPriority ( zoneLayerPriority ); // applies the priority to the zone layer // and its categories in one single operation.
```

</pre>

In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last.

Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the “labels” layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

- ‘custom-labels’ A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
- ‘custom-labels-no-self-overlap’ A label should be rendered after ‘custom-labels’, is not allowed to overlap with other labels of the same categoty and block map labels.
- ‘custom-labels-overlap-all’ A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.

</p>

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

  Creates an instance of the layer priority builder interface.

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

      withCategory(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the layer category for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`. After a priority is defined by calling one of the aforementioned functions, the current category is cleared and the builder refers again to the layer itself.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func withCategory ( _ category : String ) -> MapLayerPriorityBuilder
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
  <td><code> </code><em><code>category</code></em><code> </code></td>
  <td><div>
  <p>The name of the layer category.</p>
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

      inGroup(_: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the group for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`. When a group is set, the next defined priority is relative to the layers and layer categories inside this group. The references (i.e. ‘referenceLayer’ and ‘referenceCategory’) of the priority are only searched inside the group. Only one group or no group can be defined per layer priority and layer category priority, however, different layers can set priorities for the same group. After a priority is defined by calling one of the aforementioned functions, the current group is cleared and the builder refers again to the global layer list in the scene. Note that a group needs to exist when the built <a href="sdk-for-ios-explore-maps#/s:7heresdk16MapLayerPriorityC">`MapLayerPriority`</a> is used during a

      MapLayerBuilder.build(...)

  or
      MapLayer.setPriority(...)

  , otherwise the priority cannot be applied and the layer will render nothing to the group. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func inGroup ( _ group : String ) -> MapLayerPriorityBuilder
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
  <td><code> </code><em><code>group</code></em><code> </code></td>
  <td><div>
  <p>The name of the group. For instance the name of a <a href="sdk-for-ios-explore-classes-translucentmaplayergroup"><code>TranslucentMapLayerGroup</code></a>.</p>
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

      renderedFirst()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the priority as rendered before all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to

      MapLayerPriorityBuilder.withCategory(...)

  . Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category ‘C’ after layer ‘L’ would be overridden by the priority to render layer category ‘C’ before layer ‘L’ when building something like
  </p>

  withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)

      withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")

  The previously defined and prioritised categories can be used as reference.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func renderedFirst () -> MapLayerPriorityBuilder
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      renderedLast()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the priority as rendered after all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to

      MapLayerPriorityBuilder.withCategory(...)

  . Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category ‘C’ after layer ‘L’ would be overridden by the priority to render layer category ‘C’ before layer ‘L’ when building something like
  </p>

  withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)

      withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")

  The previously defined and prioritised categories can be used as reference.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func renderedLast () -> MapLayerPriorityBuilder
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  This class instance.

  </div>

  </div>

  </div>

- <div>

      renderedBeforeLayer(named: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the priority as rendered before the first one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to

      MapLayerPriorityBuilder.withCategory(...)

  . Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category ‘C’ after layer ‘L’ would be overridden by the priority to render layer category ‘C’ before layer ‘L’ when building something like
  </p>

  withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)

      withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")

  The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered before all layers and categories.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func renderedBeforeLayer ( named referenceLayer : String ) -> MapLayerPriorityBuilder
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
  <td><code> </code><em><code>referenceLayer</code></em><code> </code></td>
  <td><div>
  <p>The beforehand defined layer name which renders directly after the current layer.</p>
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

      renderedBeforeLayer(named: categoryName: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to

      MapLayerPriorityBuilder.withCategory(...)

  . Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category ‘C’ after layer ‘L’ would be overridden by the priority to render layer category ‘C’ before layer ‘L’ when building something like
  </p>

  withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)

      withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")

  The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered before all layers and categories.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func renderedBeforeLayer ( named referenceLayer : String , categoryName referenceCategory : String ) -> MapLayerPriorityBuilder
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
  <td><code> </code><em><code>referenceLayer</code></em><code> </code></td>
  <td><div>
  <p>The beforehand defined layer name which renders directly after the current layer.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>referenceCategory</code></em><code> </code></td>
  <td><div>
  <p>The beforehand defined category name which renders directly after the current layer.</p>
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

      renderedAfterLayer(named: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the priority as rendered after the last one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to

      MapLayerPriorityBuilder.withCategory(...)

  . Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category ‘C’ after layer ‘L’ would be overridden by the priority to render layer category ‘C’ before layer ‘L’ when building something like
  </p>

  withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)

      withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")

  The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered after all layers and categories.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func renderedAfterLayer ( named referenceLayer : String ) -> MapLayerPriorityBuilder
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
  <td><code> </code><em><code>referenceLayer</code></em><code> </code></td>
  <td><div>
  <p>The beforehand defined layer name which renders directly before the current layer.</p>
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

      renderedAfterLayer(named: categoryName: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to

      MapLayerPriorityBuilder.withCategory(...)

  . Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category ‘C’ after layer ‘L’ would be overridden by the priority to render layer category ‘C’ before layer ‘L’ when building something like
  </p>

  withCategory(“C”).renderedAfterLayer(“L”).withCategory(“C”).renderedBeforeLayer(“L”)

      withCategory(named: "C").renderedAfterLayer(named: "L").withCategory(named: "C").renderedBeforeLayer(named: "L")

  The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered after all layers and categories.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func renderedAfterLayer ( named referenceLayer : String , categoryName referenceCategory : String ) -> MapLayerPriorityBuilder
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
  <td><code> </code><em><code>referenceLayer</code></em><code> </code></td>
  <td><div>
  <p>The beforehand defined layer name which renders directly before the current layer.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>referenceCategory</code></em><code> </code></td>
  <td><div>
  <p>The beforehand defined category name which renders directly before the current layer.</p>
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

  Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new MapLayerPriority.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func build () -> MapLayerPriority
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  A new MapLayerPriority instance.

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

