---
title: "VehicleSpecificSpeedLimit class"
slug: "sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VehicleSpecificSpeedLimit-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/VehicleSpecificSpeedLimit-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/VehicleSpecificSpeedLimit.html">VehicleSpecificSpeedLimit</a></li>
<li class="section-title">
<a href="mapdata/VehicleSpecificSpeedLimit-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/builtUpAreaMaxOverrideSpeedInMetersPerSecond.html">builtUpAreaMaxOverrideSpeedInMetersPerSecond</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/condition.html">condition</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/hashCode.html">hashCode</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/isAdvisory.html">isAdvisory</a></li>
<li class="inherited"><a href="mapdata/VehicleSpecificSpeedLimit/runtimeType.html">runtimeType</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/speedLimitInMetersPerSecond.html">speedLimitInMetersPerSecond</a></li>
<li class="section-title inherited"><a href="mapdata/VehicleSpecificSpeedLimit-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/VehicleSpecificSpeedLimit/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/VehicleSpecificSpeedLimit/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/VehicleSpecificSpeedLimit-class.html#operators">Operators</a></li>
<li><a href="mapdata/VehicleSpecificSpeedLimit/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">VehicleSpecificSpeedLimit class</li>
</ol>
<div class="self-name">VehicleSpecificSpeedLimit</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/VehicleSpecificSpeedLimit-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>VehicleSpecificSpeedLimit class</h1></div>
<section class="desc markdown">
<p>Speed limit regulation specific to a vehicle type.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="VehicleSpecificSpeedLimit">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-vehiclespecificspeedlimit(double speedLimitInMetersPerSecond, bool isAdvisory, /sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-class condition)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="builtUpAreaMaxOverrideSpeedInMetersPerSecond">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-builtupareamaxoverridespeedinmeterspersecond
↔ double?
</dt>
<dd>
  Max Override Speed indicates the maximum speed a commercial vehicle may travel within a BUA.
Could be 0 if unlimited.
A <code>null</code> value means the speed limit is not affected by the BUA override or not present.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="condition">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-condition
↔ /sdk-for-flutter-navigate-mapdata-vehiclerestrictioncondition-class
</dt>
<dd>
  Conditions under which this speed limit is active.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="isAdvisory">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-isadvisory
↔ bool
</dt>
<dd>
  If true, this speed limit is advisory rather than legally enforced.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-speedlimitinmeterspersecond
↔ double
</dt>
<dd>
  Maximum permitted speed in meters per second.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-vehiclespecificspeedlimit-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">VehicleSpecificSpeedLimit class</li>
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
