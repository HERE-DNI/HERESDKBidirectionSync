---
title: "Untitled"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrackingCameraBehaviorManeuverModeConfiguration-class.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TrackingCameraBehaviorManeuverModeConfiguration class</li>
</ol>
<div class="self-name">TrackingCameraBehaviorManeuverModeConfiguration</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehaviorManeuverModeConfiguration-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrackingCameraBehaviorManeuverModeConfiguration class</h1></div>
<section class="desc markdown">
<p>Configuration that defines how /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class reacts to nearby maneuvers.</p>
<p>On each frame, and based on the current position, the availability of its functional road
class, and the availability of maneuver data for at least one adjacent maneuver, the camera
checks for a match against the /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules in the order they are listed. If a match is
found, subsequent rules are not checked. If no match is found, if inputs are unavailable,
or if the matched rule has <code>null</code> options, the camera does not react.</p>
<p>For correct default initialization, use /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrackingCameraBehaviorManeuverModeConfiguration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-trackingcamerabehaviormaneuvermodeconfiguration()
</dt>
<dd>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearingThresholdInDegrees">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-bearingthresholdindegrees
↔ double
</dt>
<dd>
  Maximum angle difference in degrees between the current bearing and the bearing to the
maneuver point. If the difference exceeds this threshold, the camera does not turn
towards the maneuver. Valid range is 0.0 to 180.0. Defaults to 25.0.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="maneuverRules">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules
↔ List&lt;<wbr/>/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class&gt;
</dt>
<dd>
  Ordered list of maneuver rules. Rules are evaluated in order; the first matching rule
determines the camera behavior. If empty, this configuration is not valid and the
camera does not react to maneuvers. If /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration is not used
for /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class, it will be an empty list.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-runtimetype
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
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">TrackingCameraBehaviorManeuverModeConfiguration class</li>
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



</div>
`
}</HTMLBlock>
