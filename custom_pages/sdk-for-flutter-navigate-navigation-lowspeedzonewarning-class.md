---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LowSpeedZoneWarning-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">LowSpeedZoneWarning class</li>
</ol>
<div class="self-name">LowSpeedZoneWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LowSpeedZoneWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>LowSpeedZoneWarning class</h1></div>
<section class="desc markdown">
<p>A class that provides low speed zone.</p>
<p>The main field describing the low speed zone is <code>LowSpeedZoneWarning.speed_limit_in_meters_per_second</code>
specifying the speed limit of the low speed zone.
Use <code>LowSpeedZoneWarningListener</code> to get notifications about upcoming low speed zones.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="LowSpeedZoneWarning">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-lowspeedzonewarning(double distanceToLowSpeedZoneInMeters, double speedLimitInMetersPerSecond, /sdk-for-flutter-navigate-navigation-distancetype distanceType, /sdk-for-flutter-navigate-routing-segmentreference-class segmentReference)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToLowSpeedZoneInMeters">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-distancetolowspeedzoneinmeters
↔ double
</dt>
<dd>
  Distance to the low speed warning in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new low speed zone ahead or a warning
for passing a low speed zone.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific low speed zone warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentReference">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-segmentreference
↔ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  The reference to the segment where the low speed zone is located. It can be used to identify the
location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-speedlimitinmeterspersecond
↔ double
</dt>
<dd>
  Speed limit of the low speed zone.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-lowspeedzonewarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">LowSpeedZoneWarning class</li>
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
