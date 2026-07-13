---
title: "AreaCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-areacamerabehavior-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/AreaCameraBehavior-class-sidebar.html">

<div>

# <span class="kind-class">AreaCameraBehavior</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use this class to show an overview of geo points.

By default, the orientation of the camera will be perpendicular to the Earth's surface (ie. looking towards the center of the Earth), while bearing will be towards north.

Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API's are subject to change without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-areacamerabehavior">AreaCameraBehavior</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-cameraanimationduration">cameraAnimationDuration</a></span> <span class="signature">↔ Duration</span>  
The duration of camera animation in milliseconds. If there is an animation, it will last for specified period of time. Defaults to 500 milliseconds, or half a second. Gets the current animation duration in milliseconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-camerabearingindegrees">cameraBearingInDegrees</a></span> <span class="signature">↔ double</span>  
Camera bearing in degrees. The direction in which the camera will point in degrees clockwise, relative to true North. The input should range between \[0, 360\]. Defaults to true North (0 degrees). Gets the current camera bearing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-cameratiltindegrees">cameraTiltInDegrees</a></span> <span class="signature">↔ double</span>  
Camera tilt in degrees. The tilt of the camera relative to the axis perpendicular to the ground. Defaults to 0 degrees, meaning that it will look straight down into the ground. Gets the current camera tilt.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-iscurrentpositionincluded">isCurrentPositionIncluded</a></span> <span class="signature">↔ bool</span>  
Include current position in camera view. Decides if the current position should be added to the set of visible points. Note that if the current position is in the vicinity of any of the visible points, setting this to `false` will not explicitly exclude the current position from the camera view. However if displaying an area potentially away from the current position, this does need to be explicitly set to `false` or it will try to include the current position. Defaults to false. Gets whether to include the current position.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-maxzoom">maxZoom</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a></span>  
Maximal allowed zoom. Defines maximal zoom level to be applied to enclose geodetic bounding box. Defaults to a <a href="sdk-for-flutter-navigate-mapview-mapmeasure-class">MapMeasure</a> with kind <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> and value 20.0. Note: <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.scale</a> is not supported. Gets maximal allowed zoom.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-normalizedprincipalpoint">normalizedPrincipalPoint</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span>  
The normalized principal point. Normalized principal point to be used during navigation. Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom of the mapview. Gets the currently set normalized principal point to be used during navigation.

<div class="features">

<span class="feature">getter/setter pair</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-principalpointanimationduration">principalPointAnimationDuration</a></span> <span class="signature">↔ Duration</span>  
The duration of principal point animation in milliseconds. If the principal point is changed, the change will be animated over this duration. Defaults to 500 milliseconds, or half a second. Gets the current principal point animation duration in milliseconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-viewrectangle">viewRectangle</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-rectangle2d-class">Rectangle2D</a>?</span>  
The view rectangle for camera updates. Defines a sub-space of the screen that the behavior should consider for camera updates. Defaults to `null`. If not set, it uses the viewport bounds of the underlying map view. Gets the current view rectangle, if it's set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-getvisiblepoints">getVisiblePoints</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> </span>  
Gets configured visible geo points.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-camerabehavior-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-areacamerabehavior-setvisiblepoints">setVisiblePoints</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setVisiblePoints-param-visiblePoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a></span>\></span></span> <span class="parameter-name">visiblePoints</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the list of geo points to show in the camera view.

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

