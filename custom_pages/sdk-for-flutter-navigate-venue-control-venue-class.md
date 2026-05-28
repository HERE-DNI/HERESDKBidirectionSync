---
title: "Venue class abstract"
slug: "sdk-for-flutter-navigate-venue-control-venue-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- Venue-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.control/Venue-class.html#constructors">Constructors</a></li>
<li><a href="venue.control/Venue/Venue.html">Venue</a></li>
<li class="section-title">
<a href="venue.control/Venue-class.html#instance-properties">Properties</a>
</li>
<li class="inherited"><a href="venue.control/Venue/hashCode.html">hashCode</a></li>
<li><a href="venue.control/Venue/isTopologyVisible.html">isTopologyVisible</a></li>
<li class="inherited"><a href="venue.control/Venue/runtimeType.html">runtimeType</a></li>
<li><a href="venue.control/Venue/selectedDrawing.html">selectedDrawing</a></li>
<li><a href="venue.control/Venue/selectedLevel.html">selectedLevel</a></li>
<li><a href="venue.control/Venue/selectedLevelIndex.html">selectedLevelIndex</a></li>
<li><a href="venue.control/Venue/selectedLevelZIndex.html">selectedLevelZIndex</a></li>
<li><a href="venue.control/Venue/venueModel.html">venueModel</a></li>
<li><a href="venue.control/Venue/venueStyle.html">venueStyle</a></li>
<li class="section-title"><a href="venue.control/Venue-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="venue.control/Venue/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="venue.control/Venue/setCustomStyle.html">setCustomStyle</a></li>
<li><a href="venue.control/Venue/setCustomStyleToCrosswalk.html">setCustomStyleToCrosswalk</a></li>
<li><a href="venue.control/Venue/setCustomStyleToTopology.html">setCustomStyleToTopology</a></li>
<li class="inherited"><a href="venue.control/Venue/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.control/Venue-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.control/Venue/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li class="self-crumb">Venue class</li>
</ol>
<div class="self-name">Venue</div>
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
<div class="main-content" data-above-sidebar="venue.control/venue.control-library-sidebar.html" data-below-sidebar="venue.control/Venue-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>Venue class abstract</h1></div>
<section class="desc markdown">
<p>Controls the /sdk-for-flutter-navigate-venue-data-venuemodel-class inside the /sdk-for-flutter-navigate-venue-control-venuemap-class object.</p>
<p>The venue controls the selection of the /sdk-for-flutter-navigate-venue-data-venuedrawing-class and the /sdk-for-flutter-navigate-venue-data-venuelevel-class
of the /sdk-for-flutter-navigate-venue-data-venuemodel-class. It provides the possibility to customize styles for the /sdk-for-flutter-navigate-venue-data-venuegeometry-class.
Objects of this class can only be created using methods
/sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrorsstr and /sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrorsstr.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="Venue">
/sdk-for-flutter-navigate-venue-control-venue-venue()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-control-venue-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isTopologyVisible">
/sdk-for-flutter-navigate-venue-control-venue-istopologyvisible
↔ bool
</dt>
<dd>
  Returns true if topology is visible.
It can be used to check the status of topology visibility.
Gets the current status of topology visibility.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-control-venue-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="selectedDrawing">
/sdk-for-flutter-navigate-venue-control-venue-selecteddrawing
↔ /sdk-for-flutter-navigate-venue-data-venuedrawing-class
</dt>
<dd>
  The selected drawing.
Only the selected drawing will be visible as active on the map. All others will be
hidden or displayed without details, depending on the implementation of the renderer.
Gets the currently selected /sdk-for-flutter-navigate-venue-data-venuedrawing-class of the /sdk-for-flutter-navigate-venue-data-venuemodel-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="selectedLevel">
/sdk-for-flutter-navigate-venue-control-venue-selectedlevel
↔ /sdk-for-flutter-navigate-venue-data-venuelevel-class
</dt>
<dd>
  The selected level.
Only the selected level will be visible as active on the map. All others will be
hidden or displayed without details, depending on a renderer implementation.
If the level doesn't belong to the currently selected drawing, it can not be selected.
Gets the currently selected /sdk-for-flutter-navigate-venue-data-venuelevel-class from the selected /sdk-for-flutter-navigate-venue-data-venuedrawing-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="selectedLevelIndex">
/sdk-for-flutter-navigate-venue-control-venue-selectedlevelindex
↔ int
</dt>
<dd>
  The index of the /sdk-for-flutter-navigate-venue-data-venuelevel-class selected from the level array
of the /sdk-for-flutter-navigate-venue-data-venuedrawing-class.
Unlike the Z index, it can't have a negative value.
Gets the index of the currently selected /sdk-for-flutter-navigate-venue-data-venuelevel-class in the level array
of the related /sdk-for-flutter-navigate-venue-data-venuedrawing-class. The level array can be taken from
/sdk-for-flutter-navigate-venue-data-venuedrawing-levels.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="selectedLevelZIndex">
/sdk-for-flutter-navigate-venue-control-venue-selectedlevelzindex
↔ int
</dt>
<dd>
  The Z index value of the /sdk-for-flutter-navigate-venue-data-venuelevel-class selected.
Z index 0 represents the ground level, negative values represent
underground levels, positive values - levels above the ground.
Z index can also be taken from /sdk-for-flutter-navigate-venue-data-venuelevel-zindex.
Gets the Z index of the currently selected /sdk-for-flutter-navigate-venue-data-venuelevel-class.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="venueModel">
/sdk-for-flutter-navigate-venue-control-venue-venuemodel
→ /sdk-for-flutter-navigate-venue-data-venuemodel-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-venue-data-venuemodel-class controlled by this object.
It can be used to get the /sdk-for-flutter-navigate-venue-data-venuemodel-class
belonging to this object, like a building or a complex of buildings.
Gets the /sdk-for-flutter-navigate-venue-data-venuemodel-class controlled by this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="venueStyle">
/sdk-for-flutter-navigate-venue-control-venue-venuestyle
→ /sdk-for-flutter-navigate-venue-style-venuestyle-class
</dt>
<dd>
  The /sdk-for-flutter-navigate-venue-style-venuestyle-class associated with the /sdk-for-flutter-navigate-venue-data-venuemodel-class
controlled by this object.
It can be used to get the style of the venue. Contains the information about
the geometry and label styles available for the venue.
Gets the /sdk-for-flutter-navigate-venue-style-venuestyle-class associated with the /sdk-for-flutter-navigate-venue-data-venuemodel-class
controlled by this object.
  <div class="features">no setter</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-control-venue-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setCustomStyle">
/sdk-for-flutter-navigate-venue-control-venue-setcustomstyle(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-venue-data-venuegeometry-class&gt; geometries, /sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class? style, /sdk-for-flutter-navigate-venue-style-venuelabelstyle-class? labelStyle)
    → void

</dt>
<dd>
  Sets a custom style for geometries and related labels.
  

</dd>
<dt class="callable" id="setCustomStyleToCrosswalk">
/sdk-for-flutter-navigate-venue-control-venue-setcustomstyletocrosswalk(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-venue-data-crosswalk-class&gt; crosswalks, /sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class? style)
    → void

</dt>
<dd>
  Sets a custom style for crosswalk.
  

</dd>
<dt class="callable" id="setCustomStyleToTopology">
/sdk-for-flutter-navigate-venue-control-venue-setcustomstyletotopology(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-venue-data-venuetopology-class&gt; topologies, /sdk-for-flutter-navigate-venue-style-venuegeometrystyle-class? style)
    → void

</dt>
<dd>
  Sets a custom style for topologies.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-control-venue-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-control-venue-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li class="self-crumb">Venue class</li>
</ol>
<h5>venue.control library</h5>
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
