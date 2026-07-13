---
title: "InterpolatedLocationListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/InterpolatedLocationListener-class-sidebar.html">

<div>

# <span class="kind-class">InterpolatedLocationListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive interpolated locations.

The interpolated locations are only provided between <a href="sdk-for-flutter-navigate-navigation-visualnavigator-startrendering">VisualNavigator.startRendering</a> and <a href="sdk-for-flutter-navigate-navigation-visualnavigator-stoprendering">VisualNavigator.stopRendering</a> calls and the application is not running in the background.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-interpolatedlocationlistener">InterpolatedLocationListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onInterpolatedLocationUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onInterpolatedLocationUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive interpolated locations.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-oninterpolatedlocationupdated">onInterpolatedLocationUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onInterpolatedLocationUpdated-param-location" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-location-class">Location</a></span> <span class="parameter-name">location</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new interpolated location is calculated, usually several times per second.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-interpolatedlocationlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

