---
title: "TrafficMergeWarning class"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/TrafficMergeWarning-class.html#constructors">Constructors</a></li>
<li><a href="navigation/TrafficMergeWarning/TrafficMergeWarning.html">TrafficMergeWarning</a></li>
<li class="section-title">
<a href="navigation/TrafficMergeWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/TrafficMergeWarning/distanceToTrafficMergeInMeters.html">distanceToTrafficMergeInMeters</a></li>
<li><a href="navigation/TrafficMergeWarning/distanceType.html">distanceType</a></li>
<li><a href="navigation/TrafficMergeWarning/hashCode.html">hashCode</a></li>
<li><a href="navigation/TrafficMergeWarning/id.html">id</a></li>
<li><a href="navigation/TrafficMergeWarning/laneCount.html">laneCount</a></li>
<li><a href="navigation/TrafficMergeWarning/roadType.html">roadType</a></li>
<li class="inherited"><a href="navigation/TrafficMergeWarning/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/TrafficMergeWarning/side.html">side</a></li>
<li class="section-title inherited"><a href="navigation/TrafficMergeWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/TrafficMergeWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/TrafficMergeWarning/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/TrafficMergeWarning-class.html#operators">Operators</a></li>
<li><a href="navigation/TrafficMergeWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TrafficMergeWarning class</li>
</ol>
<div class="self-name">TrafficMergeWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrafficMergeWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrafficMergeWarning class</h1></div>
<section class="desc markdown">
<p>A class that provides warning for merging traffic.</p>
<p>The main field describing the merging traffic is <code>TrafficMergeWarning.road_type</code>
specifying the type of road containing traffic which is merging with the current road.
Use <code>TrafficMergeWarningListener</code> to get notifications about upcoming merging traffic.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrafficMergeWarning">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-trafficmergewarning(double distanceToTrafficMergeInMeters, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToTrafficMergeInMeters">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-distancetotrafficmergeinmeters
↔ double
</dt>
<dd>
  Distance to merging traffic in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new traffic merge location ahead or a warning for
passing a traffic merge location. Since the traffic merge warning is given relative to a single position on
the route, <code>DistanceType.REACHED</code> will never be given for this warning.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific traffic merge warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="laneCount">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-lanecount
↔ int
</dt>
<dd>
  Number of lanes of the merging road containing the traffic. If the road has no lanes defined, than the
number of lanes returned will be 1.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="roadType">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-roadtype
↔ /sdk-for-flutter-navigate-navigation-trafficmergeroadtype
</dt>
<dd>
  Type of road which contains the merging traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="side">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-side
↔ /sdk-for-flutter-navigate-navigation-trafficmergeside
</dt>
<dd>
  The side from which the traffic is merging.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-trafficmergewarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-trafficmergewarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TrafficMergeWarning class</li>
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
