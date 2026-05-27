---
title: "Constructors"
slug: "sdk-for-flutter-explore-mapview-mappolyline-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- MapPolyline-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapview/MapPolyline-class.html#constructors">Constructors</a></li>
<li><a href="mapview/MapPolyline/MapPolyline.withRepresentation.html">withRepresentation</a></li>
<li class="section-title">
<a href="mapview/MapPolyline-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapview/MapPolyline/drawOrder.html">drawOrder</a></li>
<li><a href="mapview/MapPolyline/drawOrderType.html">drawOrderType</a></li>
<li><a href="mapview/MapPolyline/geometry.html">geometry</a></li>
<li class="inherited"><a href="mapview/MapPolyline/hashCode.html">hashCode</a></li>
<li><a href="mapview/MapPolyline/mapContentCategoriesToBlock.html">mapContentCategoriesToBlock</a></li>
<li><a href="mapview/MapPolyline/metadata.html">metadata</a></li>
<li><a href="mapview/MapPolyline/progress.html">progress</a></li>
<li><a href="mapview/MapPolyline/progressColor.html">progressColor</a></li>
<li><a href="mapview/MapPolyline/progressGradientLength.html">progressGradientLength</a></li>
<li><a href="mapview/MapPolyline/progressOutlineColor.html">progressOutlineColor</a></li>
<li class="inherited"><a href="mapview/MapPolyline/runtimeType.html">runtimeType</a></li>
<li><a href="mapview/MapPolyline/visibilityRanges.html">visibilityRanges</a></li>
<li class="section-title"><a href="mapview/MapPolyline-class.html#instance-methods">Methods</a></li>
<li><a href="mapview/MapPolyline/cancelAnimation.html">cancelAnimation</a></li>
<li class="inherited"><a href="mapview/MapPolyline/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="mapview/MapPolyline/setRepresentation.html">setRepresentation</a></li>
<li><a href="mapview/MapPolyline/startAnimation.html">startAnimation</a></li>
<li class="inherited"><a href="mapview/MapPolyline/toString.html">toString</a></li>
<li class="section-title inherited"><a href="mapview/MapPolyline-class.html#operators">Operators</a></li>
<li class="inherited"><a href="mapview/MapPolyline/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../mapview/mapview-library.html">/sdk-for-flutter-explore-mapview-mapview-library</a></li>
<li class="self-crumb">MapPolyline class</li>
</ol>
<div class="self-name">MapPolyline</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolyline-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapPolyline class abstract</h1></div>
<section class="desc markdown">
<p>A visual representation of a line on the map.</p>
<p>The geometry to be visualized is represented by an instance of <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a>.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapPolyline.withRepresentation">
<a href="../mapview/MapPolyline/MapPolyline.withRepresentation.html">/sdk-for-flutter-explore-mapview-mappolyline-mappolyline-withrepresentation</a>(<a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a> geometry, <a href="../mapview/MapPolylineRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinerepresentation-class</a> representation)
</dt>
<dd>
          Creates a new <code>MapPolyline</code> instance with a specified visual representation.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="drawOrder">
<a href="../mapview/MapPolyline/drawOrder.html">/sdk-for-flutter-explore-mapview-mappolyline-draworder</a>
↔ int
</dt>
<dd>
  The draw order of the polyline.
Gets the draw order of the polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="drawOrderType">
<a href="../mapview/MapPolyline/drawOrderType.html">/sdk-for-flutter-explore-mapview-mappolyline-drawordertype</a>
↔ <a href="../mapview/DrawOrderType.html">/sdk-for-flutter-explore-mapview-drawordertype</a>
</dt>
<dd>
  The draw order type of the polyline.
Gets the draw order type of the polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="geometry">
<a href="../mapview/MapPolyline/geometry.html">/sdk-for-flutter-explore-mapview-mappolyline-geometry</a>
↔ <a href="../core/GeoPolyline-class.html">/sdk-for-flutter-explore-core-geopolyline-class</a>
</dt>
<dd>
  The list of vertices that represent the geometry of the polyline.
Gets the geometry of the polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
<a href="../mapview/MapPolyline/hashCode.html">/sdk-for-flutter-explore-mapview-mappolyline-hashcode</a>
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="mapContentCategoriesToBlock">
<a href="../mapview/MapPolyline/mapContentCategoriesToBlock.html">/sdk-for-flutter-explore-mapview-mappolyline-mapcontentcategoriestoblock</a>
↔ List&lt;<wbr/><a href="../mapview/MapContentCategory.html">/sdk-for-flutter-explore-mapview-mapcontentcategory</a>&gt;
</dt>
<dd>
  List of map content categories this polyline should block.
Gets list of map content categories this polyline should block.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="metadata">
<a href="../mapview/MapPolyline/metadata.html">/sdk-for-flutter-explore-mapview-mappolyline-metadata</a>
↔ <a href="../core/Metadata-class.html">/sdk-for-flutter-explore-core-metadata-class</a>?
</dt>
<dd>
  The <code>Metadata</code> instance attached to this polyline.
Gets the <code>Metadata</code> instance attached to this polyline.
This will be <code>null</code> if nothing has been attached before.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progress">
<a href="../mapview/MapPolyline/progress.html">/sdk-for-flutter-explore-mapview-mappolyline-progress</a>
↔ double
</dt>
<dd>
  The progress from the polyline's starting point, as a ratio of its total length clamped to
the range [0, 1].
Gets the progress of the polyline, 0 by default.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progressColor">
<a href="../mapview/MapPolyline/progressColor.html">/sdk-for-flutter-explore-mapview-mappolyline-progresscolor</a>
↔ Color
</dt>
<dd>
  The color used for the progress part of the polyline.
Gets the progress color of the polyline, opaque white by default.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progressGradientLength">
<a href="../mapview/MapPolyline/progressGradientLength.html">/sdk-for-flutter-explore-mapview-mappolyline-progressgradientlength</a>
↔ <a href="../mapview/MapMeasureDependentRenderSize-class.html">/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class</a>
</dt>
<dd>
  The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
Gets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progressOutlineColor">
<a href="../mapview/MapPolyline/progressOutlineColor.html">/sdk-for-flutter-explore-mapview-mappolyline-progressoutlinecolor</a>
↔ Color
</dt>
<dd>
  The color used for outline of the progress part of the polyline.
Gets the progress outline color of the polyline, opaque white by default.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../mapview/MapPolyline/runtimeType.html">/sdk-for-flutter-explore-mapview-mappolyline-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="visibilityRanges">
<a href="../mapview/MapPolyline/visibilityRanges.html">/sdk-for-flutter-explore-mapview-mappolyline-visibilityranges</a>
↔ List&lt;<wbr/><a href="../mapview/MapMeasureRange-class.html">/sdk-for-flutter-explore-mapview-mapmeasurerange-class</a>&gt;
</dt>
<dd>
  The list of visibility ranges. The map polyline is visible only inside these map measure ranges.
Gets the list of visibility ranges. The map polyline is visible only inside these map measure
ranges. When empty (the default), the map polyline is visible without map measure restrictions.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="cancelAnimation">
<a href="../mapview/MapPolyline/cancelAnimation.html">/sdk-for-flutter-explore-mapview-mappolyline-cancelanimation</a>(<wbr/><a href="../animation/MapPolylineAnimation-class.html">/sdk-for-flutter-explore-animation-mappolylineanimation-class</a> animation)
    → void

</dt>
<dd>
  Cancels single ongoing animation of this map polyline.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../mapview/MapPolyline/noSuchMethod.html">/sdk-for-flutter-explore-mapview-mappolyline-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setRepresentation">
<a href="../mapview/MapPolyline/setRepresentation.html">/sdk-for-flutter-explore-mapview-mappolyline-setrepresentation</a>(<wbr/><a href="../mapview/MapPolylineRepresentation-class.html">/sdk-for-flutter-explore-mapview-mappolylinerepresentation-class</a> representation)
    → void

</dt>
<dd>
  Changes the appearance of the <code>MapPolyline</code> instance.
  

</dd>
<dt class="callable" id="startAnimation">
<a href="../mapview/MapPolyline/startAnimation.html">/sdk-for-flutter-explore-mapview-mappolyline-startanimation</a>(<wbr/><a href="../animation/MapPolylineAnimation-class.html">/sdk-for-flutter-explore-animation-mappolylineanimation-class</a> animation, <a href="../animation/AnimationListener-class.html">/sdk-for-flutter-explore-animation-animationlistener-class</a> listener)
    → void

</dt>
<dd>
  Starts an animation of this map polyline.
  

</dd>
<dt class="callable inherited" id="toString">
<a href="../mapview/MapPolyline/toString.html">/sdk-for-flutter-explore-mapview-mappolyline-tostring</a>(<wbr/>)
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
<a href="../mapview/MapPolyline/operator_equals.html">/sdk-for-flutter-explore-mapview-mappolyline-operator-equals</a>(<wbr/>Object other)
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
<li class="self-crumb">MapPolyline class</li>
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
