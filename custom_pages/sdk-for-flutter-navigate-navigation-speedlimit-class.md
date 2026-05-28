---
title: "SpeedLimit class"
slug: "sdk-for-flutter-navigate-navigation-speedlimit-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedLimit-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/SpeedLimit-class.html#constructors">Constructors</a></li>
<li><a href="navigation/SpeedLimit/SpeedLimit.html">SpeedLimit</a></li>
<li class="section-title">
<a href="navigation/SpeedLimit-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/SpeedLimit/advisorySpeedLimitInMetersPerSecond.html">advisorySpeedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SpeedLimit/fogSpeedLimitInMetersPerSecond.html">fogSpeedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SpeedLimit/hashCode.html">hashCode</a></li>
<li><a href="navigation/SpeedLimit/optimalWeatherSpeedLimitInMetersPerSecond.html">optimalWeatherSpeedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SpeedLimit/rainSpeedLimitInMetersPerSecond.html">rainSpeedLimitInMetersPerSecond</a></li>
<li class="inherited"><a href="navigation/SpeedLimit/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/SpeedLimit/schoolZoneSpeedLimitInMetersPerSecond.html">schoolZoneSpeedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SpeedLimit/snowSpeedLimitInMetersPerSecond.html">snowSpeedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SpeedLimit/speedLimitInMetersPerSecond.html">speedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SpeedLimit/timeDependentSpeedLimitInMetersPerSecond.html">timeDependentSpeedLimitInMetersPerSecond</a></li>
<li class="section-title"><a href="navigation/SpeedLimit-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/SpeedLimit/effectiveSpeedLimitInMetersPerSecond.html">effectiveSpeedLimitInMetersPerSecond</a></li>
<li class="inherited"><a href="navigation/SpeedLimit/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/SpeedLimit/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/SpeedLimit-class.html#operators">Operators</a></li>
<li><a href="navigation/SpeedLimit/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SpeedLimit class</li>
</ol>
<div class="self-name">SpeedLimit</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SpeedLimit-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SpeedLimit class</h1></div>
<section class="desc markdown">
<p>Represents the speed limit of the current road.</p>
<p>Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits,
the HERE SDK internally reads the current device time and notifies only on speed limits
that are currently active.</p>
<p>It is recommended to use /sdk-for-flutter-navigate-navigation-speedlimit-effectivespeedlimitinmeterspersecond when
an application does not offer dedicated speed limit indicators for other cases, such as
weather-dependent speed limits.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SpeedLimit">
/sdk-for-flutter-navigate-navigation-speedlimit-speedlimit()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="advisorySpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-advisoryspeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A recommended speed limit that may not be indicated on the local road signs,
but that serves to warn a driver that the road conditions may indicate a lower speed.
Typically, the road condition is a curved road or a ramp but it may be due to a narrow road,
narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a
different road than the one for which it applies (this can happen with ramps). In this case,
the advisory speed is indicated for the road for which it is intended, even if the sign is
further than 50 meters from the particular road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="fogSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-fogspeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when the visibility decreases due to fog.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-speedlimit-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="optimalWeatherSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-optimalweatherspeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when the visibility is optimal due to weather
conditions.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="rainSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-rainspeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when it is raining or there is water on the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-speedlimit-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="schoolZoneSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-schoolzonespeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A conditional speed limit as indicated on the local road signs.
School zone signs are often placed to slow drivers before reaching an intersection where
children are crossing.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="snowSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-snowspeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A conditional speed limit as indicated on the local road signs.
The road speed limit that is in effect only when there is snow on the road.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-speedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  Regular speed limit if available. In case of unbounded speed limit, the value is zero.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="timeDependentSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-timedependentspeedlimitinmeterspersecond
↔ double?
</dt>
<dd>
  A conditional speed limit as indicated on the local road signs.
Speed limit that is in effect considering the current local time provided by the device's
clock.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="effectiveSpeedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-speedlimit-effectivespeedlimitinmeterspersecond(<wbr/>)
    → double?

</dt>
<dd>
  Returns the effective (lowest) speed limit between /sdk-for-flutter-navigate-navigation-speedlimit-speedlimitinmeterspersecond,
/sdk-for-flutter-navigate-navigation-speedlimit-schoolzonespeedlimitinmeterspersecond, /sdk-for-flutter-navigate-navigation-speedlimit-timedependentspeedlimitinmeterspersecond
and /sdk-for-flutter-navigate-navigation-speedlimit-optimalweatherspeedlimitinmeterspersecond.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-speedlimit-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-speedlimit-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-speedlimit-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">SpeedLimit class</li>
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
