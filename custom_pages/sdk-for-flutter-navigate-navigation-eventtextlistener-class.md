---
title: "EventTextListener class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-eventtextlistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/navigation-library-sidebar.html" data-below-sidebar="navigation/EventTextListener-class-sidebar.html">

<div>

# <span class="kind-class">EventTextListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

This abstract class should be implemented in order to receive notifications when text notifications are available from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

Multiple notifications can be given for the same maneuver at different distances.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-eventtextlistener">EventTextListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onEventTextUpdatedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onEventTextUpdatedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a></span></span>)</span>)</span>  
This abstract class should be implemented in order to receive notifications when text notifications are available from <a href="sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-oneventtextupdated">onEventTextUpdated</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onEventTextUpdated-param-eventText" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a></span> <span class="parameter-name">eventText</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called whenever there is a new text notification for a maneuver (multiple notifications can be given for the same maneuver at different distances (for example: "After 500 meters turn right." or "Now turn right.") and in that case, this method will be called once for each distance.

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-navigation-eventtextlistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

