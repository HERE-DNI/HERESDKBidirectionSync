---
title: "RealisticViewWarning class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarning-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RealisticViewWarning-class-sidebar.html">

<div>

# <span class="kind-class">RealisticViewWarning</span> class

</div>

<div class="section desc markdown">

A realistic view notification.

This notification is given for complex junctions and it includes a visual representation of that junction, in order to help the user to better navigate it. When `RealisticViewWarning.distanceType` is <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a>, the <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">RealisticViewWarning.realisticViewVectorImage</a> object will be provided with the junction view and the signpost representations. For `RealisticViewWarning.distanceType` with value <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a>, the <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">RealisticViewWarning.realisticViewVectorImage</a> object will be null. Use `RealisticViewWarningListener` to get notifications about the realistic views of the upcoming junctions.

Realistic view notifications require an online connection in order to function properly, or that the junction or signpost map layer data is cached, installed or preloaded as part of a `Region`. This can be enabled via feature configurations.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewwarning">RealisticViewWarning</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-distanceToRealisticViewInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceToRealisticViewInMeters</span>, </span><span id="sdk-for-flutter-navigate-param-distanceType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span> <span class="parameter-name">distanceType</span></span>)</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">distanceToRealisticViewInMeters</a></span> <span class="signature">↔ double</span>  
Distance to the junction, for which the realistic view is given, expressed in meters.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetype">distanceType</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType</a></span>  
The distance type for the warning, e.g. a warning for a new realistic view ahead or a warning for passing a realistic view. Since the realistic view warning is given relative to a single position on the route, <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.reached</a> will never be given for this warning.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-id">id</a></span> <span class="signature">↔ int</span>  
Unique identifier for this specific realistic view warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewrasterimage">realisticViewRasterImage</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-realisticviewrasterimage-class">RealisticViewRasterImage</a>?</span>  
The realistic view object for which the warning is given. Image resources are stored as raster graphics. Within <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a>, only one type of image, either raster or vector, will be provided. If this property is not `null`, then <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">RealisticViewWarning.realisticViewVectorImage</a> will be `null`. **Note:** Certain countries support only raster images as realistic views. Currently, this is the case only for Japan, but in the future, more countries might support this type of realistic views.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewvectorimage">realisticViewVectorImage</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-navigation-realisticviewvectorimage-class">RealisticViewVectorImage</a>?</span>  
The realistic view object for which the warning is given. Image resources are stored as vector graphics. Within <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a>, only one type of image, either raster or vector, will be provided. If this property is not `null`, then <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-realisticviewrasterimage">RealisticViewWarning.realisticViewRasterImage</a> will be `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

