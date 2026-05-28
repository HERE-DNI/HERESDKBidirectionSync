---
title: "RailwayCrossingWarning class"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RailwayCrossingWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/RailwayCrossingWarning-class.html#constructors">Constructors</a></li>
<li><a href="navigation/RailwayCrossingWarning/RailwayCrossingWarning.html">RailwayCrossingWarning</a></li>
<li class="section-title">
<a href="navigation/RailwayCrossingWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/RailwayCrossingWarning/distanceToRailwayCrossingInMeters.html">distanceToRailwayCrossingInMeters</a></li>
<li><a href="navigation/RailwayCrossingWarning/distanceType.html">distanceType</a></li>
<li><a href="navigation/RailwayCrossingWarning/hashCode.html">hashCode</a></li>
<li><a href="navigation/RailwayCrossingWarning/id.html">id</a></li>
<li class="inherited"><a href="navigation/RailwayCrossingWarning/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/RailwayCrossingWarning/segmentReference.html">segmentReference</a></li>
<li><a href="navigation/RailwayCrossingWarning/type.html">type</a></li>
<li class="section-title inherited"><a href="navigation/RailwayCrossingWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/RailwayCrossingWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/RailwayCrossingWarning/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/RailwayCrossingWarning-class.html#operators">Operators</a></li>
<li><a href="navigation/RailwayCrossingWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">RailwayCrossingWarning class</li>
</ol>
<div class="self-name">RailwayCrossingWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RailwayCrossingWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RailwayCrossingWarning class</h1></div>
<section class="desc markdown">
<p>A class that provides railway crossing.</p>
<p>The main field describing the railway crossing is <code>RailwayCrossingWarning.type</code> specifying
whether the railway crossing is protected by a barrier or not.
Use <code>RailwayCrossingWarningListener</code> to get notifications about upcoming railway crossings.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RailwayCrossingWarning">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-railwaycrossingwarning(double distanceToRailwayCrossingInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType, /sdk-for-flutter-navigate-routing-segmentreference-class segmentReference)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToRailwayCrossingInMeters">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-distancetorailwaycrossinginmeters
↔ double
</dt>
<dd>
  Distance to the railway crossing in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new railway crossing ahead or a warning
for passing a railway crossing.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific railway crossing warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="segmentReference">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-segmentreference
↔ /sdk-for-flutter-navigate-routing-segmentreference-class
</dt>
<dd>
  The reference to the segment where the railway crossing is located. It can be used to identify the
location.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-type
↔ /sdk-for-flutter-navigate-routing-routerailwaycrossingtype
</dt>
<dd>
  Type of railway crossing, specifying whether it is protected by a barrier or not.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-railwaycrossingwarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">RailwayCrossingWarning class</li>
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
</div></div>
</div>
`
}</HTMLBlock>
