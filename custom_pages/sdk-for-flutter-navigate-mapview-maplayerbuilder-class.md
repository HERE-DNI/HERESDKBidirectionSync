---
title: "MapLayerBuilder class abstract"
slug: "sdk-for-flutter-navigate-mapview-maplayerbuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerBuilder-class.html -->


<div>
<h1>MapLayerBuilder class abstract</h1></div>

<p>MapLayerBuilder is used to add layers to a map to visualise a dataset in a
programmatic way without defining it upfront in the configuration files.</p>
<p>For example, after loading a scene configuration file, the renderer is setup to draw layers in the
following order:</p>
<ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>Rendering order of elements in
a single map layer can be controlled with categories. Layer names are unique, and category names have
to be unique within a layer. The layer's default, main category is unnamed.</p>
<p>The concept of 'category' is tightly linked to styling. The idea behind category is that
one should be able to style separately elements in a map layer. Take, for instance, roads.
If one wants to style separately the bridges it will create a category 'bridges' and style
it accordingly in the style file. If the user does not intend to or cannot style elements of
the layer differently then it should opt for a layer with only the default category (e.g.
for a raster layer, only the default category makes sense, since the layer has no other
stylable elements apart from the raster image).</p>
<p>A new layer called 'zone' and its category 'background' can be added dynamically so that the
rendering order gets modified in the following way:</p>
<ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as in the
following example:</p>
<pre class="language-dart"><code> final layerPriority = MapLayerPriorityBuilder()
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
</code></pre>
<p>In case no layer priority or an empty one is provided, or if a reference layer-category pair is not
present in the rendering order, the layer is going to be rendered last with respect to the rendering
order at the time of its creation.</p>
<p>Due to current limitations, the MapLayerPriority assignment is not implemented for point map layers.
All labels will be rendered within the "labels" layer, defined in the scene configuration file.
By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed.
The following categories can be used to have a different behaviour:</p>
<ul>
<li>'custom-labels' A label should be rendered first, is allowed to overlap with other labels of
the same category and block map labels.</li>
<li>'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed
to overlap with other labels of the same categoty and block map labels.</li>
<li>'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all
predefined categories, also map labels.
These categories are configured accordingly in the basic map
scene configurations.
Category assignment to features can be done in the style based on data attributes. The category
assignment can be done for all types of content: point, line, polygon.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-maplayerbuilder">MapLayerBuilder</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-build">build</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-formap">forMap</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-tostring">toString</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withdatasource">withDataSource</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withloadpriority">withLoadPriority</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withmapmeasuredependentstoragelevels">withMapMeasureDependentStorageLevels</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withname">withName</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withpriority">withPriority</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withstyle">withStyle</a></li><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-withvisibilityrange">withVisibilityRange</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
