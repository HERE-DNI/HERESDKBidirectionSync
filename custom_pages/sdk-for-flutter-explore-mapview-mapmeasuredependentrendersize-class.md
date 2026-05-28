---
title: "MapMeasureDependentRenderSize class"
slug: "sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMeasureDependentRenderSize-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapMeasureDependentRenderSize-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapMeasureDependentRenderSize/MapMeasureDependentRenderSize.html">MapMeasureDependentRenderSize</a></li>
<li><a href="mapview/MapMeasureDependentRenderSize/MapMeasureDependentRenderSize.withSingleSize.html">withSingleSize</a></li>
<li class="section-title">
<a href="mapview/MapMeasureDependentRenderSize-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapMeasureDependentRenderSize/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapMeasureDependentRenderSize/measureKind.html">measureKind</a></li>
<li class="inherited"><a href="mapview/MapMeasureDependentRenderSize/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapMeasureDependentRenderSize/sizes.html">sizes</a></li>
<li><a href="mapview/MapMeasureDependentRenderSize/sizeUnit.html">sizeUnit</a></li>
<li class="section-title inherited"><a href="mapview/MapMeasureDependentRenderSize-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapMeasureDependentRenderSize/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapMeasureDependentRenderSize/toString.html">toString</a></li>
<li class="section-title"><a href="mapview/MapMeasureDependentRenderSize-class.html#operators">Operators</a></li>
<li><a href="mapview/MapMeasureDependentRenderSize/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapMeasureDependentRenderSize class</li>
</ol>
<div class="self-name">MapMeasureDependentRenderSize</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapMeasureDependentRenderSize-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapMeasureDependentRenderSize class</h1></div>
<section class="desc markdown">
<p>Represents a render size, described as map measure dependent values.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Annotations</dt>
<dd>
<ul class="annotation-list clazz-relationships">
<li>@<a href="https://pub.dev/documentation/meta/1.17.0/meta/immutable-constant.html">immutable</a></li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapMeasureDependentRenderSize">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize(/sdk-for-flutter-explore-mapview-mapmeasurekind measureKind, /sdk-for-flutter-explore-mapview-rendersizeunit sizeUnit, Map&lt;<wbr/>double, double&gt; sizes)
</dt>
<dd>
          Constructs a <code>MapMeasureDependentRenderSize</code> from given parameters.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapMeasureDependentRenderSize.withSingleSize">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize-withsinglesize(/sdk-for-flutter-explore-mapview-rendersizeunit sizeUnit, double size)
</dt>
<dd>
          Constructs a <code>MapMeasureDependentRenderSize</code> from single size value which is constant across all map measures.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="measureKind">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-measurekind
→ /sdk-for-flutter-explore-mapview-mapmeasurekind
</dt>
<dd>
  The unit used for the key in /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes.
  <div class="features">final</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sizes">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes
→ Map&lt;<wbr/>double, double&gt;
</dt>
<dd>
  The dictionary describing the size (value) per map measure (key).
  <div class="features">final</div>
</dd>
<dt class="property" id="sizeUnit">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizeunit
→ /sdk-for-flutter-explore-mapview-rendersizeunit
</dt>
<dd>
  The unit used for the value in /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes.
  <div class="features">final</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

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
<li class="self-crumb">MapMeasureDependentRenderSize class</li>
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
