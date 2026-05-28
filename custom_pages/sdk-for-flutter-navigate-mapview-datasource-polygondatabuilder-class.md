---
title: "PolygonDataBuilder class abstract"
slug: "sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PolygonDataBuilder-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview.datasource/PolygonDataBuilder-class.html#constructors">Constructors</a></li>
<li><a href="mapview.datasource/PolygonDataBuilder/PolygonDataBuilder.html">PolygonDataBuilder</a></li>
<li class="section-title inherited">
<a href="mapview.datasource/PolygonDataBuilder-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="mapview.datasource/PolygonDataBuilder/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataBuilder/runtimeType.html">runtimeType</a></li>
<li class="section-title"><a href="mapview.datasource/PolygonDataBuilder-class.html#instance-methods">Methods</a></li>
<li><a href="mapview.datasource/PolygonDataBuilder/build.html">build</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataBuilder/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataBuilder/toString.html">toString</a></li>
<li><a href="mapview.datasource/PolygonDataBuilder/withAttributes.html">withAttributes</a></li>
<li><a href="mapview.datasource/PolygonDataBuilder/withGeometry.html">withGeometry</a></li>
<li class="section-title inherited"><a href="mapview.datasource/PolygonDataBuilder-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview.datasource/PolygonDataBuilder/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li class="self-crumb">PolygonDataBuilder class</li>
</ol>
<div class="self-name">PolygonDataBuilder</div>
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
<div class="main-content" data-above-sidebar="mapview.datasource/mapview.datasource-library-sidebar.html" data-below-sidebar="mapview.datasource/PolygonDataBuilder-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PolygonDataBuilder class abstract</h1></div>
<section class="desc markdown">
<p>Builder of /sdk-for-flutter-navigate-mapview-datasource-polygondata-class instances.</p>
<p>The builder can create /sdk-for-flutter-navigate-mapview-datasource-polygondata-class instances for polygons with an outer boundary and
optionally one or more inner boundaries (holes).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PolygonDataBuilder">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-polygondatabuilder()
</dt>
<dd>
          Creates a builder instance.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-runtimetype
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
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-build(<wbr/>)
    → /sdk-for-flutter-navigate-mapview-datasource-polygondata-class

</dt>
<dd>
  Builds an instance of /sdk-for-flutter-navigate-mapview-datasource-polygondata-class and resets the builder instance.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="withAttributes">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-withattributes(<wbr/>/sdk-for-flutter-navigate-mapview-datasource-dataattributes-class attributes)
    → /sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-class

</dt>
<dd>
  Configures the builder with custom attributes for polygon to be created.
  

</dd>
<dt class="callable" id="withGeometry">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-withgeometry(<wbr/>/sdk-for-flutter-navigate-core-geopolygon-class geometry)
    → /sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-class

</dt>
<dd>
  Configures the builder with geometry for the polygon to be created.
  

</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-mapview-datasource-polygondatabuilder-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">PolygonDataBuilder class</li>
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
