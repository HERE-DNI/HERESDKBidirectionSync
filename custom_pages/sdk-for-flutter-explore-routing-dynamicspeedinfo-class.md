---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-dynamicspeedinfo-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- DynamicSpeedInfo-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/DynamicSpeedInfo-class.html#constructors">Constructors</a></li>
<li><a href="routing/DynamicSpeedInfo/DynamicSpeedInfo.html">DynamicSpeedInfo</a></li>
<li class="section-title">
<a href="routing/DynamicSpeedInfo-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/DynamicSpeedInfo/baseSpeedInMetersPerSecond.html">baseSpeedInMetersPerSecond</a></li>
<li><a href="routing/DynamicSpeedInfo/hashCode.html">hashCode</a></li>
<li class="inherited"><a href="routing/DynamicSpeedInfo/runtimeType.html">runtimeType</a></li>
<li><a href="routing/DynamicSpeedInfo/trafficSpeedInMetersPerSecond.html">trafficSpeedInMetersPerSecond</a></li>
<li><a href="routing/DynamicSpeedInfo/turnTimeInSeconds.html">turnTimeInSeconds</a></li>
<li class="section-title"><a href="routing/DynamicSpeedInfo-class.html#instance-methods">Methods</a></li>
<li><a href="routing/DynamicSpeedInfo/calculateJamFactor.html">calculateJamFactor</a></li>
<li class="inherited"><a href="routing/DynamicSpeedInfo/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/DynamicSpeedInfo/toString.html">toString</a></li>
<li class="section-title"><a href="routing/DynamicSpeedInfo-class.html#operators">Operators</a></li>
<li><a href="routing/DynamicSpeedInfo/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">DynamicSpeedInfo class</li>
</ol>
<div class="self-name">DynamicSpeedInfo</div>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/DynamicSpeedInfo-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DynamicSpeedInfo class</h1></div>
<section class="desc markdown">
<p>Provides estimated speed information.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DynamicSpeedInfo">
<a href="../routing/DynamicSpeedInfo/DynamicSpeedInfo.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-dynamicspeedinfo</a>(double baseSpeedInMetersPerSecond, double trafficSpeedInMetersPerSecond, int turnTimeInSeconds)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="baseSpeedInMetersPerSecond">
<a href="../routing/DynamicSpeedInfo/baseSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-basespeedinmeterspersecond</a>
↔ double
</dt>
<dd>
  The speed in meters per second without taking traffic into consideration.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/DynamicSpeedInfo/hashCode.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/DynamicSpeedInfo/runtimeType.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="trafficSpeedInMetersPerSecond">
<a href="../routing/DynamicSpeedInfo/trafficSpeedInMetersPerSecond.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-trafficspeedinmeterspersecond</a>
↔ double
</dt>
<dd>
  The speed in meters per second considering traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="turnTimeInSeconds">
<a href="../routing/DynamicSpeedInfo/turnTimeInSeconds.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-turntimeinseconds</a>
↔ int
</dt>
<dd>
  The time it takes to make a turn, represented in seconds.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="calculateJamFactor">
<a href="../routing/DynamicSpeedInfo/calculateJamFactor.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-calculatejamfactor</a>(<wbr/>)
    → double

</dt>
<dd>
  Calculates the traffic jam factor that shows the traffic condition in a numeric way.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/DynamicSpeedInfo/noSuchMethod.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/DynamicSpeedInfo/toString.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-tostring</a>(<wbr/>)
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
<a href="../routing/DynamicSpeedInfo/operator_equals.html">/sdk-for-flutter-explore-routing-dynamicspeedinfo-operator-equals</a>(<wbr/>Object other)
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
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">DynamicSpeedInfo class</li>
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
</HTMLBlock>
