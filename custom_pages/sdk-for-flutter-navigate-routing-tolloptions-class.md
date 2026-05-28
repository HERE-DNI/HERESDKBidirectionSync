---
title: "TollOptions class"
slug: "sdk-for-flutter-navigate-routing-tolloptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/TollOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/TollOptions/TollOptions.html">TollOptions</a></li>
<li class="section-title">
<a href="routing/TollOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/TollOptions/co2Class.html">co2Class</a></li>
<li><a href="routing/TollOptions/emissionType.html">emissionType</a></li>
<li><a href="routing/TollOptions/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/TollOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/TollOptions/transponders.html">transponders</a></li>
<li><a href="routing/TollOptions/vehicleCategory.html">vehicleCategory</a></li>
<li class="section-title inherited"><a href="routing/TollOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/TollOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/TollOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/TollOptions-class.html#operators">Operators</a></li>
<li><a href="routing/TollOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">TollOptions class</li>
</ol>
<div class="self-name">TollOptions</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/TollOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TollOptions class</h1></div>
<section class="desc markdown">
<p>The option to specify how the tolls should be calculated.</p>
<p><strong>Note</strong>
Not used for offline calculations.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TollOptions">
/sdk-for-flutter-navigate-routing-tolloptions-tolloptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="co2Class">
/sdk-for-flutter-navigate-routing-tolloptions-co2class
↔ int?
</dt>
<dd>
  Defines the CO2 class of the vehicle as defined by the toll operator.
CO2 class is used with <code>emissionType</code>.
Allowed values for CO2 class are 1, 2, 3, 4, or 5, where a lower value generally indicates lower CO2 emissions.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="emissionType">
/sdk-for-flutter-navigate-routing-tolloptions-emissiontype
↔ /sdk-for-flutter-navigate-routing-tolloptionsemissiontype?
</dt>
<dd>
  Defines the emission type as defined by the toll operator for toll calculation based on vehicle emissions class.
The emission type is based on the European emission standards (Euro 1 to Euro 6, and Euro EEV).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-tolloptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-tolloptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="transponders">
/sdk-for-flutter-navigate-routing-tolloptions-transponders
↔ List&lt;<wbr/>String&gt;
</dt>
<dd>
  Specifies the toll collection systems for which the user has valid transponders.
Note: currently, the only valid value is "all". This means the user has a transponder that is accepted by all toll systems.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="vehicleCategory">
/sdk-for-flutter-navigate-routing-tolloptions-vehiclecategory
↔ /sdk-for-flutter-navigate-routing-tolloptionsvehiclecategory?
</dt>
<dd>
  Defines special vehicle category for toll calculation. Usual types like car or truck
are determined from transport mode.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-tolloptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-tolloptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-tolloptions-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li class="self-crumb">TollOptions class</li>
</ol>
<h5>routing library</h5>
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
