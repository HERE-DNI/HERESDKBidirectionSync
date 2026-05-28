---
title: "SpatialNotificationDetails class"
slug: "sdk-for-flutter-navigate-navigation-spatialnotificationdetails-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpatialNotificationDetails-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/SpatialNotificationDetails-class.html#constructors">Constructors</a></li>
<li><a href="navigation/SpatialNotificationDetails/SpatialNotificationDetails.html">SpatialNotificationDetails</a></li>
<li class="section-title">
<a href="navigation/SpatialNotificationDetails-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/SpatialNotificationDetails/audioCuePanning.html">audioCuePanning</a></li>
<li><a href="navigation/SpatialNotificationDetails/estimatedAudioCueDuration.html">estimatedAudioCueDuration</a></li>
<li><a href="navigation/SpatialNotificationDetails/hashCode.html">hashCode</a></li>
<li><a href="navigation/SpatialNotificationDetails/initialAzimuthInDegrees.html">initialAzimuthInDegrees</a></li>
<li class="inherited"><a href="navigation/SpatialNotificationDetails/runtimeType.html">runtimeType</a></li>
<li class="section-title inherited"><a href="navigation/SpatialNotificationDetails-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/SpatialNotificationDetails/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/SpatialNotificationDetails/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/SpatialNotificationDetails-class.html#operators">Operators</a></li>
<li><a href="navigation/SpatialNotificationDetails/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">SpatialNotificationDetails class</li>
</ol>
<div class="self-name">SpatialNotificationDetails</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SpatialNotificationDetails-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>SpatialNotificationDetails class</h1></div>
<section class="desc markdown">
<p>This class provides all the information for a spatial text notification, including the
maneuver data and extra data which is required to set the direction of spatialization
of the audio cue.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="SpatialNotificationDetails">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-spatialnotificationdetails(double initialAzimuthInDegrees, /sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class audioCuePanning, Duration estimatedAudioCueDuration)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="audioCuePanning">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-audiocuepanning
↔ /sdk-for-flutter-navigate-navigation-spatialaudiocuepanning-class
</dt>
<dd>
  Object to start the angular panning when spatialization of the text notification is desired
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="estimatedAudioCueDuration">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-estimatedaudiocueduration
↔ Duration
</dt>
<dd>
  Estimation of the required time to play an audio cue at speech rate 1.0.
For example the cue "Turn right on Name-Of-A-Street" will playback over an X number of milliseconds.
Therefore, an estimation of this audio cue duration is needed to correctly sync the movement
of sound to the cue (so that audio movement and audio duration match).
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="initialAzimuthInDegrees">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees
↔ double
</dt>
<dd>
  Initial desired angular position of the upcoming audio cue. For example, for a maneuver such as
"Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc trajectory
from the front to the right, mimicking the maneuver geometry.
In this case, it is good practice to start the trajectory from an initial azimuth that is located
slightly on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting to play
the audio cue to avoid unwanted audio "jumps".
The orientation in space for /sdk-for-flutter-navigate-navigation-spatialnotificationdetails-initialazimuthindegrees can be represented by the
following angular values:
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-runtimetype
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
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-spatialnotificationdetails-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">SpatialNotificationDetails class</li>
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
