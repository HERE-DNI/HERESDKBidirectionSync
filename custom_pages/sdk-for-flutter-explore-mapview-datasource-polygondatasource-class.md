---
title: "PolygonDataSource class abstract"
slug: "sdk-for-flutter-explore-mapview-datasource-polygondatasource-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonDataSource-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/PolygonDataSource-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/PolygonDataSource/PolygonDataSource.html">PolygonDataSource</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/PolygonDataSource-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/PolygonDataSource/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataSource/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/PolygonDataSource-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/PolygonDataSource/add.html">add</a></li>
<li><a href="mapview.datasource/PolygonDataSource/addPolygons.html">addPolygons</a></li>
<li><a href="mapview.datasource/PolygonDataSource/destroy.html">destroy</a></li>
<li><a href="mapview.datasource/PolygonDataSource/forEach.html">forEach</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataSource/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview.datasource/PolygonDataSource/removeAll.html">removeAll</a></li>
<li><a href="mapview.datasource/PolygonDataSource/removeIf.html">removeIf</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataSource/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/PolygonDataSource-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataSource/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonDataSource class</li>
</ol>
<div class="self-name">PolygonDataSource</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/PolygonDataSource-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolygonDataSource class abstract</h1></div>
<section class="desc markdown">
<p>Polygon data source allows the rendering engine access to the user provided
polygons geometry and their attributes.</p>
<p>Polygon segments are rendered following the shortest path between their end points.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolygonDataSource">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-polygondatasource()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-runtimetype
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
<dt class="callable" id="add">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-add(<wbr/>/sdk-for-flutter-explore-mapview-datasource-polygondata-class polygon)
    → void

</dt>
<dd>
  Adds a new polygon to the data source.
  

</dd>
<dt class="callable" id="addPolygons">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-addpolygons(<wbr/>List&lt;<wbr/>/sdk-for-flutter-explore-mapview-datasource-polygondata-class&gt; polygons)
    → void

</dt>
<dd>
  Adds new polygons to the data source.
  

</dd>
<dt class="callable" id="destroy">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-destroy(<wbr/>)
    → void

</dt>
<dd>
  Frees all internally used resources.
  

</dd>
<dt class="callable" id="forEach">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-foreach(<wbr/>/sdk-for-flutter-explore-mapview-datasource-polygondatasourcepolygondataprocessor processor)
    → void

</dt>
<dd>
  Iterates through all the polygons from the data source and passes them to the
given processor, one by one.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeAll">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-removeall(<wbr/>)
    → void

</dt>
<dd>
  Removes all polygons from the data source.
  

</dd>
<dt class="callable" id="removeIf">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-removeif(<wbr/>/sdk-for-flutter-explore-mapview-datasource-polygondatasourcepolygondataprocessor inspector)
    → void

</dt>
<dd>
  Iterates through all the polygons from the data source and passes them to the
given inspector, one by one.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-datasource-polygondatasource-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonDataSource class</li>
</ol>
<h5>mapview.datasource library</h5>
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
