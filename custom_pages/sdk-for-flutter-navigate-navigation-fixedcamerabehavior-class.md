---
title: "FixedCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-fixedcamerabehavior-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- FixedCameraBehavior-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/FixedCameraBehavior-class-sidebar.html">

<div>

# <span class="kind-class">FixedCameraBehavior</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use this class to follow the current location of the user: The camera will permanently look at the target location that was fed into the navigator instance.

Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-fixedcamerabehavior">FixedCameraBehavior</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-camerabearingindegrees">cameraBearingInDegrees</a></span> <span class="signature">↔ double?</span>  
Camera bearing in degrees. Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range is \[0, 360\]. If set, it will prevent the map from rotating to the direction of travel. For example, a value of zero results in "north up" mode. Defaults to `null`, which means the camera derives the bearing from the <a href="sdk-for-flutter-navigate-core-location-class">Location</a>, so that it points to the direction of travel. If this property is `null` and the device does not provide bearing, the last known value is used or zero otherwise. Gets the currently set fixed bearing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-cameradistanceinmeters" class="deprecated">cameraDistanceInMeters</a></span> <span class="signature">↔ double</span>  
Camera distance in meters. Camera distance to current location. The default value is 150 meters. Gets the currently set camera distance to current location. The default value is 150 meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-cameratiltindegrees">cameraTiltInDegrees</a></span> <span class="signature">↔ double</span>  
Camera tilt with axis parallel to the ground. The default value is 50 degrees. Gets the currently set camera tilt with axis parallel to the ground. The default value is 50 degrees.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">normalizedPrincipalPoint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span>  
The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview. Gets the currently set normalized principal point to be used during navigation.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-fixedcamerabehavior-zoom">zoom</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>  
Zoom configuration. The default value is 150 meters. Camera zoom configuration. The default value is 150 meters. Note: <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.scale</a> is not supported. Gets the current camera's zoom configuration.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

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

</div>
`
}</HTMLBlock>
