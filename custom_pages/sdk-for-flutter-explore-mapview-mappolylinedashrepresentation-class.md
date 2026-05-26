---
title: "MapPolylineDashRepresentation class abstract"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashRepresentation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapPolylineDashRepresentation-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapPolylineDashRepresentation/MapPolylineDashRepresentation.html">MapPolylineDashRepresentation</a></li>
<li><a href="mapview/MapPolylineDashRepresentation/MapPolylineDashRepresentation.withGapColor.html">withGapColor</a></li>
<li class="section-title">
<a href="mapview/MapPolylineDashRepresentation-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapPolylineDashRepresentation/dashColor.html">dashColor</a></li>
<li><a href="mapview/MapPolylineDashRepresentation/dashLength.html">dashLength</a></li>
<li><a href="mapview/MapPolylineDashRepresentation/gapColor.html">gapColor</a></li>
<li><a href="mapview/MapPolylineDashRepresentation/gapLength.html">gapLength</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapPolylineDashRepresentation/lineWidth.html">lineWidth</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapview/MapPolylineDashRepresentation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapPolylineDashRepresentation-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapItemRepresentation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapPolylineDashRepresentation class</li>
</ol>
<div class="self-name">MapPolylineDashRepresentation</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineDashRepresentation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapPolylineDashRepresentation class abstract</h1></div>
<section class="desc markdown">
<p>Represents a dash pattern for map polyline where the dash can be rendered as a colored
line and the gap can be either empty or colored.</p>
<p>The length of the dash and gap are set independently, allowing for patterns
like <code>'  —  —  —  —'</code> (dash length = gap length) or <code>' ——— ——— ———'</code> (dash length != gap length).</p>
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
<dt class="callable" id="MapPolylineDashRepresentation">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation(/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class lineWidth, /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class dashLength, /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class gapLength, Color dashColor)
</dt>
<dd>
          Creates a representation for a dashed line.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapPolylineDashRepresentation.withGapColor">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation-withgapcolor(/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class lineWidth, /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class dashLength, /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class gapLength, Color dashColor, Color gapColor)
</dt>
<dd>
          Creates a representation for a dashed line with both dash and the gap being colored.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="dashColor">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-dashcolor
→ Color
</dt>
<dd>
  The color of the dashes of the polyline.
Gets the color of the dashes of the polyline.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="dashLength">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-dashlength
→ /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class
</dt>
<dd>
  The dash length of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>dashLength</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>dashLength</code>.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="gapColor">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-gapcolor
→ Color?
</dt>
<dd>
  The color for the gaps of the polyline. The default value is <code>null</code> and
no color is used.
Gets the color for the gaps of the polyline. Returns <code>null</code> if no
color is used.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="gapLength">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-gaplength
→ /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class
</dt>
<dd>
  The gap length of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>gapLength</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>gapLength</code>.
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
<dt class="property" id="lineWidth">
/sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-linewidth
→ /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class
</dt>
<dd>
  The width of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.
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
<li class="self-crumb">MapPolylineDashRepresentation class</li>
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
