---
title: "LocationStatusListener class - location library - Dart API"
slug: "sdk-for-flutter-navigate-location-locationstatuslistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="location/location-library-sidebar.html" data-below-sidebar="location/LocationStatusListener-class-sidebar.html">

<div>

# <span class="kind-class">LocationStatusListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Abstract class for listening the LocationEngine status updates.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-locationstatuslistener">LocationStatusListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onStatusChangedLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onStatusChangedLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-onFeaturesNotAvailableLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onFeaturesNotAvailableLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationfeature">LocationFeature</a></span>\></span></span></span>)</span>)</span>  
Abstract class for listening the LocationEngine status updates.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-onfeaturesnotavailable">onFeaturesNotAvailable</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onFeaturesNotAvailable-param-features" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-location-locationfeature">LocationFeature</a></span>\></span></span> <span class="parameter-name">features</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called after start() if any requested location feature is not available for the application.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-onstatuschanged">onStatusChanged</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onStatusChanged-param-locationEngineStatus" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></span> <span class="parameter-name">locationEngineStatus</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called each time the status of the LocationEngine has changed.

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-location-locationstatuslistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

