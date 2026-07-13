---
title: "MapLayerBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-maplayerbuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerBuilder-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayerBuilder-class-sidebar.html">

<div>

# <span class="kind-class">MapLayerBuilder</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

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

``` dart
final layerPriority = MapLayerPriorityBuilder()
     .renderedAfterLayer("water") // places main category after 'water'
     .withCategory("background")
     .renderedAfterLayer("water") // places 'background' category after 'water' and before the
                                  // layer's main category.
     .build();

 var layer = MapLayerBuilder()
     .withDataSource("DataSourceName", MapContentType.line)
     .forMap(map)
     .withName("zone")
     .withPriority(layerPriority)
     .build();
```

</pre>

In case no layer priority or an empty one is provided, or if a reference layer-category pair is not present in the rendering order, the layer is going to be rendered last with respect to the rendering order at the time of its creation.

Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

- 'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
- 'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.
- 'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of content: point, line, polygon.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-maplayerbuilder">MapLayerBuilder</a></span><span class="signature">()</span>  
Creates an instance of the layer builder interface.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-build">build</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayer-class">MapLayer</a></span> </span>  
Constructs, registers and configures a new map layer showing specified content type according to the configured parameters.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-formap">forMap</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-forMap-param-targetMap" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">targetMap</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures the builder to display a layer in the given map.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withdatasource">withDataSource</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withDataSource-param-dataSourceName" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">dataSourceName</span>, </span><span id="sdk-for-flutter-explore-withDataSource-param-contentType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapcontenttype">MapContentType</a></span> <span class="parameter-name">contentType</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures the builder to use a data source with the given name as the source of data for the layer.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withloadpriority">withLoadPriority</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withLoadPriority-param-loadPriority" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">loadPriority</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures the builder to set the layer load priority.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withmapmeasuredependentstoragelevels">withMapMeasureDependentStorageLevels</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withMapMeasureDependentStorageLevels-param-mapLayerMapMeasureDependentStorageLevels" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayermapmeasuredependentstoragelevels-class">MapLayerMapMeasureDependentStorageLevels</a></span> <span class="parameter-name">mapLayerMapMeasureDependentStorageLevels</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Applies a mapping from the map measure to the storage level.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withname">withName</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withName-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures builder to use the given name as a layer name.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withpriority">withPriority</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withPriority-param-priority" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a></span> <span class="parameter-name">priority</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures the builder to set the MapLayerPriority to be used by the layer.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withstyle">withStyle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withStyle-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-style-class">Style</a></span> <span class="parameter-name">style</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures the builder to use a style.

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-withvisibilityrange">withVisibilityRange</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-withVisibilityRange-param-visibilityRange" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayervisibilityrange-class">MapLayerVisibilityRange</a></span> <span class="parameter-name">visibilityRange</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-explore-mapview-maplayerbuilder-class">MapLayerBuilder</a></span> </span>  
Configures the builder to set the layer visible in the given zoom levels range.

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-maplayerbuilder-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
