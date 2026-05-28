---
title: "LineDataSource class abstract"
slug: "sdk-for-flutter-navigate-mapview-datasource-linedatasource-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LineDataSource-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/LineDataSource-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/LineDataSource/LineDataSource.html">LineDataSource</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/LineDataSource-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/LineDataSource/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/LineDataSource/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/LineDataSource-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/LineDataSource/add.html">add</a></li>
<li><a href="mapview.datasource/LineDataSource/addLines.html">addLines</a></li>
<li><a href="mapview.datasource/LineDataSource/destroy.html">destroy</a></li>
<li><a href="mapview.datasource/LineDataSource/forEach.html">forEach</a></li>
<li class="inherited"><a href="mapview.datasource/LineDataSource/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview.datasource/LineDataSource/removeAll.html">removeAll</a></li>
<li><a href="mapview.datasource/LineDataSource/removeIf.html">removeIf</a></li>
<li class="inherited"><a href="mapview.datasource/LineDataSource/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview.datasource/LineDataSource-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/LineDataSource/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">LineDataSource class</li>
</ol>
<div class="self-name">LineDataSource</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/LineDataSource-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LineDataSource class abstract</h1></div>
<section class="desc markdown">
<p>Polyline data source allows the rendering engine access to the user provided
polylines geometry and their attributes.</p>
<p>Polyline segments are rendered following the shortest path between their end vertices.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LineDataSource">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-linedatasource()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-runtimetype
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
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-add(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-linedata-class line)
    → void

</dt>
<dd>
  Adds a new line to the data source.
  

</dd>
<dt class="callable" id="addLines">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-addlines(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-mapview-datasource-linedata-class&gt; lines)
    → void

</dt>
<dd>
  Adds new lines to the data source.
  

</dd>
<dt class="callable" id="destroy">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-destroy(<wbr/>)
    → void

</dt>
<dd>
  Frees all internally used resources.
  

</dd>
<dt class="callable" id="forEach">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-foreach(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-linedatasourcelinedataprocessor processor)
    → void

</dt>
<dd>
  Iterates through all the lines from the data source and passes them to the
given processor, one by one.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="removeAll">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-removeall(<wbr/>)
    → void

</dt>
<dd>
  Removes all lines from the data source.
  

</dd>
<dt class="callable" id="removeIf">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-removeif(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-linedatasourcelinedataprocessor inspector)
    → void

</dt>
<dd>
  Iterates through all the lines from the data source and passes them to the
given inspector, one by one.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapview-datasource-linedatasource-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">LineDataSource class</li>
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
