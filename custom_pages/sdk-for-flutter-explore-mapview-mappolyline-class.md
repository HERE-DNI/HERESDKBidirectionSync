---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mappolyline-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolyline-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
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
<p>The geometry to be visualized is represented by an instance of /sdk-for-flutter-explore-core-geopolyline-class.</p>
<p>Altitude component of <code>GeoPolyline</code>'s vertices is ignored.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="MapPolyline.withRepresentation">
/sdk-for-flutter-explore-mapview-mappolyline-mappolyline-withrepresentation(/sdk-for-flutter-explore-core-geopolyline-class geometry, /sdk-for-flutter-explore-mapview-mappolylinerepresentation-class representation)
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
/sdk-for-flutter-explore-mapview-mappolyline-draworder
↔ int
</dt>
<dd>
  The draw order of the polyline.
Gets the draw order of the polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="drawOrderType">
/sdk-for-flutter-explore-mapview-mappolyline-drawordertype
↔ /sdk-for-flutter-explore-mapview-drawordertype
</dt>
<dd>
  The draw order type of the polyline.
Gets the draw order type of the polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="geometry">
/sdk-for-flutter-explore-mapview-mappolyline-geometry
↔ /sdk-for-flutter-explore-core-geopolyline-class
</dt>
<dd>
  The list of vertices that represent the geometry of the polyline.
Gets the geometry of the polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mappolyline-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="mapContentCategoriesToBlock">
/sdk-for-flutter-explore-mapview-mappolyline-mapcontentcategoriestoblock
↔ List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapcontentcategory&gt;
</dt>
<dd>
  List of map content categories this polyline should block.
Gets list of map content categories this polyline should block.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="metadata">
/sdk-for-flutter-explore-mapview-mappolyline-metadata
↔ /sdk-for-flutter-explore-core-metadata-class?
</dt>
<dd>
  The <code>Metadata</code> instance attached to this polyline.
Gets the <code>Metadata</code> instance attached to this polyline.
This will be <code>null</code> if nothing has been attached before.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progress">
/sdk-for-flutter-explore-mapview-mappolyline-progress
↔ double
</dt>
<dd>
  The progress from the polyline's starting point, as a ratio of its total length clamped to
the range [0, 1].
Gets the progress of the polyline, 0 by default.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progressColor">
/sdk-for-flutter-explore-mapview-mappolyline-progresscolor
↔ Color
</dt>
<dd>
  The color used for the progress part of the polyline.
Gets the progress color of the polyline, opaque white by default.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progressGradientLength">
/sdk-for-flutter-explore-mapview-mappolyline-progressgradientlength
↔ /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class
</dt>
<dd>
  The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
Gets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="progressOutlineColor">
/sdk-for-flutter-explore-mapview-mappolyline-progressoutlinecolor
↔ Color
</dt>
<dd>
  The color used for outline of the progress part of the polyline.
Gets the progress outline color of the polyline, opaque white by default.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-mapview-mappolyline-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="visibilityRanges">
/sdk-for-flutter-explore-mapview-mappolyline-visibilityranges
↔ List&lt;<wbr/>/sdk-for-flutter-explore-mapview-mapmeasurerange-class&gt;
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
/sdk-for-flutter-explore-mapview-mappolyline-cancelanimation(<wbr/>/sdk-for-flutter-explore-animation-mappolylineanimation-class animation)
    → void

</dt>
<dd>
  Cancels single ongoing animation of this map polyline.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-explore-mapview-mappolyline-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setRepresentation">
/sdk-for-flutter-explore-mapview-mappolyline-setrepresentation(<wbr/>/sdk-for-flutter-explore-mapview-mappolylinerepresentation-class representation)
    → void

</dt>
<dd>
  Changes the appearance of the <code>MapPolyline</code> instance.
  

</dd>
<dt class="callable" id="startAnimation">
/sdk-for-flutter-explore-mapview-mappolyline-startanimation(<wbr/>/sdk-for-flutter-explore-animation-mappolylineanimation-class animation, /sdk-for-flutter-explore-animation-animationlistener-class listener)
    → void

</dt>
<dd>
  Starts an animation of this map polyline.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-mapview-mappolyline-tostring(<wbr/>)
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
/sdk-for-flutter-explore-mapview-mappolyline-operator-equals(<wbr/>Object other)
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



</div>
`
}</HTMLBlock>
