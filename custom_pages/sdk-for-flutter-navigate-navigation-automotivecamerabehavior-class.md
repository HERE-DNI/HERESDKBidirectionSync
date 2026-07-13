---
title: "AutomotiveCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-automotivecamerabehavior-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/AutomotiveCameraBehavior-class-sidebar.html">

<div>

# <span class="kind-class">AutomotiveCameraBehavior</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides a high-level camera controller for automotive navigation that manages both tracking and area camera behaviors.

This class acts as a facade, delegating camera operations to either a <a href="sdk-for-flutter-navigate-navigation-trackingcamerabehavior-class">TrackingCameraBehavior</a> for following the vehicle during navigation or an <a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-class">AreaCameraBehavior</a> for showing overview areas such as points of interest or route previews.

The controller supports three states: tracking mode (following the vehicle), area mode (showing geographic regions), or inactive (no automatic camera control). The inactive state allows external control of the camera, such as when responding to user touch events or when UI logic temporarily disables automatic camera behavior.

Camera configuration, including animation durations, zoom policies, and maneuver handling settings, can be provided through a JSON configuration string or file. The configuration is validated and parsed during construction.

Note: This is a **beta** release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior">AutomotiveCameraBehavior</a></span><span class="signature">()</span>  
Creates a new instance of this class with default camera behaviors and configuration.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-automotivecamerabehavior-fromjson">AutomotiveCameraBehavior.fromJson</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-fromJson-param-configJson" class="parameter"><span class="type-annotation">String</span> <span class="parameter-name">configJson</span></span>)</span>  
Creates a new instance of this class configured from a JSON string.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-activecameratype">activeCameraType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType</a></span>  
The active camera type. Defines which camera behavior is currently active: <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.none</a> (free navigation), <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.tracking</a>, or <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavioractivecameratype">AutomotiveCameraBehaviorActiveCameraType.area</a>. Gets the type of camera currently handling camera updates.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-ismaneuverdetectionenabled">isManeuverDetectionEnabled</a></span> <span class="signature">↔ bool</span>  
Enables or disables automatic camera adjustments during upcoming maneuvers. When enabled, the tracking camera automatically adjusts zoom and framing to provide better visibility of upcoming turns and maneuvers during navigation. The specific adjustments and their timing are defined in the camera configuration.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">normalizedPrincipalPoint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span>  
The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview. Gets the currently set normalized principal point to be used during navigation.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-orientationmode">orientationMode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode</a></span>  
The current orientation mode of the camera. Defines the camera's viewing angle and orientation for tracking mode. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode2d</a>, the camera looks straight down and rotates with the vehicle heading. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.mode3d</a>, the camera is tilted for a perspective view. In <a href="sdk-for-flutter-navigate-navigation-automotivecamerabehaviororientationmode">AutomotiveCameraBehaviorOrientationMode.modeNorthUp</a>, the camera maintains north-up orientation regardless of vehicle heading.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-viewrectangle">viewRectangle</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>?</span>  
The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. This property is forwarded to both the tracking and area cameras, ensuring consistent viewport constraints across all camera modes. If not set, it uses the viewport bounds of the underlying map view. Gets the current view rectangle, if it's set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorgeobox">setAreaCameraBehaviorGeobox</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setAreaCameraBehaviorGeobox-param-geobox" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a></span> <span class="parameter-name">geobox</span></span>) <span class="returntype parameter">→ void</span> </span>  
Configures the Area camera to frame the specified geographic bounding box.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-automotivecamerabehavior-setareacamerabehaviorvisiblepoints">setAreaCameraBehaviorVisiblePoints</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setAreaCameraBehaviorVisiblePoints-param-points" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">points</span>, </span><span id="sdk-for-flutter-navigate-setAreaCameraBehaviorVisiblePoints-param-includeCurrentPosition" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">includeCurrentPosition</span></span>) <span class="returntype parameter">→ void</span> </span>  
Configures the Area camera to frame the specified points.

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

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

