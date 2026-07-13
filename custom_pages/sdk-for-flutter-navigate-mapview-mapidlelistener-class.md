---
title: "MapIdleListener class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapidlelistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapIdleListener-class-sidebar.html">

<div>

# <span class="kind-class">MapIdleListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Used to detect when the map becomes idle or busy.

Map is considered busy when its state changes (for example as a result of camera manipulation) and/or when it requires a redraw (for example, as a result of map data being downloaded).

Map is considered idle when current state is fully rendered and no further redraws are necessary.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-mapidlelistener">MapIdleListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onMapBusyLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMapBusyLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-onMapIdleLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onMapIdleLambda</span>()</span>)</span>  
Used to detect when the map becomes idle or busy.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-onmapbusy">onMapBusy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Called when map becomes invalidated and is about to be updated.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-onmapidle">onMapIdle</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Called when map finishes all state updates.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapidlelistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

