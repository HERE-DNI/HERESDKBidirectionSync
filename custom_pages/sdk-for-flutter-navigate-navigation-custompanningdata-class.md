---
title: "CustomPanningData class"
slug: "sdk-for-flutter-navigate-navigation-custompanningdata-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CustomPanningData-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="navigation/CustomPanningData-class.html#constructors">Constructors</a></li>
<li><a href="navigation/CustomPanningData/CustomPanningData.html">CustomPanningData</a></li>
<li class="section-title">
<a href="navigation/CustomPanningData-class.html#instance-properties">Properties</a>
</li>
<li><a href="navigation/CustomPanningData/estimatedAudioCueDuration.html">estimatedAudioCueDuration</a></li>
<li><a href="navigation/CustomPanningData/hashCode.html">hashCode</a></li>
<li><a href="navigation/CustomPanningData/initialAzimuthInDegrees.html">initialAzimuthInDegrees</a></li>
<li class="inherited"><a href="navigation/CustomPanningData/runtimeType.html">runtimeType</a></li>
<li><a href="navigation/CustomPanningData/sweepAzimuthInDegrees.html">sweepAzimuthInDegrees</a></li>
<li class="section-title inherited"><a href="navigation/CustomPanningData-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="navigation/CustomPanningData/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="navigation/CustomPanningData/toString.html">toString</a></li>
<li class="section-title"><a href="navigation/CustomPanningData-class.html#operators">Operators</a></li>
<li><a href="navigation/CustomPanningData/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li class="self-crumb">CustomPanningData class</li>
</ol>
<div class="self-name">CustomPanningData</div>
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
<div class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/CustomPanningData-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>CustomPanningData class</h1></div>
<section class="desc markdown">
<p>This class contains all the information regarding the next angular panning element, including
a new estimated audio cue duration, and a new set of initial and sweep angular angle,
allowing the customization of the spatial audio trajectories for any type of notification,
such as speed or merge warners, maneuvers or even roundabouts notifications.</p>
<p>The orientation in space for /sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees and /sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees can
be represented by the following angular values:</p>
<table>
<thead>
<tr>
<th align="center">Front</th>
<th align="center">Right</th>
<th align="center">Rear</th>
<th align="center">Left</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">0°</td>
<td align="center">+90°</td>
<td align="center">+- 180</td>
<td align="center">-90°</td>
</tr>
</tbody>
</table>
<p>When any of the members of /sdk-for-flutter-navigate-navigation-custompanningdata-class are initialized as null, the default value
provided by HERE SDK will be used instead.
The audio cue is spatialized considering the action of both maneuvers, for example,
the audio cue 'Now turn right and then turn left' will be spatialized as following:
'Now turn right' will be heard as coming from the right.
'and then turn left' will be heard as coming from the left.
Note: The estimation for playing both audio cues could be not fully accurate and therefore
a mismatch between the audio source and the audio cue message could be perceived.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="CustomPanningData">
/sdk-for-flutter-navigate-navigation-custompanningdata-custompanningdata(Duration? estimatedAudioCueDuration, double? initialAzimuthInDegrees, double? sweepAzimuthInDegrees)
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="estimatedAudioCueDuration">
/sdk-for-flutter-navigate-navigation-custompanningdata-estimatedaudiocueduration
↔ Duration?
</dt>
<dd>
  Customized estimated duration for playing the audio cue on the selected TTS Engine.
When not used, HERE SDK's estimation will be used instead.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-navigation-custompanningdata-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="initialAzimuthInDegrees">
/sdk-for-flutter-navigate-navigation-custompanningdata-initialazimuthindegrees
↔ double?
</dt>
<dd>
  Initial desired angular position of the upcoming audio cue. For example, for a maneuver such
as "Turn right on" (<code>ManeuverAction.RightTurn</code>) we want to create a spatial audio arc
from the front to the right, mimicking the maneuver geometry. In this case,
it is good practice to start the trajectory from an initial azimuth that is slightly located
on the opposite direction of the maneuver (e.g. slightly starting from "front-left")
and terminate the trajectory fully on the right side. The initial azimuth angle of such
a trajectory would be, for example, -5.0 (slightly front-left).
This azimuth value is needed to set the position of the audio renderer before starting
to play the audio cue to avoid unwanted audio "jumps".
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-navigation-custompanningdata-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="sweepAzimuthInDegrees">
/sdk-for-flutter-navigate-navigation-custompanningdata-sweepazimuthindegrees
↔ double?
</dt>
<dd>
  Sweep angle of the upcoming audio cue. For example, for a maneuver such as "Turn right on"
(i.e. <code>ManeuverAction.RightTurn</code>),
within an <code>initial_azimuth_in_degrees</code> of -5 degrees, we want to create a spatial audio arc
trajectory from the front to the right, mimicking the maneuver geometry.
In this case, the desired final angle would be +90 degrees, and therefore, a sweep angle of
+95 degrees would be required.
On the other hand, when the desired spatialization is to the left side
(i.e. <code>ManeuverAction.LeftTurn</code>), the <code>initial_azimuth_in_degrees</code> could be set to +5 degrees
and the <code>sweep_azimuth_in_degrees</code> to -95 degrees
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-navigation-custompanningdata-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-navigation-custompanningdata-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-navigation-custompanningdata-operator-equals(<wbr/>Object other)
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
<li class="self-crumb">CustomPanningData class</li>
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
