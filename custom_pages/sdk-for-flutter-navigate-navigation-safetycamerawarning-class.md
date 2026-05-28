---
title: "SafetyCameraWarning class"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SafetyCameraWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/SafetyCameraWarning-class.html#constructors">Constructors</a></li>
<li><a href="navigation/SafetyCameraWarning/SafetyCameraWarning.html">SafetyCameraWarning</a></li>
<li class="section-title">
<a href="navigation/SafetyCameraWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/SafetyCameraWarning/distanceToCameraInMeters.html">distanceToCameraInMeters</a></li>
<li><a href="navigation/SafetyCameraWarning/distanceType.html">distanceType</a></li>
<li><a href="navigation/SafetyCameraWarning/hashCode.html">hashCode</a></li>
<li><a href="navigation/SafetyCameraWarning/id.html">id</a></li>
<li class="inherited"><a href="navigation/SafetyCameraWarning/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/SafetyCameraWarning/speedLimitInMetersPerSecond.html">speedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SafetyCameraWarning/type.html">type</a></li>
<li class="section-title inherited"><a href="navigation/SafetyCameraWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/SafetyCameraWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/SafetyCameraWarning/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/SafetyCameraWarning-class.html#operators">Operators</a></li>
<li><a href="navigation/SafetyCameraWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SafetyCameraWarning class</li>
</ol>
<div class="self-name">SafetyCameraWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SafetyCameraWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SafetyCameraWarning class</h1></div>
<section class="desc markdown">
<p>A class that provides safety camera warning information.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SafetyCameraWarning">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-safetycamerawarning(double distanceToCameraInMeters, double speedLimitInMetersPerSecond, /sdk-for-flutter-navigate-navigation-safetycameratype type, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToCameraInMeters">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-distancetocamerainmeters
↔ double
</dt>
<dd>
  Distance to the safety camera in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type of the warning (e.g.: warning for a new safety camera ahead, warning for
passing a safety camera). Since the safety camera warning is given relative to a single
position on the route, /sdk-for-flutter-navigate-navigation-distancetype will never be given for this warning.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific safety camera warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-speedlimitinmeterspersecond
↔ double
</dt>
<dd>
  The speed limit observed by the safety camera.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="type">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-type
↔ /sdk-for-flutter-navigate-navigation-safetycameratype
</dt>
<dd>
  The type of the safety camera element.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-safetycamerawarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-safetycamerawarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">SafetyCameraWarning class</li>
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
