---
title: "TrafficMergeWarningListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarningListener-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/TrafficMergeWarningListener-class-sidebar.html">

<div>

# <span class="kind-class">TrafficMergeWarningListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive traffic merge warnings.

**Note:** The traffic merge warner is a point warner, which means that for a traffic merge there will *always* be 2 warnings emitted, with the `TrafficMergeWarning.distance_type` set to `DistanceType.AHEAD` and `DistanceType.PASSED` which is given when the location of the traffic merge is reached. A `TrafficMergeWarning` will not be given until the previous warning of that type has been passed. For example, a route with `TrafficMergeWarning` 120 meters and `TrafficMergeWarning` 160 meters ahead, the first `TrafficMergeWarning.distance_to_traffic_merge_in_meters` is 120 meters and the next `TrafficMergeWarning.distance_to_traffic_merge_in_meters` is then 40 meters, since that is the distance between the first and second warnings.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-trafficmergewarninglistener">TrafficMergeWarningListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onTrafficMergeWarningUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onTrafficMergeWarningUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive traffic merge warnings.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-ontrafficmergewarningupdated">onTrafficMergeWarningUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onTrafficMergeWarningUpdated-param-trafficMergeWarning" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a></span> <span class="parameter-name">trafficMergeWarning</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever a new traffic merge warning is available.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
