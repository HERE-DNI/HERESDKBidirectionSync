---
title: "MapLayerPriorityBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerPriorityBuilder-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html">

<div>

# <span class="kind-class">MapLayerPriorityBuilder</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

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

This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its

    renderedBeforeLayer()

and

    renderedAfterLayer()

member functions.
</p>

Note that the order of calls matters and one can use a previously defined layer or category as a reference:

``` dart
final zoneLayerPriority = MapLayerPriorityBuilder()
       .renderedAfterLayer("water")          // places "zone" after "water"
                                             // in the rendering order
       .withCategory("background")
       .renderedAfterLayer("water")          // places "zone:background" after "water"
                                             // in the rendering order and thus shifts
                                             // "zone" to be rendered later
       .withCategory("lines-outline")
       .renderedAfterLayer("road")           // places "zone:lines-outline" after "road"
                                             // in the rendering order
       .withCategory("lines")
       .renderedAfterLayer("zone", "lines-outline") // places "zone:lines" after
                                                    // "zone:lines-outline" in the rendering order
       .build();

  zoneLayer.setPriority(zoneLayerPriority);  // applies the priority to the zone layer
                                             // and its categories in one single operation.
```

</pre>

In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last.

Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:

- 'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.
- 'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.
- 'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-maplayerprioritybuilder">MapLayerPriorityBuilder</a></span><span class="signature">()</span>  
Creates an instance of the layer priority builder interface.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-build">build</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a></span> </span>  
Constructs a MapLayerPriority.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup">inGroup</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-inGroup-param-group" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">group</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the group for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedafterlayer">renderedAfterLayer</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-renderedAfterLayer-param-referenceLayer" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceLayer</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the priority as rendered after the last one from the referenceLayer and its categories.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedafterlayerwithcategory">renderedAfterLayerWithCategory</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-renderedAfterLayerWithCategory-param-referenceLayer" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceLayer</span>, </span><span id="sdk-for-flutter-navigate-renderedAfterLayerWithCategory-param-referenceCategory" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceCategory</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the priority as rendered after the referenceCategory of the referenceLayer.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedbeforelayer">renderedBeforeLayer</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-renderedBeforeLayer-param-referenceLayer" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceLayer</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the priority as rendered before the first one from the referenceLayer and its categories.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedbeforelayerwithcategory">renderedBeforeLayerWithCategory</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-renderedBeforeLayerWithCategory-param-referenceLayer" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceLayer</span>, </span><span id="sdk-for-flutter-navigate-renderedBeforeLayerWithCategory-param-referenceCategory" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">referenceCategory</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the priority as rendered before the referenceCategory of the referenceLayer.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedfirst">renderedFirst</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the priority as rendered before all layers and categories.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedlast">renderedLast</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the priority as rendered after all layers and categories.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory">withCategory</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-withCategory-param-category" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">category</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class">MapLayerPriorityBuilder</a></span> </span>  
Sets the layer category for which a priority could be defined with the next call to the functions `renderedFirst|Last|BeforeLayer|AfterLayer`.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
