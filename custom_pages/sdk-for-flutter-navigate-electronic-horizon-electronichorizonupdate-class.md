---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonUpdate-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonUpdate class</li>
</ol>
<div class="self-name">ElectronicHorizonUpdate</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonUpdate-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonUpdate class</h1></div>
<section class="desc markdown">
<p>A class representing a full update delivered via /sdk-for-flutter-navigate-electronic-horizon-electronichorizonlistener-class notifications.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonUpdate">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-electronichorizonupdate(/sdk-for-flutter-navigate-electronic-horizon-electronichorizonposition-class position)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="electronicHorizon">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-electronichorizon
↔ /sdk-for-flutter-navigate-electronic-horizon-electronichorizon-class?
</dt>
<dd>
  The full electronic horizon recomputed for the current vehicle state.
May be <code>null</code> if there is no update.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="position">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-position
↔ /sdk-for-flutter-navigate-electronic-horizon-electronichorizonposition-class
</dt>
<dd>
  The vehicle’s updated position relative to the electronic horizon.
Always present. If no <code>electronic_horizon</code> is available, the position
refers to the most recently known horizon.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentChanges">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-segmentchanges
↔ /sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-class?
</dt>
<dd>
  The difference between the previously emitted horizon and the newly computed one.
Contains added and removed segments.
May be <code>null</code> if there is no update.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonupdate-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonUpdate class</li>
</ol>
<h5>electronic_horizon library</h5>
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
