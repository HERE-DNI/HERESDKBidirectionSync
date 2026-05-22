---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-roadattributes-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadAttributes-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RoadAttributes class</li>
</ol>
<div class="self-name">RoadAttributes</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RoadAttributes-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RoadAttributes class</h1></div>
<section class="desc markdown">
<p>Road attributes, including usage and physical characteristics.</p>
<p>Note that a road can have more than one attribute at the same time.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RoadAttributes">
/sdk-for-flutter-navigate-navigation-roadattributes-roadattributes()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-roadattributes-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isBridge">
/sdk-for-flutter-navigate-navigation-roadattributes-isbridge
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
<dt class="property" id="isBuiltUpArea">
/sdk-for-flutter-navigate-navigation-roadattributes-isbuiltuparea
↔ bool
</dt>
<dd>
  Indicates if the navigable segment is a built up area.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isControlledAccess">
/sdk-for-flutter-navigate-navigation-roadattributes-iscontrolledaccess
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
<dt class="property" id="isDirtRoad">
/sdk-for-flutter-navigate-navigation-roadattributes-isdirtroad
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
<dt class="property" id="isDividedRoad">
/sdk-for-flutter-navigate-navigation-roadattributes-isdividedroad
↔ bool
</dt>
<dd>
  Indicates if there is a physical structure or painted road marking intended to legally
prohibit left turns in right-side driving countries, right turns in left-side driving
countries, and U-turns at divided intersections or in the middle of divided segments.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isNoThrough">
/sdk-for-flutter-navigate-navigation-roadattributes-isnothrough
↔ bool
</dt>
<dd>
  Identifies a no through road. This can also be a part of the route you can only enter or leave if it’s a waypoint.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isPrivate">
/sdk-for-flutter-navigate-navigation-roadattributes-isprivate
↔ bool
</dt>
<dd>
  Private identifies roads that are not maintained by an organization
responsible for maintenance of public roads.
Allows for unique cartographic representation of roads that restrict public use.
May be used to avoid routing through a private road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRamp">
/sdk-for-flutter-navigate-navigation-roadattributes-isramp
↔ bool
</dt>
<dd>
  Range is a ramp: connects roads that do not intersect at grade.
Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”)
and for route guidance when determining if sign text should be used.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRightDrivingSide">
/sdk-for-flutter-navigate-navigation-roadattributes-isrightdrivingside
↔ bool
</dt>
<dd>
  Indicates if vehicles have to drive on the right-hand side of the road or the left-hand side.
For example, in New York it is always <code>true</code> and in London always <code>false</code> as the United Kingdom is
a left-hand driving country.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isRoundabout">
/sdk-for-flutter-navigate-navigation-roadattributes-isroundabout
↔ bool
</dt>
<dd>
  Indicates the presence of a roundabout.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTollway">
/sdk-for-flutter-navigate-navigation-roadattributes-istollway
↔ bool
</dt>
<dd>
  Identifies a road for which a fee must be paid to use the road.
Tollway may be used for map display (e.g., different rendering of toll roads) and routing.
Tollway is flagged on roads that require a fee for traversal.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="isTunnel">
/sdk-for-flutter-navigate-navigation-roadattributes-istunnel
↔ bool
</dt>
<dd>
  Identifies an enclosed (on all sides) passageway through or under an obstruction.
This attribute can be used for display or route guidance.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-roadattributes-runtimetype
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
/sdk-for-flutter-navigate-navigation-roadattributes-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-roadattributes-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-roadattributes-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RoadAttributes class</li>
</ol>
<h5>navigation library</h5>
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
