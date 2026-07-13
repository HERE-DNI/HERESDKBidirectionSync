---
title: "LowSpeedZoneWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/LowSpeedZoneWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">LowSpeedZoneWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive low speed zone warnings.

**Note:** This is currently available *only* for Japan. The low speed zone warner is a zone warner, which means that for a low speed zone there will *always* be 3 warnings emitted, with the `LowSpeedZoneWarning.distance_type` set to `DistanceType.AHEAD`, `DistanceType.REACHED` and lastly `DistanceType.PASSED` when the end of the low speed zone is passed.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-lowspeedzonewarninglistener">LowSpeedZoneWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onLowSpeedZoneWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onLowSpeedZoneWarningUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class">LowSpeedZoneWarning</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive low speed zone warnings.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-onlowspeedzonewarningupdated">onLowSpeedZoneWarningUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onLowSpeedZoneWarningUpdated-param-lowSpeedZoneWarning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class">LowSpeedZoneWarning</a></span> <span class="parameter-name">lowSpeedZoneWarning</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new low speed zone warning is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

