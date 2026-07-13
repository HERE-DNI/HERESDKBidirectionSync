---
title: "DynamicCameraBehavior class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-dynamiccamerabehavior-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/DynamicCameraBehavior-class-sidebar.html">

<div>

# <span class="kind-class">DynamicCameraBehavior</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Use this class to follow the current location of the user: The camera will look at the target location that was fed into the navigator instance, gradually zooming in as the user approaches each maneuver and zooming out after the user passes them.

Since location updates happen in discrete intervals, locations in-between will be interpolated to achieve a smooth camera movement. If no route is set, constant values of camera distance and tilt are used.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-navigation-camerabehavior-class">CameraBehavior</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-dynamiccamerabehavior-dynamiccamerabehavior">DynamicCameraBehavior</a></span><span class="signature">()</span>  
Creates a new instance of this class.

<div class="constructor-modifier features">

factory

</div>

## Properties

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

