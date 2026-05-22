---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonOptions-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonOptions class</li>
</ol>
<div class="self-name">ElectronicHorizonOptions</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonOptions class</h1></div>
<section class="desc markdown">
<p>Provides options to configure /sdk-for-flutter-navigate-electronic-horizon-electronichorizonengine-class.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonOptions">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-electronichorizonoptions(List&lt;<wbr/>double&gt; lookAheadDistancesInMeters, double trailingDistanceInMeters)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="lookAheadDistancesInMeters">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-lookaheaddistancesinmeters
↔ List&lt;<wbr/>double&gt;
</dt>
<dd>
  The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths.
The first entry of the list is for the most preferred path, the second is for the side paths of the first level,
the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided.
The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list.
If the list is empty, a single default distance value is used instead.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trailingDistanceInMeters">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-trailingdistanceinmeters
↔ double
</dt>
<dd>
  The trailing distance of the electronic horizon path in meters.
Segments are removed from the path once they are passed and the distance to them exceeds this value.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ElectronicHorizonOptions class</li>
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
