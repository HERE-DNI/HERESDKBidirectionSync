---
title: "TrackingCameraBehaviorManeuverRuleOptions class"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrackingCameraBehaviorManeuverRuleOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions-class.html#constructors">Constructors</a></li>
<li><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/TrackingCameraBehaviorManeuverRuleOptions.html">TrackingCameraBehaviorManeuverRuleOptions</a></li>
<li class="section-title">
<a href="navigation/TrackingCameraBehaviorManeuverRuleOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/earlyPreManeuverActivationThresholdInMeters.html">earlyPreManeuverActivationThresholdInMeters</a></li>
<li class="inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/hashCode.html">hashCode</a></li>
<li><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/postManeuverActivationThresholdInMeters.html">postManeuverActivationThresholdInMeters</a></li>
<li><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/preManeuverActivationThresholdInMeters.html">preManeuverActivationThresholdInMeters</a></li>
<li class="inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/zoomRange.html">zoomRange</a></li>
<li class="section-title inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/TrackingCameraBehaviorManeuverRuleOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TrackingCameraBehaviorManeuverRuleOptions class</li>
</ol>
<div class="self-name">TrackingCameraBehaviorManeuverRuleOptions</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehaviorManeuverRuleOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrackingCameraBehaviorManeuverRuleOptions class</h1></div>
<section class="desc markdown">
<p>Defines a set of configurations specific to a /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrackingCameraBehaviorManeuverRuleOptions">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-trackingcamerabehaviormaneuverruleoptions()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="earlyPreManeuverActivationThresholdInMeters">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-earlypremaneuveractivationthresholdinmeters
↔ double
</dt>
<dd>
  Distance in meters for early activation. If the current position enters this threshold
of the upcoming maneuver while still within /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-postmaneuveractivationthresholdinmeters
of the previous maneuver, the camera behaves as though it were already in the upcoming
maneuver's pre-activation zone. Must be non-negative. Defaults to 0.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="postManeuverActivationThresholdInMeters">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-postmaneuveractivationthresholdinmeters
↔ double
</dt>
<dd>
  Distance in meters after the previous maneuver point within which this rule remains
active. Must be non-negative. Defaults to 0.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="preManeuverActivationThresholdInMeters">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-premaneuveractivationthresholdinmeters
↔ double
</dt>
<dd>
  Distance in meters before the next maneuver point within which this rule becomes active.
Must be non-negative. Defaults to 0.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="zoomRange">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-zoomrange
↔ /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverzoomrange-class
</dt>
<dd>
  The zoom range for this rule. Defines the minimum and maximum zoom levels.
Defaults to a default-constructed /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverzoomrange-class.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-tostring(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable inherited" id="operator ==">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
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
<li class="self-crumb">TrackingCameraBehaviorManeuverRuleOptions class</li>
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
