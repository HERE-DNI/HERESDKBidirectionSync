---
title: "ElectronicHorizonSegmentChanges class"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonSegmentChanges-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonSegmentChanges-class.html#constructors">Constructors</a></li>
<li><a href="electronic_horizon/ElectronicHorizonSegmentChanges/ElectronicHorizonSegmentChanges.html">ElectronicHorizonSegmentChanges</a></li>
<li class="section-title">
<a href="electronic_horizon/ElectronicHorizonSegmentChanges-class.html#instance-properties">Properties</a>
</li>
<li><a href="electronic_horizon/ElectronicHorizonSegmentChanges/added.html">added</a></li>
<li><a href="electronic_horizon/ElectronicHorizonSegmentChanges/hashCode.html">hashCode</a></li>
<li><a href="electronic_horizon/ElectronicHorizonSegmentChanges/removedIds.html">removedIds</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonSegmentChanges/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="electronic_horizon/ElectronicHorizonSegmentChanges-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonSegmentChanges/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="electronic_horizon/ElectronicHorizonSegmentChanges/toString.html">toString</a></li>
<li class="section-title"><a href="electronic_horizon/ElectronicHorizonSegmentChanges-class.html#operators">Operators</a></li>
<li><a href="electronic_horizon/ElectronicHorizonSegmentChanges/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonSegmentChanges class</li>
</ol>
<div class="self-name">ElectronicHorizonSegmentChanges</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonSegmentChanges-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonSegmentChanges class</h1></div>
<section class="desc markdown">
<p>A class describing the set of changes in horizon segments
between two consecutive updates.</p>
<p>Includes lists of both newly added and removed segments.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonSegmentChanges">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-electronichorizonsegmentchanges()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="added">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-added
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegment-class&gt;
</dt>
<dd>
  A list of segments that were added since the previous update.
May be empty if no segments were added.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="removedIds">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-removedids
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentid-class&gt;
</dt>
<dd>
  Identifiers of segments that were removed since the previous update.
May be empty if no segments were removed.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-runtimetype
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegmentchanges-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ElectronicHorizonSegmentChanges class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
