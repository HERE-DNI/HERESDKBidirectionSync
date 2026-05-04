---
title: "MapLayerPriorityBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapLayerPriorityBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapLayerPriorityBuilder
------------------------------------------------------------------------
public final class MapLayerPriorityBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.

Map layers are rendered in an order according to specified priorities. Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed.

The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer diffenrently then it should opt for a layer with only the default category (e.g. raster layer).

One way to define layers' priorities is by using a layer priority list in the scene configuration.

For example, a priority list in a scene configuration could define:

- background
- water
- roads:outline
- roads
- labels

This means layer "background" is rendered first. Next up is layer "water". Then category "outline" of layer "roads", followed by the main category of layer "roads". Layer "labels" is then rendered last.

Now let's consider a newly created layer 'zone' and its categories:

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

This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its `renderedBeforeLayer()` and `renderedAfterLayer()` member functions.

Note that the order of calls matters and one can use a previously defined layer or category as a reference:

    MapLayerPriority zoneLayerPriority = new MapLayerPriorityBuilder()
           .renderedAfterLayer("water")            // places "zone" after "water"
                                                   // in the rendering order
           .withCategory("background")
           .renderedAfterLayer("water")            // places "zone:background" after "water"
                                                   // in the rendering order and thus shifts
                                                   // "zone" to be rendered later
           .withCategory("lines-outline")
           .renderedAfterLayer("road")             // places "zone:lines-outline" after "road"
                                                   // in the rendering order
           .withCategory("lines")
           .renderedAfterLayer("zone", "lines-outline") // places "zone:lines" after
                                                   // "zone:lines-outline" in the rendering order
          .build();

      zoneLayer.setPriority(zoneLayerPriority);    // applies the priority to the zone layer
                                                   // and its categories in one single operation.

In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last.

Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

- 'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
- 'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.
- 'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.

## Constructor Summary

Constructors

Constructor

  Description

  [MapLayerPriorityBuilder](#%3Cinit%3E())`()`

Creates an instance of the layer priority builder interface.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")

  [build](#build())`()`

Constructs a MapLayerPriority.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [inGroup](#inGroup(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` group)`

Sets the group for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [renderedAfterLayer](#renderedAfterLayer(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` referenceLayer)`

Sets the priority as rendered after the last one from the referenceLayer and its categories.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [renderedAfterLayer](#renderedAfterLayer(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` referenceLayer, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` referenceCategory)`

Sets the priority as rendered after the referenceCategory of the referenceLayer.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [renderedBeforeLayer](#renderedBeforeLayer(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` referenceLayer)`

Sets the priority as rendered before the first one from the referenceLayer and its categories.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [renderedBeforeLayer](#renderedBeforeLayer(java.lang.String,java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` referenceLayer, `[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` referenceCategory)`

Sets the priority as rendered before the referenceCategory of the referenceLayer.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [renderedFirst](#renderedFirst())`()`

Sets the priority as rendered before all layers and categories.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [renderedLast](#renderedLast())`()`

Sets the priority as rendered after all layers and categories.

[`MapLayerPriorityBuilder`](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview")

  [withCategory](#withCategory(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` category)`

Sets the layer category for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### MapLayerPriorityBuilder

public MapLayerPriorityBuilder()

    Creates an instance of the layer priority builder interface.

## Method Details

### withCategory

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") withCategory(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) category)

    Sets the layer category for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`. After a priority is defined by calling one of the aforementioned functions, the current category is cleared and the builder refers again to the layer itself.
Parameters:
    `category` -

    The name of the layer category.

    Returns:
    This class instance.

### inGroup

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") inGroup(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) group)

    Sets the group for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`. When a group is set, the next defined priority is relative to the layers and layer categories inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority are only searched inside the group. Only one group or no group can be defined per layer priority and layer category priority, however, different layers can set priorities for the same group. After a priority is defined by calling one of the aforementioned functions, the current group is cleared and the builder refers again to the global layer list in the scene. Note that a group needs to exist when the built [`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") is used during a [`MapLayerBuilder.build()`](sdk-for-android-explore-api-reference-latestmaplayerbuilder#build()) or [`MapLayer.setPriority(com.here.sdk.mapview.MapLayerPriority)`](sdk-for-android-explore-api-reference-latestmaplayer#setPriority(com.here.sdk.mapview.MapLayerPriority)), otherwise the priority cannot be applied and the layer will render nothing to the group. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `group` -

    The name of the group. For instance the name of a [`TranslucentMapLayerGroup`](sdk-for-android-explore-api-reference-latesttranslucentmaplayergroup "class in com.here.sdk.mapview").

    Returns:
    This class instance.

### renderedFirst

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") renderedFirst()

    Sets the priority as rendered before all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to [`withCategory(java.lang.String)`](#withCategory(java.lang.String)). Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    `withCategory(&quot;C&quot;).renderedAfterLayer(&quot;L&quot;).withCategory(&quot;C&quot;).renderedBeforeLayer(&quot;L&quot;)`

    The previously defined and prioritised categories can be used as reference.
Returns:
    This class instance.

### renderedLast

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") renderedLast()

    Sets the priority as rendered after all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to [`withCategory(java.lang.String)`](#withCategory(java.lang.String)). Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    `withCategory(&quot;C&quot;).renderedAfterLayer(&quot;L&quot;).withCategory(&quot;C&quot;).renderedBeforeLayer(&quot;L&quot;)`

    The previously defined and prioritised categories can be used as reference.
Returns:
    This class instance.

### renderedBeforeLayer

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") renderedBeforeLayer(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) referenceLayer)

    Sets the priority as rendered before the first one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to [`withCategory(java.lang.String)`](#withCategory(java.lang.String)). Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    `withCategory(&quot;C&quot;).renderedAfterLayer(&quot;L&quot;).withCategory(&quot;C&quot;).renderedBeforeLayer(&quot;L&quot;)`

    The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered before all layers and categories.
Parameters:
    `referenceLayer` -

    The beforehand defined layer name which renders directly after the current layer.

    Returns:
    This class instance.

### renderedBeforeLayer

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") renderedBeforeLayer(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) referenceLayer, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) referenceCategory)

    Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to [`withCategory(java.lang.String)`](#withCategory(java.lang.String)). Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    `withCategory(&quot;C&quot;).renderedAfterLayer(&quot;L&quot;).withCategory(&quot;C&quot;).renderedBeforeLayer(&quot;L&quot;)`

    The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered before all layers and categories.
Parameters:
    `referenceLayer` -

    The beforehand defined layer name which renders directly after the current layer.

    `referenceCategory` -

    The beforehand defined category name which renders directly after the current layer.

    Returns:
    This class instance.

### renderedAfterLayer

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") renderedAfterLayer(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) referenceLayer)

    Sets the priority as rendered after the last one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to [`withCategory(java.lang.String)`](#withCategory(java.lang.String)). Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    `withCategory(&quot;C&quot;).renderedAfterLayer(&quot;L&quot;).withCategory(&quot;C&quot;).renderedBeforeLayer(&quot;L&quot;)`

    The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered after all layers and categories.
Parameters:
    `referenceLayer` -

    The beforehand defined layer name which renders directly before the current layer.

    Returns:
    This class instance.

### renderedAfterLayer

@NonNull public [MapLayerPriorityBuilder](sdk-for-android-explore-api-reference-latestmaplayerprioritybuilder "class in com.here.sdk.mapview") renderedAfterLayer(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) referenceLayer, @NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) referenceCategory)

    Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to [`withCategory(java.lang.String)`](#withCategory(java.lang.String)). Notice that the order of calls to the functions `renderedFirst|Last|Before|After` matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like

    `withCategory(&quot;C&quot;).renderedAfterLayer(&quot;L&quot;).withCategory(&quot;C&quot;).renderedBeforeLayer(&quot;L&quot;)`

    The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered after all layers and categories.
Parameters:
    `referenceLayer` -

    The beforehand defined layer name which renders directly before the current layer.

    `referenceCategory` -

    The beforehand defined category name which renders directly before the current layer.

    Returns:
    This class instance.

### build

@NonNull public [MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") build()

    Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new MapLayerPriority.
Returns:
    A new MapLayerPriority instance.
