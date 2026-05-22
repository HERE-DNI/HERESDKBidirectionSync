---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-bordercrossingwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BorderCrossingWarning-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">BorderCrossingWarning class</li>
</ol>
<div class="self-name">BorderCrossingWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/BorderCrossingWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>BorderCrossingWarning class</h1></div>
<section class="desc markdown">
<p>A border crossing.</p>
<p>The main field describing the border crossing is <code>BorderCrossingWarning.type</code> specifying whether the border crossing
is given for a country border or a state border. The <code>BorderCrossingWarning.type</code> must be known.
The country and state codes are contained in <code>BorderCrossingWarning.administrativeRules</code> along with other information such as speed
limits, u-turn regulations or pre-trip planning information contained by the /sdk-for-flutter-navigate-mapdata-administrativerules-class.</p>
<p>Use <code>BorderCrossingWarningListener</code> to get notifications about upcoming country or state border crossings.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="BorderCrossingWarning">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-bordercrossingwarning(double distanceToBorderCrossingInMeters, /sdk-for-flutter-navigate-navigation-bordercrossingtype type, /sdk-for-flutter-navigate-mapdata-administrativerules-class administrativeRules, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="administrativeRules">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-administrativerules
↔ /sdk-for-flutter-navigate-mapdata-administrativerules-class
</dt>
<dd>
  The administrative rules for the country or state after the border crossing. It contains information regarding
rules such as driving side, speed limits, various sticker requirements, toll costs and others.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="commercialVehicleRegulations">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-commercialvehicleregulations
↔ /sdk-for-flutter-navigate-mapdata-administrativecommercialvehiclerules-class?
</dt>
<dd>
  Commercial vehicle regulations for the administrative region after the border crossing.
Contains access restrictions, speed limits, and drive/rest rules applicable to commercial vehicles.
This field is only populated when crossing into a region with specific commercial vehicle regulations.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceToBorderCrossingInMeters">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetobordercrossinginmeters
↔ double
</dt>
<dd>
  Distance to the border crossing in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new border crossing ahead or a warning for
passing a border crossing. Since the border crossing warning is given relative to a single position on
the route, /sdk-for-flutter-navigate-navigation-distancetype will never be given for this warning.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific border crossing warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-type
↔ /sdk-for-flutter-navigate-navigation-bordercrossingtype
</dt>
<dd>
  Type of border crossing.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-bordercrossingwarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">BorderCrossingWarning class</li>
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
