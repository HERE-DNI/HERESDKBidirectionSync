---
title: "TrackingCameraBehavior class abstract"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrackingCameraBehavior-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/TrackingCameraBehavior-class.html#constructors">Constructors</a></li>
<li><a href="navigation/TrackingCameraBehavior/TrackingCameraBehavior.html">TrackingCameraBehavior</a></li>
<li class="section-title">
<a href="navigation/TrackingCameraBehavior-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/TrackingCameraBehavior/bearingInDegrees.html">bearingInDegrees</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/hashCode.html">hashCode</a></li>
<li><a href="navigation/TrackingCameraBehavior/isManeuverDetectionEnabled.html">isManeuverDetectionEnabled</a></li>
<li><a href="navigation/TrackingCameraBehavior/maxRotationSpeedInDegreesPerSecond.html">maxRotationSpeedInDegreesPerSecond</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/normalizedPrincipalPoint.html">normalizedPrincipalPoint</a></li>
<li><a href="navigation/TrackingCameraBehavior/principalPointAnimationDuration.html">principalPointAnimationDuration</a></li>
<li><a href="navigation/TrackingCameraBehavior/recenterAnimationDuration.html">recenterAnimationDuration</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/TrackingCameraBehavior/tiltInDegrees.html">tiltInDegrees</a></li>
<li><a href="navigation/TrackingCameraBehavior/viewRectangle.html">viewRectangle</a></li>
<li><a href="navigation/TrackingCameraBehavior/zoomPolicy.html">zoomPolicy</a></li>
<li><a href="navigation/TrackingCameraBehavior/zoomSpeedInLevelsPerSecond.html">zoomSpeedInLevelsPerSecond</a></li>
<li class="section-title"><a href="navigation/TrackingCameraBehavior-class.html#instance-methods">Methods</a></li>
<li><a href="navigation/TrackingCameraBehavior/flagFixedDurationForNextAnimation.html">flagFixedDurationForNextAnimation</a></li>
<li><a href="navigation/TrackingCameraBehavior/getManeuverModeConfiguration.html">getManeuverModeConfiguration</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/TrackingCameraBehavior/setManeuverModeConfiguration.html">setManeuverModeConfiguration</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/TrackingCameraBehavior-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/operator_equals.html">operator ==</a></li>
<li class="section-title"><a href="navigation/TrackingCameraBehavior-class.html#static-methods">Static methods</a></li>
<li><a href="navigation/TrackingCameraBehavior/defaultFunctionalRoadClassZoomPolicyOptions.html">defaultFunctionalRoadClassZoomPolicyOptions</a></li>
<li><a href="navigation/TrackingCameraBehavior/defaultManeuverModeConfiguration.html">defaultManeuverModeConfiguration</a></li>
<li><a href="navigation/TrackingCameraBehavior/defaultSpeedBasedZoomPolicyOptions.html">defaultSpeedBasedZoomPolicyOptions</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">TrackingCameraBehavior class</li>
</ol>
<div class="self-name">TrackingCameraBehavior</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehavior-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>TrackingCameraBehavior class abstract</h1></div>
<section class="desc markdown">
<p>Use this class to follow a moving target.</p>
<p>The camera smoothly tracks the target’s
position while adjusting heading, tilt, and zoom as needed. When tracking starts
or resumes, the camera first animates a re-centering transition to align with the target.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are
subject to change without a deprecation process.</p>
</section>
<section>
<dl class="dl-horizontal">
<dt>Implemented types</dt>
<dd>
<ul class="comma-separated clazz-relationships">
<li>/sdk-for-flutter-navigate-navigation-camerabehavior-class</li>
</ul>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="TrackingCameraBehavior">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-trackingcamerabehavior()
</dt>
<dd>
          Creates a new instance of this class.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="bearingInDegrees">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-bearingindegrees
↔ double?
</dt>
<dd>
  The camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in "north up" mode.
Defaults to <code>null</code>, which means the camera derives the bearing from the /sdk-for-flutter-navigate-core-location-class,
so that it points to the direction of travel.
If this property is <code>null</code> and the device does not provide bearing, the last known value is
used or zero otherwise.
Gets the bearing in degrees.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="hashCode">
/sdk-for-flutter-navigate-navigation-camerabehavior-hashcode
→ int
</dt>
<dd class="inherited">
  The hash code for this object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="isManeuverDetectionEnabled">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-ismaneuverdetectionenabled
↔ bool
</dt>
<dd>
  Whether maneuver detection is enabled.
When <code>true</code>, the camera detects adjacent maneuvers and reacts according to
the /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class set via /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration.
A valid /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class must be set for the camera to react. Defaults to <code>false</code>.
Gets whether maneuver detection is enabled.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="maxRotationSpeedInDegreesPerSecond">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-maxrotationspeedindegreespersecond
↔ double
</dt>
<dd>
  The maximum rotation speed.
Maximum bearing rotation speed in degrees per second,
limiting how fast the camera turns.
Defaults to 20 degrees per second.
Gets the maximum rotation speed.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="normalizedPrincipalPoint">
/sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint
↔ /sdk-for-flutter-navigate-core-anchor2d-class
</dt>
<dd class="inherited">
  The normalized principal point.
Normalized principal point to be used during navigation.
Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
of the mapview.
Gets the currently set normalized principal point to be used during navigation.
  <div class="features">getter/setter pairinherited</div>
</dd>
<dt class="property" id="principalPointAnimationDuration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-principalpointanimationduration
↔ Duration
</dt>
<dd>
  The duration of principal point animation in milliseconds.
If the principal point is changed, the change will be animated
over this duration.
Defaults to 500 milliseconds, or half a second.
Gets the current principal point animation duration in milliseconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="recenterAnimationDuration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-recenteranimationduration
↔ Duration
</dt>
<dd>
  The duration of recenter animation in milliseconds.
Time to recenter the camera reaching current car position.
Defaults to 500 milliseconds, or half a second.
Gets the recenter animation duration in milliseconds.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="tiltInDegrees">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-tiltindegrees
↔ double
</dt>
<dd>
  The value of camera tilt in degrees.
Camera tilt angle relative to the ground plane, in degrees.
Defaults to 50.
Gets the camera tilt in degrees.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="viewRectangle">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-viewrectangle
↔ /sdk-for-flutter-navigate-core-rectangle2d-class?
</dt>
<dd>
  The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates.
Defaults to <code>null</code>. If not set, it uses the viewport bounds of the underlying map view.
Gets the current view rectangle, if it's set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoomPolicy">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-zoompolicy
↔ /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorzoompolicy-class
</dt>
<dd>
  The strategy of computing the zoom level.
Defines the strategy used to compute the zoom level based on scene heuristics.
Defaults to a fixed zoom policy at zoom level 16.5.
Gets the current zoom computation strategy.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="zoomSpeedInLevelsPerSecond">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-zoomspeedinlevelspersecond
↔ double
</dt>
<dd>
  The zoom level transition speed.
Speed factor controlling how quickly the camera
transitions between zoom levels
Defaults to 0.5 zoom levels per second.
Gets the zoom level transition speed.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable" id="flagFixedDurationForNextAnimation">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-flagfixeddurationfornextanimation(<wbr/>)
    → void

</dt>
<dd>
  Enables fixed-duration animation mode for the next property change.
  

</dd>
<dt class="callable" id="getManeuverModeConfiguration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-getmaneuvermodeconfiguration(<wbr/>)
    → /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class?

</dt>
<dd>
  Gets the current maneuver mode configuration, or <code>null</code> if not set.
  

</dd>
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setManeuverModeConfiguration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration(<wbr/>/sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class? maneuverModeConfiguration)
    → void

</dt>
<dd>
  Sets the configuration for camera behavior near maneuvers.
  

</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-camerabehavior-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-camerabehavior-operator-equals(<wbr/>Object other)
    → bool

</dt>
<dd class="inherited">
  The equality operator.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="static-methods">
<h2>Static Methods</h2>
<dl class="callables">
<dt class="callable" id="defaultFunctionalRoadClassZoomPolicyOptions">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultfunctionalroadclasszoompolicyoptions(<wbr/>)
    → /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class

</dt>
<dd>
  Returns /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class. The default /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class.
  

</dd>
<dt class="callable" id="defaultManeuverModeConfiguration">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration(<wbr/>)
    → /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class

</dt>
<dd>
  Returns /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class. The default /sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class.
  

</dd>
<dt class="callable" id="defaultSpeedBasedZoomPolicyOptions">
/sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultspeedbasedzoompolicyoptions(<wbr/>)
    → /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class

</dt>
<dd>
  Returns /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class. The default /sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class.
  

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
<li class="self-crumb">TrackingCameraBehavior class</li>
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
