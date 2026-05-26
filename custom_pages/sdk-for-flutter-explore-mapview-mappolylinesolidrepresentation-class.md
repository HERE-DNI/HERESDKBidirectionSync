---
title: "MapPolylineSolidRepresentation class abstract"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapPolylineSolidRepresentation-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapPolylineSolidRepresentation/MapPolylineSolidRepresentation.html">MapPolylineSolidRepresentation</a></li>
<li><a href="mapview/MapPolylineSolidRepresentation/MapPolylineSolidRepresentation.withOutline.html">withOutline</a></li>
<li class="section-title">
<a href="mapview/MapPolylineSolidRepresentation-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapPolylineSolidRepresentation/capShape.html">capShape</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapPolylineSolidRepresentation/lineColor.html">lineColor</a></li>
<li><a href="mapview/MapPolylineSolidRepresentation/lineWidth.html">lineWidth</a></li>
<li><a href="mapview/MapPolylineSolidRepresentation/outlineColor.html">outlineColor</a></li>
<li><a href="mapview/MapPolylineSolidRepresentation/outlineWidth.html">outlineWidth</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapPolylineSolidRepresentation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapPolylineSolidRepresentation-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapPolylineSolidRepresentation class</li>
</ol>
<div class="self-name">MapPolylineSolidRepresentation</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineSolidRepresentation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapPolylineSolidRepresentation class abstract</h1></div>
<section class="desc markdown">
<p>Representation for a solid line without outline.</p>
<p>Can represent polylines that have constant width or width dependent on the map zoom.</p>
<p>To achieve constant width lines, use /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class with a single value.</p>
<p>To achieve line width dependent on map zoom, use /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class with
multiple values.</p>
<p>For /sdk-for-flutter-explore-mapview-mapmeasurekind only /sdk-for-flutter-explore-mapview-mapmeasurekind is supported.</p>
<p>For /sdk-for-flutter-explore-mapview-rendersizeunit only /sdk-for-flutter-explore-mapview-rendersizeunit is supported.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-explore-mapview-mappolylinerepresentation-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapPolylineSolidRepresentation">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation(/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class lineWidth, Color color, /sdk-for-flutter-explore-mapview-linecap capShape)
</dt>
<dd>
          Creates a representation for a solid line without outline.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapPolylineSolidRepresentation.withOutline">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation-withoutline(/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class lineWidth, Color color, /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class outlineWidth, Color outlineColor, /sdk-for-flutter-explore-mapview-linecap capShape)
</dt>
<dd>
          Creates a representation for a solid line with outline.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="capShape">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-capshape
→ /sdk-for-flutter-explore-mapview-linecap
</dt>
<dd>
  The cap shape applied to both ends of the polyline and its outline.
Returns the cap shape of the polyline and its outline.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapitemrepresentation-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="lineColor">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-linecolor
→ Color
</dt>
<dd>
  The color of the polyline.
Gets the color of the polyline.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lineWidth">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-linewidth
→ /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class
</dt>
<dd>
  The width of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="outlineColor">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-outlinecolor
→ Color
</dt>
<dd>
  The outline color of the polyline.
Gets the color of outline of the polyline.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="outlineWidth">
/sdk-for-flutter-explore-mapview-mappolylinesolidrepresentation-outlinewidth
→ /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class
</dt>
<dd>
  The width of the outline on one side of the polyline depending on the map measure.
The total width of the polyline is <code>line width + 2 * outline width</code>.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mapitemrepresentation-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mapitemrepresentation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mapitemrepresentation-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-mapitemrepresentation-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">MapPolylineSolidRepresentation class</li>
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
