---
title: "TrackingCameraBehaviorManeuverRuleOptions class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrackingCameraBehaviorManeuverRuleOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehaviorManeuverRuleOptions-class-sidebar.html">

<div>

# <span class="kind-class">TrackingCameraBehaviorManeuverRuleOptions</span> class

</div>

<div class="section desc markdown">

Defines a set of configurations specific to a <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class">TrackingCameraBehaviorManeuverRule</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-trackingcamerabehaviormaneuverruleoptions">TrackingCameraBehaviorManeuverRuleOptions</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-earlypremaneuveractivationthresholdinmeters">earlyPreManeuverActivationThresholdInMeters</a></span> <span class="signature">↔ double</span>  
Distance in meters for early activation. If the current position enters this threshold of the upcoming maneuver while still within <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-postmaneuveractivationthresholdinmeters">TrackingCameraBehaviorManeuverRuleOptions.postManeuverActivationThresholdInMeters</a> of the previous maneuver, the camera behaves as though it were already in the upcoming maneuver's pre-activation zone. Must be non-negative. Defaults to 0.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-postmaneuveractivationthresholdinmeters">postManeuverActivationThresholdInMeters</a></span> <span class="signature">↔ double</span>  
Distance in meters after the previous maneuver point within which this rule remains active. Must be non-negative. Defaults to 0.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-premaneuveractivationthresholdinmeters">preManeuverActivationThresholdInMeters</a></span> <span class="signature">↔ double</span>  
Distance in meters before the next maneuver point within which this rule becomes active. Must be non-negative. Defaults to 0.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-zoomrange">zoomRange</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverzoomrange-class">TrackingCameraBehaviorManeuverZoomRange</a></span>  
The zoom range for this rule. Defines the minimum and maximum zoom levels. Defaults to a default-constructed <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverzoomrange-class">TrackingCameraBehaviorManeuverZoomRange</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverruleoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
