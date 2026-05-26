---
title: "MapLayerBuilder class abstract"
slug: "sdk-for-flutter-explore-mapview-maplayerbuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapLayerBuilder-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapLayerBuilder-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapLayerBuilder/MapLayerBuilder.html">MapLayerBuilder</a></li>
<li class="section-title inherited">
<a href="mapview/MapLayerBuilder-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/MapLayerBuilder/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/MapLayerBuilder/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/MapLayerBuilder-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapLayerBuilder/build.html">build</a></li>
<li><a href="mapview/MapLayerBuilder/forMap.html">forMap</a></li>
<li class="inherited"><a href="mapview/MapLayerBuilder/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapLayerBuilder/toString.html">toString</a></li>
<li><a href="mapview/MapLayerBuilder/withDataSource.html">withDataSource</a></li>
<li><a href="mapview/MapLayerBuilder/withLoadPriority.html">withLoadPriority</a></li>
<li><a href="mapview/MapLayerBuilder/withMapMeasureDependentStorageLevels.html">withMapMeasureDependentStorageLevels</a></li>
<li><a href="mapview/MapLayerBuilder/withName.html">withName</a></li>
<li><a href="mapview/MapLayerBuilder/withPriority.html">withPriority</a></li>
<li><a href="mapview/MapLayerBuilder/withStyle.html">withStyle</a></li>
<li><a href="mapview/MapLayerBuilder/withVisibilityRange.html">withVisibilityRange</a></li>
<li class="section-title inherited"><a href="mapview/MapLayerBuilder-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapLayerBuilder/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapLayerBuilder class</li>
</ol>
<div class="self-name">MapLayerBuilder</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayerBuilder-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapLayerBuilder class abstract</h1></div>
<section class="desc markdown">
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
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapLayerBuilder">
/sdk-for-flutter-explore-mapview-maplayerbuilder-maplayerbuilder()
</dt>
<dd>
          Creates an instance of the layer builder interface.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-maplayerbuilder-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-maplayerbuilder-runtimetype
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
/sdk-for-flutter-explore-mapview-maplayerbuilder-build(<wbr/>)
    → /sdk-for-flutter-explore-mapview-maplayer-class

</dt>
<dd>
  Constructs, registers and configures a new map layer showing specified content type
according to the configured parameters.
  

</dd>
<dt class="callable" id="forMap">
/sdk-for-flutter-explore-mapview-maplayerbuilder-formap(<wbr/>/sdk-for-flutter-explore-mapview-heremapcontrollercore-class targetMap)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures the builder to display a layer in the given map.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-maplayerbuilder-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-maplayerbuilder-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="withDataSource">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withdatasource(<wbr/>String dataSourceName, /sdk-for-flutter-explore-mapview-mapcontenttype contentType)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures the builder to use a data source with the given name as the source
of data for the layer.
  

</dd>
<dt class="callable" id="withLoadPriority">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withloadpriority(<wbr/>double loadPriority)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures the builder to set the layer load priority.
  

</dd>
<dt class="callable" id="withMapMeasureDependentStorageLevels">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withmapmeasuredependentstoragelevels(<wbr/>/sdk-for-flutter-explore-mapview-maplayermapmeasuredependentstoragelevels-class mapLayerMapMeasureDependentStorageLevels)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Applies a mapping from the map measure to the storage level.
  

</dd>
<dt class="callable" id="withName">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withname(<wbr/>String name)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures builder to use the given name as a layer name.
  

</dd>
<dt class="callable" id="withPriority">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withpriority(<wbr/>/sdk-for-flutter-explore-mapview-maplayerpriority-class priority)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures the builder to set the MapLayerPriority to be used by the layer.
  

</dd>
<dt class="callable" id="withStyle">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withstyle(<wbr/>/sdk-for-flutter-explore-mapview-style-class style)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures the builder to use a style.
  

</dd>
<dt class="callable" id="withVisibilityRange">
/sdk-for-flutter-explore-mapview-maplayerbuilder-withvisibilityrange(<wbr/>/sdk-for-flutter-explore-mapview-maplayervisibilityrange-class visibilityRange)
    → /sdk-for-flutter-explore-mapview-maplayerbuilder-class

</dt>
<dd>
  Configures the builder to set the layer visible in the given zoom levels range.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-explore-mapview-maplayerbuilder-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapLayerBuilder class</li>
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
