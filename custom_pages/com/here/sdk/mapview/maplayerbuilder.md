---
title: "MapLayerBuilder (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestmaplayerbuilder"
hidden: false
---

Package [com.here.sdk.mapview](sdk-for-android-explore-api-reference-latestpackage-summary)

# Class MapLayerBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)
[com.here.NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
com.here.sdk.mapview.MapLayerBuilder
------------------------------------------------------------------------
public final class MapLayerBuilder extends [NativeBase](sdk-for-android-explore-api-reference-latestnativebase "class in com.here")
MapLayerBuilder is used to add layers to a map to visualise a dataset in a programmatic way without defining it upfront in the configuration files.

For example, after loading a scene configuration file, the renderer is setup to draw layers in the following order:

- background
- water
- roads:outline
- roads
- labels

Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed.

The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer differently then it should opt for a layer with only the default category (e.g. for a raster layer, only the default category makes sense, since the layer has no other stylable elements apart from the raster image).

A new layer called 'zone' and its category 'background' can be added dynamically so that the rendering order gets modified in the following way:

- background
- water
- zone:background
- zone
- roads:outline
- roads
- labels

This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the following example:

     MapLayerPriority layerPriority = new MapLayerPriorityBuilder()
            .renderedAfterLayer("water") // places main category after 'water'
            .withCategory("background")
            .renderedAfterLayer("water") // places 'background' category after 'water' and before the
                                         // layer's main category.
            .build();

         MapLayer layer = new MapLayerBuilder()
            .withDataSource("DataSourceName", MapContentType.LINE)
            .forMap(map)
            .withName("zone")
            .withPriority(layerPriority)
            .build();

In case no layer priority or an empty one is provided, or if a reference layer-category pair is not present in the rendering order, the layer is going to be rendered last with respect to the rendering order at the time of its creation.

Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

- 'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
- 'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.
- 'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of content: point, line, polygon.

## Nested Class Summary

Nested Classes

Modifier and Type

  Class

  Description

  `static enum `

  [MapLayerBuilder.InstantiationErrorCode](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrorcode)

Describes a reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

`static final class `

  [MapLayerBuilder.InstantiationErrorDetails](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationerrordetails)

Describes the reason for failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

`static final class `

  [MapLayerBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationexception)

Thrown when failing to build a [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview").

## Constructor Summary

Constructors

Constructor

  Description

  [MapLayerBuilder](#%3Cinit%3E())`()`

Creates an instance of the layer builder interface.

## Method Summary

  All Methods
  Instance Methods
  Concrete Methods

  Modifier and Type

  Method

  Description

  [`MapLayer`](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview")

  [build](#build())`()`

Constructs, registers and configures a new map layer showing specified content type according to the configured parameters.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [forMap](#forMap(com.here.sdk.mapview.HereMap))`(`[`HereMap`](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview")` targetMap)`

Configures the builder to display a layer in the given map.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withDataSource](#withDataSource(java.lang.String,com.here.sdk.mapview.MapContentType))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` dataSourceName, `[`MapContentType`](sdk-for-android-explore-api-reference-latestmapcontenttype "enum class in com.here.sdk.mapview")` contentType)`

Configures the builder to use a data source with the given name as the source of data for the layer.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withLoadPriority](#withLoadPriority(double))`(double loadPriority)`

Configures the builder to set the layer load priority.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withMapMeasureDependentStorageLevels](#withMapMeasureDependentStorageLevels(com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels))`(`[`MapLayerMapMeasureDependentStorageLevels`](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview")` mapLayerMapMeasureDependentStorageLevels)`

Applies a mapping from the map measure to the storage level.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withName](#withName(java.lang.String))`(`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)` name)`

Configures builder to use the given name as a layer name.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withPriority](#withPriority(com.here.sdk.mapview.MapLayerPriority))`(`[`MapLayerPriority`](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview")` priority)`

Configures the builder to set the MapLayerPriority to be used by the layer.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withStyle](#withStyle(com.here.sdk.mapview.Style))`(`[`Style`](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview")` style)`

Configures the builder to use a style.

[`MapLayerBuilder`](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview")

  [withVisibilityRange](#withVisibilityRange(com.here.sdk.mapview.MapLayerVisibilityRange))`(`[`MapLayerVisibilityRange`](sdk-for-android-explore-api-reference-latestmaplayervisibilityrange "class in com.here.sdk.mapview")` visibilityRange)`

Configures the builder to set the layer visible in the given zoom levels range.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html)

  [clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int))

## Constructor Details

  - ()" class="section detail">

### MapLayerBuilder

public MapLayerBuilder()

    Creates an instance of the layer builder interface.

## Method Details

### withName

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withName(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) name)

    Configures builder to use the given name as a layer name. The name is a mandatory layer creation parameter.
Parameters:
    `name` -

    Name of the layer. Must be unique.

    Returns:
    This class instance.

### withDataSource

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withDataSource(@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) dataSourceName, @NonNull [MapContentType](sdk-for-android-explore-api-reference-latestmapcontenttype "enum class in com.here.sdk.mapview") contentType)

    Configures the builder to use a data source with the given name as the source of data for the layer. The datasource name and content type are mandatory layer creation parameters.
Parameters:
    `dataSourceName` -

    Name of the data source.

    `contentType` -

    The renderable content type supplied by the data source.

    Returns:
    This class instance.

### withStyle

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withStyle(@NonNull [Style](sdk-for-android-explore-api-reference-lateststyle "class in com.here.sdk.mapview") style)

    Configures the builder to use a style. Providing a style during layer creation is not mandatory. The style can also be set/updated after the layer creation. For more details see Custom Layer Style Reference in the documentation. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.
Parameters:
    `style` -

    Style for the layer.

    Returns:
    This class instance.

### forMap

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") forMap(@NonNull [HereMap](sdk-for-android-explore-api-reference-latestheremap "class in com.here.sdk.mapview") targetMap)

    Configures the builder to display a layer in the given map. The map is a mandatory layer creation parameter.
Parameters:
    `targetMap` -

    The map.

    Returns:
    This class instance.

### withPriority

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withPriority(@NonNull [MapLayerPriority](sdk-for-android-explore-api-reference-latestmaplayerpriority "class in com.here.sdk.mapview") priority)

    Configures the builder to set the MapLayerPriority to be used by the layer.
Parameters:
    `priority` -

    MapLayerPriority which should be applied to the layer.

    Returns:
    This class instance.

### withVisibilityRange

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withVisibilityRange(@NonNull [MapLayerVisibilityRange](sdk-for-android-explore-api-reference-latestmaplayervisibilityrange "class in com.here.sdk.mapview") visibilityRange)

    Configures the builder to set the layer visible in the given zoom levels range. Values outside the map zoom level range (0, 24) will be ignored. Providing the visibility range is optional. If not provided, the layer will be visible on all zoom levels.
Parameters:
    `visibilityRange` -

    Visibility range which should be applied to the layer.

    Returns:
    This class instance.

### withMapMeasureDependentStorageLevels

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withMapMeasureDependentStorageLevels(@NonNull [MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-api-reference-latestmaplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview") mapLayerMapMeasureDependentStorageLevels)

    Applies a mapping from the map measure to the storage level. This mapping is used by the layer to request data for the specified storage level corresponding to the map measure from the datasource. This can be used for example to fine-tune the resolution of raster layers. Note: When the map camera is significantly tilted, the storage level is further reduced for data towards the horizon. Note: Mappings that request higher storage levels will lead to an increased number of requests to the raster tile service. Providing the map measure to storage level mapping is optional. If not provided, the default mapping will use a storage level that is for raster layers one and for others three levels lower than the zoom level, corresponding to an offset of -1 and -3.
Parameters:
    `mapLayerMapMeasureDependentStorageLevels` -

    The map measure to storage level mapping that should be applied for the layer.

    Returns:
    This class instance.

### withLoadPriority

@NonNull public [MapLayerBuilder](sdk-for-android-explore-api-reference-latestmaplayerbuilder "class in com.here.sdk.mapview") withLoadPriority(double loadPriority)

    Configures the builder to set the layer load priority. Higher load priority values lead to layer being scheduled for loading before layers with lesser values.
Parameters:
    `loadPriority` -

    Load priority for layer.

    Returns:
    This class instance.

### build

@NonNull public [MapLayer](sdk-for-android-explore-api-reference-latestmaplayer "class in com.here.sdk.mapview") build() throws [MapLayerBuilder.InstantiationException](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationexception "class in com.here.sdk.mapview")

    Constructs, registers and configures a new map layer showing specified content type according to the configured parameters. After this call this instance is reset to the initial state. It could be used to build another map layer, but will not keep any previously configured properties.
Returns:
    A new MapLayer instance.

    Throws:
    [`MapLayerBuilder.InstantiationException`](sdk-for-android-explore-api-reference-latestmaplayerbuilder-instantiationexception "class in com.here.sdk.mapview") -

    Indicates an instantiation issue.
