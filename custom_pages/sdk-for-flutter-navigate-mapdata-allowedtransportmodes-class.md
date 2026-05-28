---
title: "AllowedTransportModes class"
slug: "sdk-for-flutter-navigate-mapdata-allowedtransportmodes-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AllowedTransportModes-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="mapdata/AllowedTransportModes-class.html#constructors">Constructors</a></li>
<li><a href="mapdata/AllowedTransportModes/AllowedTransportModes.html">AllowedTransportModes</a></li>
<li class="section-title">
<a href="mapdata/AllowedTransportModes-class.html#instance-properties">Properties</a>
</li>
<li><a href="mapdata/AllowedTransportModes/bicycleAllowed.html">bicycleAllowed</a></li>
<li><a href="mapdata/AllowedTransportModes/busAllowed.html">busAllowed</a></li>
<li><a href="mapdata/AllowedTransportModes/carAllowed.html">carAllowed</a></li>
<li><a href="mapdata/AllowedTransportModes/hashCode.html">hashCode</a></li>
<li><a href="mapdata/AllowedTransportModes/pedestrianAllowed.html">pedestrianAllowed</a></li>
<li class="inherited"><a href="mapdata/AllowedTransportModes/runtimeType.html">runtimeType</a></li>
<li><a href="mapdata/AllowedTransportModes/scooterAllowed.html">scooterAllowed</a></li>
<li><a href="mapdata/AllowedTransportModes/taxiAllowed.html">taxiAllowed</a></li>
<li><a href="mapdata/AllowedTransportModes/truckAllowed.html">truckAllowed</a></li>
<li class="section-title inherited"><a href="mapdata/AllowedTransportModes-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="mapdata/AllowedTransportModes/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="mapdata/AllowedTransportModes/toString.html">toString</a></li>
<li class="section-title"><a href="mapdata/AllowedTransportModes-class.html#operators">Operators</a></li>
<li><a href="mapdata/AllowedTransportModes/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li class="self-crumb">AllowedTransportModes class</li>
</ol>
<div class="self-name">AllowedTransportModes</div>
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
<div class="main-content" data-above-sidebar="mapdata/mapdata-library-sidebar.html" data-below-sidebar="mapdata/AllowedTransportModes-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AllowedTransportModes class</h1></div>
<section class="desc markdown">
<p>Specifies which transport modes are allowed in a particular direction.</p>
<p><strong>Note:</strong> This struct specifies a general restriction to that transport mode,
but additional restriction are possible.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="AllowedTransportModes">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-allowedtransportmodes()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bicycleAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-bicycleallowed
↔ bool
</dt>
<dd>
<code>True</code> if bicycles can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="busAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-busallowed
↔ bool
</dt>
<dd>
<code>True</code> if buses can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="carAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-carallowed
↔ bool
</dt>
<dd>
<code>True</code> if cars can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="pedestrianAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-pedestrianallowed
↔ bool
</dt>
<dd>
<code>True</code> if pedestrians can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="scooterAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-scooterallowed
↔ bool
</dt>
<dd>
<code>True</code> if scooters can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="taxiAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-taxiallowed
↔ bool
</dt>
<dd>
<code>True</code> if taxis can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="truckAllowed">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-truckallowed
↔ bool
</dt>
<dd>
<code>True</code> if trucks can access the segment in the given direction
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-mapdata-allowedtransportmodes-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">AllowedTransportModes class</li>
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
