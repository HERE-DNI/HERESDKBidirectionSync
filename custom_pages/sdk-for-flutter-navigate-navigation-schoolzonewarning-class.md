---
title: "SchoolZoneWarning class"
slug: "sdk-for-flutter-navigate-navigation-schoolzonewarning-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SchoolZoneWarning-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/SchoolZoneWarning-class.html#constructors">Constructors</a></li>
<li><a href="navigation/SchoolZoneWarning/SchoolZoneWarning.html">SchoolZoneWarning</a></li>
<li class="section-title">
<a href="navigation/SchoolZoneWarning-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/SchoolZoneWarning/distanceToSchoolZoneInMeters.html">distanceToSchoolZoneInMeters</a></li>
<li><a href="navigation/SchoolZoneWarning/distanceType.html">distanceType</a></li>
<li><a href="navigation/SchoolZoneWarning/hashCode.html">hashCode</a></li>
<li><a href="navigation/SchoolZoneWarning/id.html">id</a></li>
<li class="inherited"><a href="navigation/SchoolZoneWarning/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/SchoolZoneWarning/speedLimitInMetersPerSecond.html">speedLimitInMetersPerSecond</a></li>
<li><a href="navigation/SchoolZoneWarning/timeRule.html">timeRule</a></li>
<li class="section-title inherited"><a href="navigation/SchoolZoneWarning-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/SchoolZoneWarning/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/SchoolZoneWarning/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/SchoolZoneWarning-class.html#operators">Operators</a></li>
<li><a href="navigation/SchoolZoneWarning/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SchoolZoneWarning class</li>
</ol>
<div class="self-name">SchoolZoneWarning</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SchoolZoneWarning-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SchoolZoneWarning class</h1></div>
<section class="desc markdown">
<p>A school zone warning which notifies about a school zone presence on road with a speed limit
different than the default speed limit applicable for cars.</p>
<p>Use <code>SchoolZoneWarningListener</code> to get notifications about school zones.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SchoolZoneWarning">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-schoolzonewarning(double distanceToSchoolZoneInMeters, double speedLimitInMetersPerSecond, /sdk-for-flutter-navigate-navigation-distancetype distanceType)
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="distanceToSchoolZoneInMeters">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-distancetoschoolzoneinmeters
↔ double
</dt>
<dd>
  The distance from the current location to the school zone in meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="distanceType">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-distancetype
↔ /sdk-for-flutter-navigate-navigation-distancetype
</dt>
<dd>
  The distance type for the warning, e.g. a warning for a new school zone ahead or a warning
for passing a school zone.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="id">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-id
↔ int
</dt>
<dd>
  Unique identifier for this specific school zone warning instance.
Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace.
Use this ID to track, update, or dismiss individual warning instances of this type.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="speedLimitInMetersPerSecond">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-speedlimitinmeterspersecond
↔ double
</dt>
<dd>
  Speed limit meters/second, which applies to current school zone.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="timeRule">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-timerule
↔ /sdk-for-flutter-navigate-core-timerule-class?
</dt>
<dd>
  Time rule indicating the time periods for which the warning applies.
If the field is 'null' then the warning is applicable at anytime.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-schoolzonewarning-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-schoolzonewarning-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">SchoolZoneWarning class</li>
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
