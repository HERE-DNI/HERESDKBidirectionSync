---
title: "WarningNotificationDistances class"
slug: "sdk-for-flutter-navigate-navigation-warningnotificationdistances-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningNotificationDistances-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/WarningNotificationDistances-class.html#constructors">Constructors</a></li>
<li><a href="navigation/WarningNotificationDistances/WarningNotificationDistances.html">WarningNotificationDistances</a></li>
<li class="section-title">
<a href="navigation/WarningNotificationDistances-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/WarningNotificationDistances/fastSpeedDistanceInMeters.html">fastSpeedDistanceInMeters</a></li>
<li><a href="navigation/WarningNotificationDistances/hashCode.html">hashCode</a></li>
<li><a href="navigation/WarningNotificationDistances/regularSpeedDistanceInMeters.html">regularSpeedDistanceInMeters</a></li>
<li class="inherited"><a href="navigation/WarningNotificationDistances/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/WarningNotificationDistances/slowSpeedDistanceInMeters.html">slowSpeedDistanceInMeters</a></li>
<li class="section-title inherited"><a href="navigation/WarningNotificationDistances-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/WarningNotificationDistances/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/WarningNotificationDistances/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/WarningNotificationDistances-class.html#operators">Operators</a></li>
<li><a href="navigation/WarningNotificationDistances/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">WarningNotificationDistances class</li>
</ol>
<div class="self-name">WarningNotificationDistances</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/WarningNotificationDistances-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>WarningNotificationDistances class</h1></div>
<section class="desc markdown">
<p>Distances for emitting warnings according to the timing profile.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="WarningNotificationDistances">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-warningnotificationdistances()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="fastSpeedDistanceInMeters">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-fastspeeddistanceinmeters
↔ int
</dt>
<dd>
  The distance in meters for emitting warnings when the speed limit or current speed is fast.
The conditions for a speed to be considered fast are the same ones as for <code>TimingProfile.FAST_SPEED</code>.
The distance should be greater than 0.
Defaults to 1500 meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="regularSpeedDistanceInMeters">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-regularspeeddistanceinmeters
↔ int
</dt>
<dd>
  The distance in meters for emitting warnings when the speed limit or current speed is regular.
The conditions for a speed to be considered regular are the same ones as for <code>TimingProfile.REGULAR_SPEED</code>.
The distance should be greater than 0.
Defaults to 750 meters.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="slowSpeedDistanceInMeters">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-slowspeeddistanceinmeters
↔ int
</dt>
<dd>
  The distance in meters for emitting warnings when the speed limit or current speed is slow.
The conditions for a speed to be considered slow are the same ones as for <code>TimingProfile.SLOW_SPEED</code>.
The distance should be greater than 0.
Defaults to 500 meters.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-warningnotificationdistances-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">WarningNotificationDistances class</li>
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
