---
title: "RoadSignWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadSignWarningListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RoadSignWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">RoadSignWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive road sign warnings.

**Note:** The road sign warner is a point warner, which means that for a road sign there will *always* be 2 warnings emitted, with the <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetype">RoadSignWarning.distanceType</a> set to <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.ahead</a> and <a href="sdk-for-flutter-navigate-navigation-distancetype">DistanceType.passed</a> which is given when the location of the road sign is reached. A <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> will not be given until the previous warning of that type has been passed. For example, a route with <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 120 meters and <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a> 160 meters ahead, the first <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is 120 meters and the next <a href="sdk-for-flutter-navigate-navigation-roadsignwarning-distancetoroadsigninmeters">RoadSignWarning.distanceToRoadSignInMeters</a> is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-roadsignwarninglistener">RoadSignWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onRoadSignWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRoadSignWarningUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive road sign warnings.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-onroadsignwarningupdated">onRoadSignWarningUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onRoadSignWarningUpdated-param-roadSignWarning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-roadsignwarning-class">RoadSignWarning</a></span> <span class="parameter-name">roadSignWarning</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new road sign warning is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-roadsignwarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
