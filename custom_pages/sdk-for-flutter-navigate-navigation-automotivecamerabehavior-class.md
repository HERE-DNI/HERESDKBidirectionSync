---
title: "AutomotiveCameraBehavior class abstract"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AutomotiveCameraBehavior-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/AutomotiveCameraBehavior-class.html#constructors">Constructors</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/AutomotiveCameraBehavior.html">AutomotiveCameraBehavior</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/AutomotiveCameraBehavior.fromJson.html">fromJson</a></li>
<li class="section-title">
<a href="navigation/AutomotiveCameraBehavior-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/AutomotiveCameraBehavior/activeCameraType.html">activeCameraType</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/hashCode.html">hashCode</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/isManeuverDetectionEnabled.html">isManeuverDetectionEnabled</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/normalizedPrincipalPoint.html">normalizedPrincipalPoint</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/orientationMode.html">orientationMode</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/viewRectangle.html">viewRectangle</a></li>
<li class="section-title"><a href="navigation/AutomotiveCameraBehavior-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/noSuchMethod.html">noSuchMethod</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/setAreaCameraBehaviorGeobox.html">setAreaCameraBehaviorGeobox</a></li>
<li><a href="navigation/AutomotiveCameraBehavior/setAreaCameraBehaviorVisiblePoints.html">setAreaCameraBehaviorVisiblePoints</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/toString.html">toString</a></li>
<li class="section-title inherited"><a href="navigation/AutomotiveCameraBehavior-class.html#operators">Operators</a></li>
<li class="inherited"><a href="navigation/CameraBehavior/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">AutomotiveCameraBehavior class</li>
</ol>
<div class="self-name">AutomotiveCameraBehavior</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>AutomotiveCameraBehavior class abstract</h1></div>
<section class="desc markdown">
<p>Provides a high-level camera controller for automotive navigation that manages both tracking
and area camera behaviors.</p>
<p>This class acts as a facade, delegating camera operations to either
a /sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class for following the vehicle during navigation or an /sdk-for-flutter-navigate-navigation-areacamerabehavior-class
for showing overview areas such as points of interest or route previews.</p>
<p>The controller supports three states: tracking mode (following the vehicle), area mode (showing
geographic regions), or inactive (no automatic camera control). The inactive state allows
external control of the camera, such as when responding to user touch events or when UI logic
temporarily disables automatic camera behavior.</p>
<p>Camera configuration, including animation durations, zoom policies, and maneuver handling
settings, can be provided through a JSON configuration string or file. The configuration is
validated and parsed during construction.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
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
<dt class="callable" id="AutomotiveCameraBehavior">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior()
</dt>
<dd>
          Creates a new instance of this class with default camera behaviors and configuration.
            <div class="constructor-modifier features">factory</div>
</dd>
<dt class="callable" id="AutomotiveCameraBehavior.fromJson">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior-fromjson(String configJson)
</dt>
<dd>
          Creates a new instance of this class configured from a JSON string.
            <div class="constructor-modifier features">factory</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="activeCameraType">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype
↔ /sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype
</dt>
<dd>
  The active camera type.
Defines which camera behavior is currently active:
/sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype (free navigation), /sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype,
or /sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype.
Gets the type of camera currently handling camera updates.
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
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-ismaneuverdetectionenabled
↔ bool
</dt>
<dd>
  Enables or disables automatic camera adjustments during upcoming maneuvers.
When enabled, the tracking camera automatically adjusts zoom and framing to provide
better visibility of upcoming turns and maneuvers during navigation. The specific
adjustments and their timing are defined in the camera configuration.
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
<dt class="property" id="orientationMode">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-orientationmode
↔ /sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode
</dt>
<dd>
  The current orientation mode of the camera.
Defines the camera's viewing angle and orientation for tracking mode.
In /sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode, the camera looks straight down and rotates with the vehicle heading.
In /sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode, the camera is tilted for a perspective view.
In /sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode, the camera maintains north-up orientation regardless of vehicle heading.
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
<dt class="property" id="viewRectangle">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-viewrectangle
↔ /sdk-for-flutter-navigate-core-rectangle2d-class?
</dt>
<dd>
  The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates. This property is forwarded to both the tracking and area cameras,
ensuring consistent viewport constraints across all camera modes.
If not set, it uses the viewport bounds of the underlying map view.
Gets the current view rectangle, if it's set.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable" id="setAreaCameraBehaviorGeobox">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox(<wbr/>/sdk-for-flutter-navigate-core-geobox-class geobox)
    → void

</dt>
<dd>
  Configures the Area camera to frame the specified geographic bounding box.
  

</dd>
<dt class="callable" id="setAreaCameraBehaviorVisiblePoints">
/sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints(<wbr/>List&lt;<wbr/>/sdk-for-flutter-navigate-core-geocoordinates-class&gt; points, bool includeCurrentPosition)
    → void

</dt>
<dd>
  Configures the Area camera to frame the specified points.
  

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
<li class="self-crumb">AutomotiveCameraBehavior class</li>
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
