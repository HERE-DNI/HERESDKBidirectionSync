---
title: "RealisticViewWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarningListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RealisticViewWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">RealisticViewWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive realistic view warnings.

A <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 160 meters ahead, the first <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is 120 meters and the next <a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-realisticviewwarninglistener">RealisticViewWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onRealisticViewWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRealisticViewWarningUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive realistic view warnings.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-onrealisticviewwarningupdated">onRealisticViewWarningUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onRealisticViewWarningUpdated-param-realisticViewWarning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a></span> <span class="parameter-name">realisticViewWarning</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new realistic view warning is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
