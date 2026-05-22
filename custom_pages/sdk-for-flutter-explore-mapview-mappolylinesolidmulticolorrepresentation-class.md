---
title: "Untitled"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidMultiColorRepresentation-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-mapview-mapview-library</li>
<li class="self-crumb">MapPolylineSolidMultiColorRepresentation class</li>
</ol>
<div class="self-name">MapPolylineSolidMultiColorRepresentation</div>
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
<div class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineSolidMultiColorRepresentation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>MapPolylineSolidMultiColorRepresentation class abstract</h1></div>
<section class="desc markdown">
<p>Representation allows map polyline to be colored in multiple specified color segments.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.</p>
<p>Examples:
The following configuration will color map polyline as follows:</p>
<ul>
<li>from the start to the middle of it at the 0.5 point - in Red</li>
<li>from the middle point 0.5 to the 0.7 point - in Green</li>
<li>from 0.7 to 1.0 - in Red
'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
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
<dt class="callable" id="MapPolylineSolidMultiColorRepresentation">
/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation(/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class lineWidth, /sdk-for-flutter-explore-mapview-linecap capShape, List&lt;<wbr/>double&gt; colorStops, List&lt;<wbr/>int&gt; colorIndices, List&lt;<wbr/>Color&gt; colors, double gradientLength)
</dt>
<dd>
          Creates a representation for a multicolored line without an outline.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="MapPolylineSolidMultiColorRepresentation.withOutline">
/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation-withoutline(/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class lineWidth, /sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class outlineWidth, Color outlineColor, /sdk-for-flutter-explore-mapview-linecap capShape, List&lt;<wbr/>double&gt; colorStops, List&lt;<wbr/>int&gt; colorIndices, List&lt;<wbr/>Color&gt; colors, double gradientLength)
</dt>
<dd>
          Creates a representation for a multicolored line with an outline.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-explore-mapview-mapitemrepresentation-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
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
<section class="summary offset-anchor" id="instance-methods">
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
<dt class="callable" id="setMultiColorGradientLength">
/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolorgradientlength(<wbr/>double length)
    → bool

</dt>
<dd>
  Sets the multiple color segment gradient length.
  

</dd>
<dt class="callable" id="setMultiColors">
/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolors(<wbr/>List&lt;<wbr/>double&gt; colorStops, List&lt;<wbr/>int&gt; colorIndices, List&lt;<wbr/>Color&gt; colors)
    → bool

</dt>
<dd>
  Sets lists of colors and multiple color segment stops for the polyline to be colored in.
  

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
<li class="self-crumb">MapPolylineSolidMultiColorRepresentation class</li>
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
