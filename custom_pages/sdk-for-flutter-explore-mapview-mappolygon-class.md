---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mappolygon-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolygon-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapPolygon-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapPolygon/MapPolygon.html">MapPolygon</a></li>
<li><a href="mapview/MapPolygon/MapPolygon.withOutlineColorAndOutlineWidthInPixels.html">withOutlineColorAndOutlineWidthInPixels</a></li>
<li class="section-title">
<a href="mapview/MapPolygon-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapPolygon/drawOrder.html">drawOrder</a></li>
<li><a href="mapview/MapPolygon/fillColor.html">fillColor</a></li>
<li><a href="mapview/MapPolygon/geometry.html">geometry</a></li>
<li class="inherited"><a href="mapview/MapPolygon/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapPolygon/metadata.html">metadata</a></li>
<li><a href="mapview/MapPolygon/outlineColor.html">outlineColor</a></li>
<li><a href="mapview/MapPolygon/outlineWidth.html">outlineWidth</a></li>
<li class="inherited"><a href="mapview/MapPolygon/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapPolygon/visibilityRanges.html">visibilityRanges</a></li>
<li class="section-title inherited"><a href="mapview/MapPolygon-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapview/MapPolygon/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapview/MapPolygon/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapPolygon-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapPolygon/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapPolygon class</li>
</ol>
<div class="self-name">MapPolygon</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolygon-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapPolygon class abstract</h1></div>
<section class="desc markdown">
<p>A visual representation of a polygon on the map.</p>
<p>Can be used to visualize areas of all shapes
and sizes.</p>
<p>The geometry to be visualized is represented by an instance of <a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a>.
To display circular areas (for example, a position accuracy indicator) use a GeoPolygon
created from a <a href="../core/GeoCircle-class.html">/sdk-for-flutter-explore-core-geocircle-class</a> using <a href="../core/GeoPolygon/GeoPolygon.withGeoCircle.html">/sdk-for-flutter-explore-core-geopolygon-geopolygon-withgeocircle</a>.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapPolygon">
<a href="../mapview/MapPolygon/MapPolygon.html">/sdk-for-flutter-explore-mapview-mappolygon-mappolygon</a>(<a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a> geometry, Color color)
</dt>
<dd>
          Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapPolygon.withOutlineColorAndOutlineWidthInPixels">
<a href="../mapview/MapPolygon/MapPolygon.withOutlineColorAndOutlineWidthInPixels.html">/sdk-for-flutter-explore-mapview-mappolygon-mappolygon-withoutlinecolorandoutlinewidthinpixels</a>(<a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a> geometry, Color color, Color outlineColor, double outlineWidthInPixels)
</dt>
<dd>
          Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="drawOrder">
<a href="../mapview/MapPolygon/drawOrder.html">/sdk-for-flutter-explore-mapview-mappolygon-draworder</a>
↔ int
</dt>
<dd>
  The draw order of this map polygon relative to other map polygons.
Gets the draw order of this map polygon relative to other map polygons. Default value is 0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fillColor">
<a href="../mapview/MapPolygon/fillColor.html">/sdk-for-flutter-explore-mapview-mappolygon-fillcolor</a>
↔ Color
</dt>
<dd>
  Color of the polygon's fill.
Gets the current color of the fill.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="geometry">
<a href="../mapview/MapPolygon/geometry.html">/sdk-for-flutter-explore-mapview-mappolygon-geometry</a>
↔ <a href="../core/GeoPolygon-class.html">/sdk-for-flutter-explore-core-geopolygon-class</a>
</dt>
<dd>
  The geometry of the polygon. Setting a new geometry will update the appearance.
Gets the current geometry of the polygon.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapPolygon/hashCode.html">/sdk-for-flutter-explore-mapview-mappolygon-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="metadata">
<a href="../mapview/MapPolygon/metadata.html">/sdk-for-flutter-explore-mapview-mappolygon-metadata</a>
↔ <a href="../core/Metadata-class.html">/sdk-for-flutter-explore-core-metadata-class</a>?
</dt>
<dd>
  The Metadata instance attached to this polygon, <code>null</code> by default.
Gets the Metadata instance attached to this polygon.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="outlineColor">
<a href="../mapview/MapPolygon/outlineColor.html">/sdk-for-flutter-explore-mapview-mappolygon-outlinecolor</a>
↔ Color
</dt>
<dd>
  The color of the polygon outline.
Gets the color of the polygon outline. The default outline color is opaque white.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="outlineWidth">
<a href="../mapview/MapPolygon/outlineWidth.html">/sdk-for-flutter-explore-mapview-mappolygon-outlinewidth</a>
↔ double
</dt>
<dd>
  The width of the polygon outline in pixels.
Gets the outline width of the polygon in pixels.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapPolygon/runtimeType.html">/sdk-for-flutter-explore-mapview-mappolygon-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="visibilityRanges">
<a href="../mapview/MapPolygon/visibilityRanges.html">/sdk-for-flutter-explore-mapview-mappolygon-visibilityranges</a>
↔ List&lt;<wbr/><a href="../mapview/MapMeasureRange-class.html">/sdk-for-flutter-explore-mapview-mapmeasurerange-class</a>&gt;
</dt>
<dd>
  The list of visibility ranges. The map polygon is visible only inside these map measure ranges.
Gets the list of visibility ranges. The map polygon is visible only inside these map measure
ranges. When empty (the default), the map polygon is visible without map measure restrictions.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapPolygon/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mappolygon-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapPolygon/toString.html">/sdk-for-flutter-explore-mapview-mappolygon-tostring</a>(<wbr/>)
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
<a href="../mapview/MapPolygon/operator_equals.html">/sdk-for-flutter-explore-mapview-mappolygon-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">MapPolygon class</li>
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
