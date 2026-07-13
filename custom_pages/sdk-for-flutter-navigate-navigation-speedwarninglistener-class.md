---
title: "SpeedWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedwarninglistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/SpeedWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">SpeedWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

**Note:** The warnings issued by this abstract class don't take into account any temporary special speed limits. See `SpeedLimitListener`.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-speedwarninglistener">SpeedWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onSpeedWarningStatusChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onSpeedWarningStatusChangedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive notifications when a speed limit on a road is exceeded or driving speed is restored back to normal.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-onspeedwarningstatuschanged">onSpeedWarningStatusChanged</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onSpeedWarningStatusChanged-param-status" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></span> <span class="parameter-name">status</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new `SpeedWarningStatus` is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-speedwarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

