---
title: "TrackingCameraBehaviorManeuverModeConfiguration class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehaviorManeuverModeConfiguration-class-sidebar.html">

<div>

# <span class="kind-class">TrackingCameraBehaviorManeuverModeConfiguration</span> class

</div>

<div class="section desc markdown">

Configuration that defines how <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> reacts to nearby maneuvers.

On each frame, and based on the current position, the availability of its functional road class, and the availability of maneuver data for at least one adjacent maneuver, the camera checks for a match against the <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules">TrackingCameraBehaviorManeuverModeConfiguration.maneuverRules</a> in the order they are listed. If a match is found, subsequent rules are not checked. If no match is found, if inputs are unavailable, or if the matched rule has `null` options, the camera does not react.

For correct default initialization, use <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration">TrackingCameraBehavior.defaultManeuverModeConfiguration</a>.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-trackingcamerabehaviormaneuvermodeconfiguration">TrackingCameraBehaviorManeuverModeConfiguration</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-bearingthresholdindegrees">bearingThresholdInDegrees</a></span> <span class="signature">↔ double</span>  
Maximum angle difference in degrees between the current bearing and the bearing to the maneuver point. If the difference exceeds this threshold, the camera does not turn towards the maneuver. Valid range is 0.0 to 180.0. Defaults to 25.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-maneuverrules">maneuverRules</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuverrule-class">TrackingCameraBehaviorManeuverRule</a></span>\></span></span>  
Ordered list of maneuver rules. Rules are evaluated in order; the first matching rule determines the camera behavior. If empty, this configuration is not valid and the camera does not react to maneuvers. If <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration">TrackingCameraBehavior.defaultManeuverModeConfiguration</a> is not used for <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>, it will be an empty list.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

