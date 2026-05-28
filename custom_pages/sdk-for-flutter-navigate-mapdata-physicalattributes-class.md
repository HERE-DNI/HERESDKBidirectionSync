---
title: "PhysicalAttributes class"
slug: "sdk-for-flutter-navigate-mapdata-physicalattributes-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PhysicalAttributes-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/PhysicalAttributes-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/PhysicalAttributes/PhysicalAttributes.html">PhysicalAttributes</a></li>
<li class="section-title">
<a href="mapdata/PhysicalAttributes-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/PhysicalAttributes/divider.html">divider</a></li>
<li><a href="mapdata/PhysicalAttributes/hashCode.html">hashCode</a></li>
<li><a href="mapdata/PhysicalAttributes/isBoatFerry.html">isBoatFerry</a></li>
<li><a href="mapdata/PhysicalAttributes/isBridge.html">isBridge</a></li>
<li><a href="mapdata/PhysicalAttributes/isDirtRoad.html">isDirtRoad</a></li>
<li><a href="mapdata/PhysicalAttributes/isMultiplyDigitized.html">isMultiplyDigitized</a></li>
<li><a href="mapdata/PhysicalAttributes/isPrivate.html">isPrivate</a></li>
<li><a href="mapdata/PhysicalAttributes/isRailFerry.html">isRailFerry</a></li>
<li><a href="mapdata/PhysicalAttributes/isRoundabout.html">isRoundabout</a></li>
<li><a href="mapdata/PhysicalAttributes/isTunnel.html">isTunnel</a></li>
<li class="inherited"><a href="mapdata/PhysicalAttributes/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapdata/PhysicalAttributes-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/PhysicalAttributes/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/PhysicalAttributes/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/PhysicalAttributes-class.html#operators">Operators</a></li>
<li><a href="mapdata/PhysicalAttributes/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">PhysicalAttributes class</li>
</ol>
<div class="self-name">PhysicalAttributes</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/PhysicalAttributes-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>PhysicalAttributes class</h1></div>
<section class="desc markdown">
<p>Physical attributes of the segment.</p>
<p><em><strong>Note</strong></em> a road can have more than one attribute at the same time.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="PhysicalAttributes">
/sdk-for-flutter-navigate-mapdata-physicalattributes-physicalattributes()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="divider">
/sdk-for-flutter-navigate-mapdata-physicalattributes-divider
↔ /sdk-for-flutter-navigate-mapdata-roaddivider?
</dt>
<dd>
  Indicates the presence of a road divider.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-physicalattributes-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isBoatFerry">
/sdk-for-flutter-navigate-mapdata-physicalattributes-isboatferry
↔ bool
</dt>
<dd>
  Identifies a generalised route of a boat ferry for passengers or vehicles over water.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isBridge">
/sdk-for-flutter-navigate-mapdata-physicalattributes-isbridge
↔ bool
</dt>
<dd>
  Identifies a structure that allows a road, railway, or walkway
to pass over another road, railway, waterway, or valley serving
map display and route guidance functionalities.
Bridge is published on segments that represent significant
bridges and/or overpasses; elevated roads are not published as bridge.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isDirtRoad">
/sdk-for-flutter-navigate-mapdata-physicalattributes-isdirtroad
↔ bool
</dt>
<dd>
  Indicates whether the navigable segment is paved.
Paved is primarily used for map display and routing by assigning
higher penalties to unpaved roads.
Paved roads are made of concrete, asphalt, cobblestone or brick.
Unpaved roads do not have a solid surface, e.g. are made of gravel, dirt or grass.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isMultiplyDigitized">
/sdk-for-flutter-navigate-mapdata-physicalattributes-ismultiplydigitized
↔ bool
</dt>
<dd>
  Identifies separately digitised roads, i.e., roads that are digitised with one line per
direction of traffic instead of one line per road.
It may be flagged on roads when certain physical features (e.g. a walkway, a tram, a bus
lane) are located between the separately digitised opposing roadbeds if driver perception
remains unchanged.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isPrivate">
/sdk-for-flutter-navigate-mapdata-physicalattributes-isprivate
↔ bool
</dt>
<dd>
  Private identifies roads that are not maintained by an organization
responsible for maintenance of public roads.
Allows for unique cartographic representation of roads that restrict public use.
May be used to avoid routing through a private road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRailFerry">
/sdk-for-flutter-navigate-mapdata-physicalattributes-israilferry
↔ bool
</dt>
<dd>
  Identifies a generalised route of a ferry for passengers or vehicles via rail. It is applied
on a segment that represent a ferry route for vehicles over rail such as: a route for
ferrying passengers over rail, if destination is not accessible by the road network or
prohibits the use of automobiles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRoundabout">
/sdk-for-flutter-navigate-mapdata-physicalattributes-isroundabout
↔ bool
</dt>
<dd>
  Indicates the presence of a roundabout.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTunnel">
/sdk-for-flutter-navigate-mapdata-physicalattributes-istunnel
↔ bool
</dt>
<dd>
  Identifies an enclosed (on all sides) passageway through or under an obstruction.
This attribute can be used for display or route guidance.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-physicalattributes-runtimetype
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
/sdk-for-flutter-navigate-mapdata-physicalattributes-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-physicalattributes-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-physicalattributes-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">PhysicalAttributes class</li>
</ol>
<h5>mapdata library</h5>
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
