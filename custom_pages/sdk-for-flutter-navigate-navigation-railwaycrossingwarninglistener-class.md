---
title: "RailwayCrossingWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RailwayCrossingWarningListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/RailwayCrossingWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">RailwayCrossingWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive railway crossing warnings.

**Note:** The railway crossing warner can be either a zone warner or a point warner, depending on whether the railroad crossing warning is given for a railroad crossing zone or just a point. This means that for a railway crossing there will can be either 2 or 3 warnings emitted. In case the railroad crossing is a zone warner then 3 warnings will be emitted with the `RailwayCrossingWarning.distance_type` set to `DistanceType.AHEAD`, `DistanceType.REACHED` and lastly `DistanceType.PASSED` when the end of the railway crossing is passed. In case the railroad crossing is a point warner then 2 warnings will be emitted with the `RailwayCrossingWarning.distance_type` set to `DistanceType.AHEAD` and `DistanceType.PASSED` when the end of the railway crossing is passed.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-railwaycrossingwarninglistener">RailwayCrossingWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onRailwayCrossingWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onRailwayCrossingWarningUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive railway crossing warnings.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-onrailwaycrossingwarningupdated">onRailwayCrossingWarningUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onRailwayCrossingWarningUpdated-param-railwayCrossingWarning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarning-class">RailwayCrossingWarning</a></span> <span class="parameter-name">railwayCrossingWarning</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new railway crossing warning is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-railwaycrossingwarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
