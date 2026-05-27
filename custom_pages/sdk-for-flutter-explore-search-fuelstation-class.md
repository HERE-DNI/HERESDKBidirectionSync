---
title: "Constructors"
slug: "sdk-for-flutter-explore-search-fuelstation-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- FuelStation-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="search/FuelStation-class.html#constructors">Constructors</a></li>
<li><a href="search/FuelStation/FuelStation.html">FuelStation</a></li>
<li class="section-title">
<a href="search/FuelStation-class.html#instance-properties">Properties</a>
</li>
<li><a href="search/FuelStation/fuels.html">fuels</a></li>
<li><a href="search/FuelStation/hashCode.html">hashCode</a></li>
<li><a href="search/FuelStation/highVolumePumps.html">highVolumePumps</a></li>
<li><a href="search/FuelStation/payAtThePump.html">payAtThePump</a></li>
<li class="inherited"><a href="search/FuelStation/runtimeType.html">runtimeType</a></li>
<li><a href="search/FuelStation/truckFuels.html">truckFuels</a></li>
<li class="section-title inherited"><a href="search/FuelStation-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="search/FuelStation/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="search/FuelStation/toString.html">toString</a></li>
<li class="section-title"><a href="search/FuelStation-class.html#operators">Operators</a></li>
<li><a href="search/FuelStation/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">FuelStation class</li>
</ol>
<div class="self-name">FuelStation</div>
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
<div class="main-content" data-above-sidebar="search/search-library-sidebar.html" data-below-sidebar="search/FuelStation-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>FuelStation class</h1></div>
<section class="desc markdown">
<p>Contains information about a specific fuel station.</p>
<p>Use <a href="../search/PlaceCategory/businessAndServicesPetrolGasolineStation.html">/sdk-for-flutter-explore-search-placecategory-businessandservicespetrolgasolinestation</a> to find fuel stations.
In the <code>Details</code> of a <code>Place</code> result you can find the associated fuel station information,
if any.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="FuelStation">
<a href="../search/FuelStation/FuelStation.html">/sdk-for-flutter-explore-search-fuelstation-fuelstation</a>()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="fuels">
<a href="../search/FuelStation/fuels.html">/sdk-for-flutter-explore-search-fuelstation-fuels</a>
↔ List&lt;<wbr/><a href="../search/GenericFuel-class.html">/sdk-for-flutter-explore-search-genericfuel-class</a>&gt;
</dt>
<dd>
  The list of car fuel types associated with the fuel station.
The list can be empty when no generic fuels are offered or when the information is unknown.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../search/FuelStation/hashCode.html">/sdk-for-flutter-explore-search-fuelstation-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="highVolumePumps">
<a href="../search/FuelStation/highVolumePumps.html">/sdk-for-flutter-explore-search-fuelstation-highvolumepumps</a>
↔ bool?
</dt>
<dd>
  Indicates if high volume pumps are available or not. <code>null</code> means information is unknown.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="payAtThePump">
<a href="../search/FuelStation/payAtThePump.html">/sdk-for-flutter-explore-search-fuelstation-payatthepump</a>
↔ bool?
</dt>
<dd>
  Indicates if paying at the pump is supported or not. <code>null</code> means information is unknown.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../search/FuelStation/runtimeType.html">/sdk-for-flutter-explore-search-fuelstation-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="truckFuels">
<a href="../search/FuelStation/truckFuels.html">/sdk-for-flutter-explore-search-fuelstation-truckfuels</a>
↔ List&lt;<wbr/><a href="../search/TruckFuel-class.html">/sdk-for-flutter-explore-search-truckfuel-class</a>&gt;
</dt>
<dd>
  The list of truck fuel types associated with the fuel station.
The list can be empty when no truck fuels are offered or when the information is unknown.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../search/FuelStation/noSuchMethod.html">/sdk-for-flutter-explore-search-fuelstation-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../search/FuelStation/toString.html">/sdk-for-flutter-explore-search-fuelstation-tostring</a>(<wbr/>)
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
<a href="../search/FuelStation/operator_equals.html">/sdk-for-flutter-explore-search-fuelstation-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../search/search-library.html">/sdk-for-flutter-explore-search-search-library</a></li>
<li class="self-crumb">FuelStation class</li>
</ol>
<h5>search library</h5>
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
</HTMLBlock>
