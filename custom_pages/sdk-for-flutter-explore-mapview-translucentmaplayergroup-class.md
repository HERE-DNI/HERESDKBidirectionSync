---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-translucentmaplayergroup-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- TranslucentMapLayerGroup-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/TranslucentMapLayerGroup-class.html#constructors">Constructors</a></li>
<li><a href="mapview/TranslucentMapLayerGroup/TranslucentMapLayerGroup.create.html">create</a></li>
<li><a href="mapview/TranslucentMapLayerGroup/TranslucentMapLayerGroup.withPriority.html">withPriority</a></li>
<li class="section-title inherited">
<a href="mapview/TranslucentMapLayerGroup-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview/TranslucentMapLayerGroup/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview/TranslucentMapLayerGroup/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview/TranslucentMapLayerGroup-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/TranslucentMapLayerGroup/destroy.html">destroy</a></li>
<li class="inherited"><a href="mapview/TranslucentMapLayerGroup/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/TranslucentMapLayerGroup/setPriority.html">setPriority</a></li>
<li class="inherited"><a href="mapview/TranslucentMapLayerGroup/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/TranslucentMapLayerGroup-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/TranslucentMapLayerGroup/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">TranslucentMapLayerGroup class</li>
</ol>
<div class="self-name">TranslucentMapLayerGroup</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/TranslucentMapLayerGroup-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TranslucentMapLayerGroup class abstract</h1></div>
<section class="desc markdown">
<p>A translucent layer group that can be the target for <a href="../mapview/MapLayerPriorityBuilder/inGroup.html">/sdk-for-flutter-explore-mapview-maplayerprioritybuilder-ingroup</a>.</p>
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
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TranslucentMapLayerGroup.create">
<a href="../mapview/TranslucentMapLayerGroup/TranslucentMapLayerGroup.create.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-translucentmaplayergroup-create</a>(String name, <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a> aMap)
</dt>
<dd>
          Creates an instance of the group.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="TranslucentMapLayerGroup.withPriority">
<a href="../mapview/TranslucentMapLayerGroup/TranslucentMapLayerGroup.withPriority.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-translucentmaplayergroup-withpriority</a>(String name, <a href="../mapview/HereMapControllerCore-class.html">/sdk-for-flutter-explore-mapview-heremapcontrollercore-class</a> aMap, <a href="../mapview/MapLayerPriority-class.html">/sdk-for-flutter-explore-mapview-maplayerpriority-class</a> priority)
</dt>
<dd>
          Creates an instance of the group.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
<a href="../mapview/TranslucentMapLayerGroup/hashCode.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/TranslucentMapLayerGroup/runtimeType.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-runtimetype</a>
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
<dt class="callable" id="destroy">
<a href="../mapview/TranslucentMapLayerGroup/destroy.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-destroy</a>(<wbr/>)
    → void

</dt>
<dd>
  Frees all internally used resources.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/TranslucentMapLayerGroup/noSuchMethod.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setPriority">
<a href="../mapview/TranslucentMapLayerGroup/setPriority.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-setpriority</a>(<wbr/><a href="../mapview/MapLayerPriority-class.html">/sdk-for-flutter-explore-mapview-maplayerpriority-class</a> priority)
    → void

</dt>
<dd>
  Sets the render priority for the layer group which replaces any previously defined priority.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/TranslucentMapLayerGroup/toString.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
<a href="../mapview/TranslucentMapLayerGroup/operator_equals.html">/sdk-for-flutter-explore-mapview-translucentmaplayergroup-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">TranslucentMapLayerGroup class</li>
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
</HTMLBlock>
