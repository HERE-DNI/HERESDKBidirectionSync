---
title: "TollStopWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-tollstopwarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollStopWarningListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TollStopWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">TollStopWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive information on the upcoming toll booth structure.

The warner might also warn about gates/checkpoints for vignette, border checkpoints and similar structures on the street.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process. A `TollStop` will not be given until the previous warning of that type has been passed. For example, a route with `TollStop` 120 meters and `TollStop` 160 meters ahead, the first `TollStop.distance_to_toll_stop_in_meters` is 120 meters and the next `TollStop.distance_to_toll_stop_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tollstopwarninglistener">TollStopWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onTollStopWarningLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTollStopWarningLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstop-class">TollStop</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive information on the upcoming toll booth structure.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-ontollstopwarning">onTollStopWarning</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onTollStopWarning-param-tollStop" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-tollstop-class">TollStop</a></span> <span class="parameter-name">tollStop</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new `TollStop` is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-tollstopwarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
