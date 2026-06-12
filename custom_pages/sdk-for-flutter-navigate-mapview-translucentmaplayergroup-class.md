---
title: "TranslucentMapLayerGroup class abstract"
slug: "sdk-for-flutter-navigate-mapview-translucentmaplayergroup-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TranslucentMapLayerGroup-class.html -->


<div>
<h1>TranslucentMapLayerGroup class abstract</h1></div>

<p>A translucent layer group that can be the target for <a href="/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup">MapLayerPriorityBuilder.inGroup</a>.</p>
<p>Currently, only custom line layers can be added to a translucent layer group.
Custom line layers in a translucent layer group are rendered in an offscreen translucent pass so
that overlapping translucent line geometry is not alpha blended with itself.
At creation, the layer group gets added to a map. The layer group gets removed from the map upon
instance destruction and any layer (categories) still in the group are not rendered anymore,
therefore it is recommended to keep a group alive as long as layers using the group are alive and
in use.</p>
<p>Conceptual example to place line layers into a translucent group:</p>
<pre class="language-dart"><code> // Create a translucent group with a unique name and a render priority
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
</code></pre>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-translucentmaplayergroup-create">TranslucentMapLayerGroup.create</a></li><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-translucentmaplayergroup-withpriority">TranslucentMapLayerGroup.withPriority</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-destroy">destroy</a></li><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-setpriority">setPriority</a></li><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-navigate-mapview-translucentmaplayergroup-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
