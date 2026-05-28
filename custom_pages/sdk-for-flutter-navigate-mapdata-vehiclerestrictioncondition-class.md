---
title: "VehicleRestrictionCondition class"
slug: "sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleRestrictionCondition-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/VehicleRestrictionCondition-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/VehicleRestrictionCondition/VehicleRestrictionCondition.html">VehicleRestrictionCondition</a></li>
<li class="section-title">
<a href="mapdata/VehicleRestrictionCondition-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/VehicleRestrictionCondition/appliesDuring.html">appliesDuring</a></li>
<li><a href="mapdata/VehicleRestrictionCondition/hashCode.html">hashCode</a></li>
<li><a href="mapdata/VehicleRestrictionCondition/requiredRoadProfile.html">requiredRoadProfile</a></li>
<li><a href="mapdata/VehicleRestrictionCondition/requiredVehicleProfile.html">requiredVehicleProfile</a></li>
<li><a href="mapdata/VehicleRestrictionCondition/requiredWeatherCondition.html">requiredWeatherCondition</a></li>
<li class="inherited"><a href="mapdata/VehicleRestrictionCondition/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="mapdata/VehicleRestrictionCondition-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/VehicleRestrictionCondition/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/VehicleRestrictionCondition/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/VehicleRestrictionCondition-class.html#operators">Operators</a></li>
<li><a href="mapdata/VehicleRestrictionCondition/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">VehicleRestrictionCondition class</li>
</ol>
<div class="self-name">VehicleRestrictionCondition</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/VehicleRestrictionCondition-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VehicleRestrictionCondition class</h1></div>
<section class="desc markdown">
<p>Combined set of conditions that must all be satisfied for a regulation to apply.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VehicleRestrictionCondition">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-vehiclerestrictioncondition()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="appliesDuring">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-appliesduring
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-core-timerule-class&gt;
</dt>
<dd>
  Time rules during which this restriction is active.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="requiredRoadProfile">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-requiredroadprofile
↔ /sdk-for-flutter-navigate-mapdata-roadprofilecondition-class?
</dt>
<dd>
  Road profile conditions that activate this restriction.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="requiredVehicleProfile">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-requiredvehicleprofile
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-vehicleprofilerestriction-class&gt;
</dt>
<dd>
  Vehicle profile that is subject to this restriction.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="requiredWeatherCondition">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-requiredweathercondition
↔ /sdk-for-flutter-navigate-navigation-weathertype?
</dt>
<dd>
  Weather condition that must be present for this restriction to apply.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-runtimetype
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
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">VehicleRestrictionCondition class</li>
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
