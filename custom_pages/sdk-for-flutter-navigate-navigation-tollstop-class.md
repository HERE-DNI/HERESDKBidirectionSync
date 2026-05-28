---
title: "TollStop class"
slug: "sdk-for-flutter-navigate-navigation-tollstop-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollStop-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/TollStop-class.html#constructors">Constructors</a></li>
<li><a href="navigation/TollStop/TollStop.html">TollStop</a></li>
<li class="section-title">
<a href="navigation/TollStop-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/TollStop/distanceToTollStopInMeters.html">distanceToTollStopInMeters</a></li>
<li><a href="navigation/TollStop/distanceType.html">distanceType</a></li>
<li><a href="navigation/TollStop/hashCode.html">hashCode</a></li>
<li><a href="navigation/TollStop/id.html">id</a></li>
<li><a href="navigation/TollStop/lanes.html">lanes</a></li>
<li class="inherited"><a href="navigation/TollStop/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="navigation/TollStop-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/TollStop/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/TollStop/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/TollStop-class.html#operators">Operators</a></li>
<li><a href="navigation/TollStop/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TollStop class</li>
</ol>
<div class="self-name">TollStop</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TollStop-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TollStop class</h1></div>
<section class="desc markdown">
<p>A class that provides information for a toll stop with multiple toll booths.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TollStop">
/sdk-for-flutter-navigate-navigation-tollstop-tollstop(/sdk-for-flutter-navigate-navigation-distancetype distanceType, double distanceToTollStopInMeters, List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-tollboothlane-class&gt; lanes)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToTollStopInMeters">
/sdk-for-flutter-navigate-navigation-tollstop-distancetotollstopinmeters
↔ double
</dt>
<dd>
  Distance to the toll stop in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-tollstop-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  Indicates if the specified toll stop is ahead of the vehicle or has just passed by.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-tollstop-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-tollstop-id
↔ int
</dt>
<dd>
  Unique identifier for this specific toll stop warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="lanes">
/sdk-for-flutter-navigate-navigation-tollstop-lanes
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-tollboothlane-class&gt;
</dt>
<dd>
  Describes the features of the booth for the lane.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-tollstop-runtimetype
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
/sdk-for-flutter-navigate-navigation-tollstop-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-tollstop-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-tollstop-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TollStop class</li>
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
