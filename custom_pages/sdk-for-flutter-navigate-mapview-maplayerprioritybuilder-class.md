---
title: "MapLayerPriorityBuilder class abstract"
slug: "sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerPriorityBuilder-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapLayerPriorityBuilder-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/MapLayerPriorityBuilder.html">MapLayerPriorityBuilder</a></li>
<li class="section-title inherited">
<a href="mapview/MapLayerPriorityBuilder-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapLayerPriorityBuilder/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapLayerPriorityBuilder/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapLayerPriorityBuilder-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/build.html">build</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/inGroup.html">inGroup</a></li>
<li class="inherited"><a href="mapview/MapLayerPriorityBuilder/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/renderedAfterLayer.html">renderedAfterLayer</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/renderedAfterLayerWithCategory.html">renderedAfterLayerWithCategory</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/renderedBeforeLayer.html">renderedBeforeLayer</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/renderedBeforeLayerWithCategory.html">renderedBeforeLayerWithCategory</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/renderedFirst.html">renderedFirst</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/renderedLast.html">renderedLast</a></li>
<li class="inherited"><a href="mapview/MapLayerPriorityBuilder/toString.html">toString</a></li>
<li><a href="mapview/MapLayerPriorityBuilder/withCategory.html">withCategory</a></li>
<li class="section-title inherited"><a href="mapview/MapLayerPriorityBuilder-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapLayerPriorityBuilder/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapLayerPriorityBuilder class</li>
</ol>
<div class="self-name">MapLayerPriorityBuilder</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayerPriorityBuilder-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapLayerPriorityBuilder class abstract</h1></div>
<section class="desc markdown">
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
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapLayerPriorityBuilder">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-maplayerprioritybuilder()
</dt>
<dd>
          Creates an instance of the layer priority builder interface.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="build">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-build(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-maplayerpriority-class

</dt>
<dd>
  Constructs a MapLayerPriority.
  

</dd>
<dt class="callable" id="inGroup">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-ingroup(<wbr/>String group)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the group for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="renderedAfterLayer">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedafterlayer(<wbr/>String referenceLayer)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the priority as rendered after the last one from the referenceLayer and its categories.
  

</dd>
<dt class="callable" id="renderedAfterLayerWithCategory">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedafterlayerwithcategory(<wbr/>String referenceLayer, String referenceCategory)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the priority as rendered after the referenceCategory of the referenceLayer.
  

</dd>
<dt class="callable" id="renderedBeforeLayer">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedbeforelayer(<wbr/>String referenceLayer)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the priority as rendered before the first one from the referenceLayer and its categories.
  

</dd>
<dt class="callable" id="renderedBeforeLayerWithCategory">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedbeforelayerwithcategory(<wbr/>String referenceLayer, String referenceCategory)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the priority as rendered before the referenceCategory of the referenceLayer.
  

</dd>
<dt class="callable" id="renderedFirst">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedfirst(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the priority as rendered before all layers and categories.
  

</dd>
<dt class="callable" id="renderedLast">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-renderedlast(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the priority as rendered after all layers and categories.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="withCategory">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-withcategory(<wbr/>String category)
    → /sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-class

</dt>
<dd>
  Sets the layer category for which a priority could be defined with the next call to the functions
<code>renderedFirst|Last|BeforeLayer|AfterLayer</code>.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-maplayerprioritybuilder-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li class="self-crumb">MapLayerPriorityBuilder class</li>
</ol>
<h5>mapview library</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
