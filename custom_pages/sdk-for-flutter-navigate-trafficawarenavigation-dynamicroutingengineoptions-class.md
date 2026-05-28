---
title: "DynamicRoutingEngineOptions class"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DynamicRoutingEngineOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="trafficawarenavigation/DynamicRoutingEngineOptions-class.html#constructors">Constructors</a></li>
<li><a href="trafficawarenavigation/DynamicRoutingEngineOptions/DynamicRoutingEngineOptions.html">DynamicRoutingEngineOptions</a></li>
<li class="section-title">
<a href="trafficawarenavigation/DynamicRoutingEngineOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="trafficawarenavigation/DynamicRoutingEngineOptions/hashCode.html">hashCode</a></li>
<li><a href="trafficawarenavigation/DynamicRoutingEngineOptions/minTimeDifference.html">minTimeDifference</a></li>
<li><a href="trafficawarenavigation/DynamicRoutingEngineOptions/minTimeDifferencePercentage.html">minTimeDifferencePercentage</a></li>
<li><a href="trafficawarenavigation/DynamicRoutingEngineOptions/pollInterval.html">pollInterval</a></li>
<li class="inherited"><a href="trafficawarenavigation/DynamicRoutingEngineOptions/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="trafficawarenavigation/DynamicRoutingEngineOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="trafficawarenavigation/DynamicRoutingEngineOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="trafficawarenavigation/DynamicRoutingEngineOptions/toString.html">toString</a></li>
<li class="section-title"><a href="trafficawarenavigation/DynamicRoutingEngineOptions-class.html#operators">Operators</a></li>
<li><a href="trafficawarenavigation/DynamicRoutingEngineOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li class="self-crumb">DynamicRoutingEngineOptions class</li>
</ol>
<div class="self-name">DynamicRoutingEngineOptions</div>
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
<div class="main-content" data-above-sidebar="trafficawarenavigation/trafficawarenavigation-library-sidebar.html" data-below-sidebar="trafficawarenavigation/DynamicRoutingEngineOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>DynamicRoutingEngineOptions class</h1></div>
<section class="desc markdown">
<p>Options defining the behavior of the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class.</p>
<p>Both, <code>minTimeDifference</code> and <code>minTimeDifferencePercentage</code>, will be checked:
When the poll interval is reached, the smaller difference will win and
the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class is notified.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="DynamicRoutingEngineOptions">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-dynamicroutingengineoptions()
</dt>
<dd>
          Creates an instance of this class.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="minTimeDifference">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference
↔ Duration?
</dt>
<dd>
  The minimum time difference, before notifying the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class.
To get notified, the following check must be true:
oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival &gt; /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifference.
A value of 0 will be treated as <code>null</code> meaning no event will be sent.
In order to receive events the difference needs to be greater than 0.
Defaults to <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="minTimeDifferencePercentage">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifferencepercentage
↔ double?
</dt>
<dd>
  The value is in the range of [0, 1] over the remaining (current position to next waypoint)
To get notified, the following check must be true:
oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival &gt;= newRouteDuration * <code>min_time_difference_percentage</code>.
A value of 0 will be treated as <code>null</code> meaning no event will be sent.
In order to receive events the difference needs to be greater than 0.
Defaults to <code>null</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="pollInterval">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-pollinterval
↔ Duration
</dt>
<dd>
  The poll interval.
Zero duration triggers a route calculation with each position update.
Triggered via /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-updatecurrentlocation
Defaults to 15 minutes.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-runtimetype
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
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li class="self-crumb">DynamicRoutingEngineOptions class</li>
</ol>
<h5>trafficawarenavigation library</h5>
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
