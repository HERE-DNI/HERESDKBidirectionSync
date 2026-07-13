---
title: "SafetyCameraWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SafetyCameraWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">SafetyCameraWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications on safety cameras.

A `SafetyCameraWarning` will not be given until the previous warning of that type has been passed. For example, a route with `SafetyCameraWarning` 120 meters and `SafetyCameraWarning` 160 meters ahead, the first `SafetyCameraWarning.distance_to_camera_in_meters` is 120 meters and the next `SafetyCameraWarning.distance_to_camera_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

When `SafetyCameraWarningListener` is enabled, a new set of text notifications (e.g. "Speed camera ahead") will be trigger if any has been also enabled. The updates for the same safety camera appear in order of the initial `DistanceType.AHEAD` event. That is a first in first out approach is used when multiple safety cameras are reached or passed on the same location.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-safetycamerawarninglistener">SafetyCameraWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onSafetyCameraWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSafetyCameraWarningUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-class">SafetyCameraWarning</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive notifications on safety cameras.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-onsafetycamerawarningupdated">onSafetyCameraWarningUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onSafetyCameraWarningUpdated-param-safetyCameraWarning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarning-class">SafetyCameraWarning</a></span> <span class="parameter-name">safetyCameraWarning</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new `SafetyCameraWarning` is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-safetycamerawarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

