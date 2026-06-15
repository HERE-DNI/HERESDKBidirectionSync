---
title: "MapLayerPriorityBuilder class abstract"
slug: "sdk-for-flutter-explore-mapview-maplayerprioritybuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerPriorityBuilder-class.html -->


<div>
<h1>MapLayerPriorityBuilder class abstract</h1></div>

<p>MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer
and its categories, relative to other layers or layer-category pairs.</p>
<p>Map layers are rendered in an order according to specified priorities. Rendering order of elements in
a single map layer can be controlled with categories. Layer names are unique, and category names have
to be unique within a layer. The layer's default, main category is unnamed.</p>
<p>The concept of 'category' is tightly linked to styling. The idea behind category is that
one should be able to style separately elements in a map layer. Take, for instance, roads.
If one wants to style separately the bridges it will create a category 'bridges' and style
it accordingly in the style file. If the user does not intend to or cannot style elements
of the layer diffenrently then it should opt for a layer with only the default category (e.g.
raster layer).</p>
<p>One way to define layers' priorities is by using a layer priority list in the scene configuration.</p>
<p>For example, a priority list in a scene configuration could define:</p>
<ul>
<li>background</li>
<li>water</li>
<li>roads:outline</li>
<li>roads</li>
<li>labels</li>
</ul>
<p>This means layer "background" is rendered first. Next up is layer "water". Then category "outline" of
layer "roads", followed by the main category of layer "roads". Layer "labels" is then rendered last.</p>
<p>
Now let's consider a newly created layer 'zone' and its categories:
</p><ul>
<li>zone</li>
<li>zone:background</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
</ul>
<p>The user wants to alter the rendering order so that it looks like:</p>
<ul>
<li>background</li>
<li>water</li>
<li>zone:background</li>
<li>zone</li>
<li>road:outline</li>
<li>road</li>
<li>zone:lines-outline</li>
<li>zone:lines</li>
<li>labels</li>
</ul>
<p>This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its
<code>renderedBeforeLayer()</code> and <code>renderedAfterLayer()</code> member functions.</p>
<p>Note that the order of calls matters and one can use a previously defined layer or category
as a reference:</p>
<pre class="language-dart"><code>  final zoneLayerPriority = MapLayerPriorityBuilder()
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
</code></pre>
<p>In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer
is going to be rendered last.</p>
<p>Due to a current limitation for point map layers, the mentioned APIs to control the rendering
order are not implemented. All labels will be rendered within the "labels" layer, defined in
the scene configuration file.
By default, all labels rendered by a point map layer are rendered last and no overlapping is
allowed. The following categories can be used to have a different behaviour:</p>
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
assignment can be done for all types of data: points, lines, polygons.</li>
</ul>


<h2>Constructors</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-maplayerprioritybuilder">MapLayerPriorityBuilder</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-hashcode">hashCode</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-build">build</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup">inGroup</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-nosuchmethod">noSuchMethod</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedafterlayer">renderedAfterLayer</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedafterlayerwithcategory">renderedAfterLayerWithCategory</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedbeforelayer">renderedBeforeLayer</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedbeforelayerwithcategory">renderedBeforeLayerWithCategory</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedfirst">renderedFirst</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-renderedlast">renderedLast</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-tostring">toString</a></li><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-withcategory">withCategory</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="sdk-for-flutter-explore-mapview-maplayerprioritybuilder-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
