---
title: "LaneAccess class"
slug: "sdk-for-flutter-navigate-navigation-laneaccess-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LaneAccess-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/LaneAccess-class.html#constructors">Constructors</a></li>
<li><a href="navigation/LaneAccess/LaneAccess.html">LaneAccess</a></li>
<li class="section-title">
<a href="navigation/LaneAccess-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/LaneAccess/automobiles.html">automobiles</a></li>
<li><a href="navigation/LaneAccess/buses.html">buses</a></li>
<li><a href="navigation/LaneAccess/carpools.html">carpools</a></li>
<li><a href="navigation/LaneAccess/deliveryVehicles.html">deliveryVehicles</a></li>
<li><a href="navigation/LaneAccess/emergencyVehicles.html">emergencyVehicles</a></li>
<li><a href="navigation/LaneAccess/hashCode.html">hashCode</a></li>
<li><a href="navigation/LaneAccess/motorcycles.html">motorcycles</a></li>
<li><a href="navigation/LaneAccess/pedestrians.html">pedestrians</a></li>
<li class="inherited"><a href="navigation/LaneAccess/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/LaneAccess/taxis.html">taxis</a></li>
<li><a href="navigation/LaneAccess/throughTraffic.html">throughTraffic</a></li>
<li><a href="navigation/LaneAccess/trucks.html">trucks</a></li>
<li class="section-title inherited"><a href="navigation/LaneAccess-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/LaneAccess/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/LaneAccess/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/LaneAccess-class.html#operators">Operators</a></li>
<li><a href="navigation/LaneAccess/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">LaneAccess class</li>
</ol>
<div class="self-name">LaneAccess</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LaneAccess-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LaneAccess class</h1></div>
<section class="desc markdown">
<p>A class which identifies the vehicle type(s) allowed to
access a lane.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LaneAccess">
/sdk-for-flutter-navigate-navigation-laneaccess-laneaccess(bool automobiles, bool buses, bool taxis, bool carpools, bool pedestrians, bool trucks, bool throughTraffic, bool deliveryVehicles, bool emergencyVehicles, bool motorcycles)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="automobiles">
/sdk-for-flutter-navigate-navigation-laneaccess-automobiles
↔ bool
</dt>
<dd>
  Four-wheel vehicles that are allowed according to national/local vehicle regulations to drive
on motorways, ranging from sub-compact cars to full-size vans and light road vehicles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="buses">
/sdk-for-flutter-navigate-navigation-laneaccess-buses
↔ bool
</dt>
<dd>
  Buses that are used for public transportation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="carpools">
/sdk-for-flutter-navigate-navigation-laneaccess-carpools
↔ bool
</dt>
<dd>
  Represents the sharing of car journeys so that more than one person travels in a car, and
prevents the need for others to have to drive to a location themselves.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="deliveryVehicles">
/sdk-for-flutter-navigate-navigation-laneaccess-deliveryvehicles
↔ bool
</dt>
<dd>
  Delivery /sdk-for-flutter-navigate-navigation-laneaccess-trucks that are permitted to enter the city proper
to unload goods at businesses.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="emergencyVehicles">
/sdk-for-flutter-navigate-navigation-laneaccess-emergencyvehicles
↔ bool
</dt>
<dd>
  Any vehicle that is designated and authorized to respond to an emergency in a
life-threatening situation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-laneaccess-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="motorcycles">
/sdk-for-flutter-navigate-navigation-laneaccess-motorcycles
↔ bool
</dt>
<dd>
  Motorized two-wheeled passenger vehicles. Generally, mopeds are considered
motorcycles.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pedestrians">
/sdk-for-flutter-navigate-navigation-laneaccess-pedestrians
↔ bool
</dt>
<dd>
  Persons traveling on foot, whether walking or running.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-laneaccess-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="taxis">
/sdk-for-flutter-navigate-navigation-laneaccess-taxis
↔ bool
</dt>
<dd>
  Four-wheel vehicles that are usually fitted with a taximeter, that may be hired,
along with their driver, to carry passengers to any specified destination.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="throughTraffic">
/sdk-for-flutter-navigate-navigation-laneaccess-throughtraffic
↔ bool
</dt>
<dd>
  Passenger vehicles (i.e., those defined as passenger car/automobiles) that are
allowed to access roads that have traffic restrictions.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trucks">
/sdk-for-flutter-navigate-navigation-laneaccess-trucks
↔ bool
</dt>
<dd>
  Large vehicles that range from medium to heavy duty trucks.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-laneaccess-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-laneaccess-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-laneaccess-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">LaneAccess class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
