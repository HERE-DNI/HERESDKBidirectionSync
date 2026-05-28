---
title: "RoadUsages class"
slug: "sdk-for-flutter-navigate-mapdata-roadusages-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadUsages-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/RoadUsages-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/RoadUsages/RoadUsages.html">RoadUsages</a></li>
<li class="section-title">
<a href="mapdata/RoadUsages-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/RoadUsages/hashCode.html">hashCode</a></li>
<li><a href="mapdata/RoadUsages/isControlledAccess.html">isControlledAccess</a></li>
<li><a href="mapdata/RoadUsages/isPriorityRoad.html">isPriorityRoad</a></li>
<li><a href="mapdata/RoadUsages/isRamp.html">isRamp</a></li>
<li><a href="mapdata/RoadUsages/isTollway.html">isTollway</a></li>
<li class="inherited"><a href="mapdata/RoadUsages/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapdata/RoadUsages-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/RoadUsages/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/RoadUsages/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/RoadUsages-class.html#operators">Operators</a></li>
<li><a href="mapdata/RoadUsages/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">RoadUsages class</li>
</ol>
<div class="self-name">RoadUsages</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/RoadUsages-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoadUsages class</h1></div>
<section class="desc markdown">
<p>Road Usages of the segment.</p>
<p><em><strong>Note</strong></em> a road can have more than one attribute at the same time.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoadUsages">
/sdk-for-flutter-navigate-mapdata-roadusages-roadusages()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-roadusages-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isControlledAccess">
/sdk-for-flutter-navigate-mapdata-roadusages-iscontrolledaccess
↔ bool
</dt>
<dd>
  Controlled access roads are roads with limited entrances and exits
that allow uninterrupted high-speed traffic flow.
For example, the Interstate/Freeway network in the United States or
the Motorway network in Europe.
Controlled Access can be used for map display, avoidance of freeway/motorway,
publishing speed limits, and route guidance timing.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isPriorityRoad">
/sdk-for-flutter-navigate-mapdata-roadusages-ispriorityroad
↔ bool
</dt>
<dd>
  Indicates road stretches that have signs indicating priority on the road.
On these roads all traffic has priority over the traffic on the incoming roads.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRamp">
/sdk-for-flutter-navigate-mapdata-roadusages-isramp
↔ bool
</dt>
<dd>
  Range is a ramp: connects roads that do not intersect at grade.
Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”)
and for route guidance when determining if sign text should be used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTollway">
/sdk-for-flutter-navigate-mapdata-roadusages-istollway
↔ bool
</dt>
<dd>
  Identifies a road for which a fee must be paid to use the road.
Tollway may be used for map display (e.g., different rendering of toll roads) and routing.
Tollway is flagged on roads that require a fee for traversal.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-roadusages-runtimetype
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
/sdk-for-flutter-navigate-mapdata-roadusages-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-roadusages-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-roadusages-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RoadUsages class</li>
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
