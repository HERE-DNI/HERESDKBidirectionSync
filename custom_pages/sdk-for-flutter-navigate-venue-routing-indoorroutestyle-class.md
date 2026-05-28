---
title: "IndoorRouteStyle class abstract"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutestyle-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- IndoorRouteStyle-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="venue.routing/IndoorRouteStyle-class.html#constructors">Constructors</a></li>
<li><a href="venue.routing/IndoorRouteStyle/IndoorRouteStyle.html">IndoorRouteStyle</a></li>
<li class="section-title">
<a href="venue.routing/IndoorRouteStyle-class.html#instance-properties">Properties</a>
</li>
<li><a href="venue.routing/IndoorRouteStyle/destinationMarker.html">destinationMarker</a></li>
<li><a href="venue.routing/IndoorRouteStyle/driveMarker.html">driveMarker</a></li>
<li class="inherited"><a href="venue.routing/IndoorRouteStyle/hashCode.html">hashCode</a></li>
<li><a href="venue.routing/IndoorRouteStyle/indoorPolylineColor.html">indoorPolylineColor</a></li>
<li><a href="venue.routing/IndoorRouteStyle/indoorPolylineWidth.html">indoorPolylineWidth</a></li>
<li class="inherited"><a href="venue.routing/IndoorRouteStyle/runtimeType.html">runtimeType</a></li>
<li><a href="venue.routing/IndoorRouteStyle/startMarker.html">startMarker</a></li>
<li><a href="venue.routing/IndoorRouteStyle/walkMarker.html">walkMarker</a></li>
<li class="section-title"><a href="venue.routing/IndoorRouteStyle-class.html#instance-methods">Methods</a></li>
<li><a href="venue.routing/IndoorRouteStyle/getIndoorMarkerFor.html">getIndoorMarkerFor</a></li>
<li class="inherited"><a href="venue.routing/IndoorRouteStyle/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="venue.routing/IndoorRouteStyle/setIndoorMarkersFor.html">setIndoorMarkersFor</a></li>
<li class="inherited"><a href="venue.routing/IndoorRouteStyle/toString.html">toString</a></li>
<li class="section-title inherited"><a href="venue.routing/IndoorRouteStyle-class.html#operators">Operators</a></li>
<li class="inherited"><a href="venue.routing/IndoorRouteStyle/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li class="self-crumb">IndoorRouteStyle class</li>
</ol>
<div class="self-name">IndoorRouteStyle</div>
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
<div class="main-content" data-above-sidebar="venue.routing/venue.routing-library-sidebar.html" data-below-sidebar="venue.routing/IndoorRouteStyle-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>IndoorRouteStyle class abstract</h1></div>
<section class="desc markdown">
<p>Represents a style of the indoor route.</p>
<p>Contains information about route colors and widths.
Optionally, this style allows to set /sdk-for-flutter-navigate-mapview-mapmarker-class instances that can be used for
specific route elements.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="IndoorRouteStyle">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-indoorroutestyle()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="destinationMarker">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-destinationmarker
↔ /sdk-for-flutter-navigate-mapview-mapmarker-class?
</dt>
<dd>
  A /sdk-for-flutter-navigate-mapview-mapmarker-class instance representing the destination of the route. By default, no map marker is provided
The destination map marker of the resulting route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="driveMarker">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-drivemarker
↔ /sdk-for-flutter-navigate-mapview-mapmarker-class?
</dt>
<dd>
  A /sdk-for-flutter-navigate-mapview-mapmarker-class instance representing the drive point of the route. By default, no map marker is provided.
The drive map marker of the resulting route. It signals that a user should take a transport vehicle.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="indoorPolylineColor">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-indoorpolylinecolor
↔ Color
</dt>
<dd>
  The color value. The default color is #48DAD0.
The color of polylines for indoor route sections.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="indoorPolylineWidth">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-indoorpolylinewidth
↔ double
</dt>
<dd>
  The width in pixels. Default value is 15 pixels
The width in pixels of polylines for indoor route sections.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="startMarker">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-startmarker
↔ /sdk-for-flutter-navigate-mapview-mapmarker-class?
</dt>
<dd>
  A /sdk-for-flutter-navigate-mapview-mapmarker-class instance representing the start of the route. By default, no map marker is provided.
The start map marker of the resulting route.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="walkMarker">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-walkmarker
↔ /sdk-for-flutter-navigate-mapview-mapmarker-class?
</dt>
<dd>
  A /sdk-for-flutter-navigate-mapview-mapmarker-class instance representing the walk point of the route. By default, no map marker is provided.
The walk map marker of the resulting route. It signals that a user should leave their transport vehicle and continue on foot.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="getIndoorMarkerFor">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-getindoormarkerfor(<wbr/>/sdk-for-flutter-navigate-routing-indoorlevelchangefeatures feature, int deltaZ)
    → /sdk-for-flutter-navigate-mapview-mapmarker-class?

</dt>
<dd>
  Returns a /sdk-for-flutter-navigate-mapview-mapmarker-class for a given indoor feature and
the number of levels to change.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setIndoorMarkersFor">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-setindoormarkersfor(<wbr/>/sdk-for-flutter-navigate-routing-indoorlevelchangefeatures feature, /sdk-for-flutter-navigate-mapview-mapmarker-class? upMarker, /sdk-for-flutter-navigate-mapview-mapmarker-class? downMarker, /sdk-for-flutter-navigate-mapview-mapmarker-class? exitMarker)
    → void

</dt>
<dd>
  Sets map markers for the given indoor feature.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-venue-routing-indoorroutestyle-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li class="self-crumb">IndoorRouteStyle class</li>
</ol>
<h5>venue.routing library</h5>
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
