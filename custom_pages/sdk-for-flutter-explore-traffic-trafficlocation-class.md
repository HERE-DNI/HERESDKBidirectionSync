---
title: "TrafficLocation class"
slug: "sdk-for-flutter-explore-traffic-trafficlocation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficLocation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="traffic/TrafficLocation-class.html#constructors">Constructors</a></li>
<li><a href="traffic/TrafficLocation/TrafficLocation.html">TrafficLocation</a></li>
<li class="section-title">
<a href="traffic/TrafficLocation-class.html#instance-properties">Properties</a>
</li>
<li><a href="traffic/TrafficLocation/additionalPolylines.html">additionalPolylines</a></li>
<li><a href="traffic/TrafficLocation/description.html">description</a></li>
<li><a href="traffic/TrafficLocation/hashCode.html">hashCode</a></li>
<li><a href="traffic/TrafficLocation/lengthInMeters.html">lengthInMeters</a></li>
<li><a href="traffic/TrafficLocation/polyline.html">polyline</a></li>
<li class="inherited"><a href="traffic/TrafficLocation/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="traffic/TrafficLocation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="traffic/TrafficLocation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="traffic/TrafficLocation/toString.html">toString</a></li>
<li class="section-title"><a href="traffic/TrafficLocation-class.html#operators">Operators</a></li>
<li><a href="traffic/TrafficLocation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li class="self-crumb">TrafficLocation class</li>
</ol>
<div class="self-name">TrafficLocation</div>
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
<div class="main-content" data-above-sidebar="traffic/traffic-library-sidebar.html" data-below-sidebar="traffic/TrafficLocation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficLocation class</h1></div>
<section class="desc markdown">
<p>The location reference to the traffic incident.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficLocation">
/sdk-for-flutter-explore-traffic-trafficlocation-trafficlocation(/sdk-for-flutter-explore-core-geopolyline-class polyline, List&lt;<wbr/>/sdk-for-flutter-explore-core-geopolyline-class&gt; additionalPolylines, int lengthInMeters)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="additionalPolylines">
/sdk-for-flutter-explore-traffic-trafficlocation-additionalpolylines
↔ List&lt;<wbr/>/sdk-for-flutter-explore-core-geopolyline-class&gt;
</dt>
<dd>
  List of polylines that were not included in continuous polyline.
Use this to fill any gaps in the continuous polyline.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="description">
/sdk-for-flutter-explore-traffic-trafficlocation-description
↔ String
</dt>
<dd>
  The description of the location.
In general, the language can't be bound to the description.
Usually, the language is one of the local languages of the incident region.
Note: A localizable description of the incident is part of /sdk-for-flutter-explore-traffic-trafficincidentbase-description.
This description describes only the location where the incident occurred.
Defaults to an empty string.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-explore-traffic-trafficlocation-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lengthInMeters">
/sdk-for-flutter-explore-traffic-trafficlocation-lengthinmeters
↔ int
</dt>
<dd>
  The affected road length in meters.
The length can be 0 only if the incident supplier has provided incomplete data.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="polyline">
/sdk-for-flutter-explore-traffic-trafficlocation-polyline
↔ /sdk-for-flutter-explore-core-geopolyline-class
</dt>
<dd>
  The polyline representing the traffic entity shape.
The current field contains a continuous polyline with no gaps between geo-coordinates.
All others following the gap are present in the <code>additional_polylines</code> field.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-explore-traffic-trafficlocation-runtimetype
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
/sdk-for-flutter-explore-traffic-trafficlocation-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-explore-traffic-trafficlocation-tostring(<wbr/>)
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
/sdk-for-flutter-explore-traffic-trafficlocation-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-explore-traffic-traffic-library</li>
<li class="self-crumb">TrafficLocation class</li>
</ol>
<h5>traffic library</h5>
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
