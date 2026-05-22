---
title: "Untitled"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonPath-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li class="self-crumb">ElectronicHorizonPath class</li>
</ol>
<div class="self-name">ElectronicHorizonPath</div>
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
<div class="main-content" data-above-sidebar="electronic_horizon/electronic_horizon-library-sidebar.html" data-below-sidebar="electronic_horizon/ElectronicHorizonPath-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>ElectronicHorizonPath class</h1></div>
<section class="desc markdown">
<p>Represents a single electronic horizon path.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="ElectronicHorizonPath">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-electronichorizonpath(List&lt;<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegment-class&gt; segments, double probability, int level)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="level">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-level
↔ int
</dt>
<dd>
  The level of this path. A value of 0 represents the most-preferred path.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="parentPathIndex">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-parentpathindex
↔ int?
</dt>
<dd>
  The index of the parent path. Index 0 marks the most-preferred path.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="parentSegmentIndex">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-parentsegmentindex
↔ int?
</dt>
<dd>
  The index of the parent segment in the parent path.
This value is <code>null</code> if the path is the most-preferred path.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="probability">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-probability
↔ double
</dt>
<dd>
  The probability of this electronic horizon path, where a value of 1 represents the most-preferred path and a value of 0 represents an unlikely path.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segments">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-segments
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-electronic-horizon-electronichorizonsegment-class&gt;
</dt>
<dd>
  The ordered list of segments in this path.
The list can be empty when no segments are available for the current path.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">ElectronicHorizonPath class</li>
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
