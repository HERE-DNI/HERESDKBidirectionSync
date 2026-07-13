---
title: "TrackingCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrackingCameraBehavior-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrackingCameraBehavior-class-sidebar.html">

<div>

# <span class="kind-class">TrackingCameraBehavior</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use this class to follow a moving target.

The camera smoothly tracks the target’s position while adjusting heading, tilt, and zoom as needed. When tracking starts or resumes, the camera first animates a re-centering transition to align with the target.

Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-bearingindegrees">bearingInDegrees</a></span> <span class="signature">↔ double?</span>  
The camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to `null`, which means the camera derives the bearing from the <a href="sdk-for-flutter-navigate-core-location-class">Location</a>, so that it points to the direction of travel. If this property is `null` and the device does not provide bearing, the last known value is used or zero otherwise. Gets the bearing in degrees.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-ismaneuverdetectionenabled">isManeuverDetectionEnabled</a></span> <span class="signature">↔ bool</span>  
Whether maneuver detection is enabled. When `true`, the camera detects adjacent maneuvers and reacts according to the <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a> set via <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration">TrackingCameraBehavior.setManeuverModeConfiguration</a>. A valid <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a> must be set for the camera to react. Defaults to `false`. Gets whether maneuver detection is enabled.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-maxrotationspeedindegreespersecond">maxRotationSpeedInDegreesPerSecond</a></span> <span class="signature">↔ double</span>  
The maximum rotation speed. Maximum bearing rotation speed in degrees per second, limiting how fast the camera turns. Defaults to 20 degrees per second. Gets the maximum rotation speed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">normalizedPrincipalPoint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span>  
The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview. Gets the currently set normalized principal point to be used during navigation.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-principalpointanimationduration">principalPointAnimationDuration</a></span> <span class="signature">↔ Duration</span>  
The duration of principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second. Gets the current principal point animation duration in milliseconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-recenteranimationduration">recenterAnimationDuration</a></span> <span class="signature">↔ Duration</span>  
The duration of recenter animation in milliseconds. Time to recenter the camera reaching current car position. Defaults to 500 milliseconds, or half a second. Gets the recenter animation duration in milliseconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-tiltindegrees">tiltInDegrees</a></span> <span class="signature">↔ double</span>  
The value of camera tilt in degrees. Camera tilt angle relative to the ground plane, in degrees. Defaults to 50. Gets the camera tilt in degrees.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-viewrectangle">viewRectangle</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>?</span>  
The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to `null`. If not set, it uses the viewport bounds of the underlying map view. Gets the current view rectangle, if it's set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-zoompolicy">zoomPolicy</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorzoompolicy-class">TrackingCameraBehaviorZoomPolicy</a></span>  
The strategy of computing the zoom level. Defines the strategy used to compute the zoom level based on scene heuristics. Defaults to a fixed zoom policy at zoom level 16.5. Gets the current zoom computation strategy.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-zoomspeedinlevelspersecond">zoomSpeedInLevelsPerSecond</a></span> <span class="signature">↔ double</span>  
The zoom level transition speed. Speed factor controlling how quickly the camera transitions between zoom levels Defaults to 0.5 zoom levels per second. Gets the zoom level transition speed.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-flagfixeddurationfornextanimation">flagFixedDurationForNextAnimation</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Enables fixed-duration animation mode for the next property change.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-getmaneuvermodeconfiguration">getManeuverModeConfiguration</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>?</span> </span>  
Gets the current maneuver mode configuration, or `null` if not set.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-setmaneuvermodeconfiguration">setManeuverModeConfiguration</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setManeuverModeConfiguration-param-maneuverModeConfiguration" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>?</span> <span class="parameter-name">maneuverModeConfiguration</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the configuration for camera behavior near maneuvers.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultfunctionalroadclasszoompolicyoptions">defaultFunctionalRoadClassZoomPolicyOptions</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</a></span> </span>  
Returns <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</a>. The default <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorfunctionalroadclasszoompolicyoptions-class">TrackingCameraBehaviorFunctionalRoadClassZoomPolicyOptions</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultmaneuvermodeconfiguration">defaultManeuverModeConfiguration</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a></span> </span>  
Returns <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>. The default <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviormaneuvermodeconfiguration-class">TrackingCameraBehaviorManeuverModeConfiguration</a>.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-defaultspeedbasedzoompolicyoptions">defaultSpeedBasedZoomPolicyOptions</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a></span> </span>  
Returns <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a>. The default <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehaviorspeedbasedzoompolicyoptions-class">TrackingCameraBehaviorSpeedBasedZoomPolicyOptions</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
