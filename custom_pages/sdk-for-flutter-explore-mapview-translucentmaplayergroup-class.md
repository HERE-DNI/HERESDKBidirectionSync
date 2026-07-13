---
title: "TranslucentMapLayerGroup class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-translucentmaplayergroup-class"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/TranslucentMapLayerGroup-class-sidebar.html">

<div>

# <span class="kind-class">TranslucentMapLayerGroup</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A translucent layer group that can be the target for <a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a>.

Currently, only custom line layers can be added to a translucent layer group. Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so that overlapping translucent line geometry is not alpha blended with itself. At creation, the layer group gets added to a map. The layer group gets removed from the map upon instance destruction and any layer (categories) still in the group are not rendered anymore, therefore it is recommended to keep a group alive as long as layers using the group are alive and in use.

Conceptual example to place line layers into a translucent group:

``` dart
// Create a translucent group with a unique name and a render priority
 final groupPriority = MapLayerPriorityBuilder().renderedLast().build();
 final group = TranslucentMapLayerGroup(name: "TranslucentGroupName", map, groupPriority);

 // Create a line layer to be rendered as part of the translucent group
 final lineLayerPriority = MapLayerPriorityBuilder()
     .inGroup("TranslucentGroupName") // places the line layer into the group
     .renderedFirst()                 // to be rendered first when the group is rendered
     .withCategory("SomeCategory")    // places the line layer category 'SomeCategory'
     .inGroup("TranslucentGroupName") // into the group
     .renderedLast()                  // to be rendered last when the group is rendered
     .build();

 final lineLayer = MapLayerBuilder()
     .withDataSource("DataSourceName", MapContentType.line)
     .forMap(map)
     .withName("LineLayerName")
     .withPriority(lineLayerPriority)
     .withStyle(translucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
     .build();

 // Create a second line layer to be rendered as part of the translucent group
 final secondLineLayerPriority = MapLayerPriorityBuilder()
     .inGroup("TranslucentGroupName")      // places the second line layer into the group
     .renderedBeforeLayer("LineLayerName") // to be rendered before first layer
                                           // when the group is rendered
     .build();

 final secondLineLayer = MapLayerBuilder()
     .withDataSource("SecondDataSourceName", MapContentType.line)
     .forMap(map)
     .withName("SecondLineLayerName")
     .withPriority(secondLineLayerPriority)
     .withStyle(secondTranslucentLineStyle) // E.g. "technique": "line" ... "color": "#FFFFFF80"
     .build();
```

</pre>

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-translucentmaplayergroup-create">TranslucentMapLayerGroup.create</a></span><span class="signature">(<span id="sdk-for-flutter-explore-create-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-explore-create-param-aMap" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">aMap</span></span>)</span>  
Creates an instance of the group.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-translucentmaplayergroup-withpriority">TranslucentMapLayerGroup.withPriority</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withPriority-param-name" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">name</span>, </span><span id="sdk-for-flutter-explore-withPriority-param-aMap" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-heremapcontrollercore-class">HereMapControllerCore</a></span> <span class="parameter-name">aMap</span>, </span><span id="sdk-for-flutter-explore-withPriority-param-priority" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a></span> <span class="parameter-name">priority</span></span>)</span>  
Creates an instance of the group.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-destroy">destroy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Frees all internally used resources.

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-setpriority">setPriority</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setPriority-param-priority" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-maplayerpriority-class">MapLayerPriority</a></span> <span class="parameter-name">priority</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the render priority for the layer group which replaces any previously defined priority.

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-translucentmaplayergroup-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

