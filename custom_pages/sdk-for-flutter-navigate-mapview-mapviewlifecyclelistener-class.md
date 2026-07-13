---
title: "MapViewLifecycleListener class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapViewLifecycleListener-class-sidebar.html">

<div>

# <span class="kind-class">MapViewLifecycleListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

A `MapView` is using a

<a href="https://developer.android.com/reference/android/view/SurfaceView">SurfaceView</a> for Android and <a href="https://developer.apple.com/documentation/quartzcore/cametallayer">CAMetalLayer</a> for iOS to render its content.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-mapviewlifecyclelistener">MapViewLifecycleListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onAttachLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onAttachLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-onDetachLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDetachLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span></span>), </span><span id="sdk-for-flutter-navigate-param-onPauseLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPauseLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-onResumeLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onResumeLambda</span>(), </span><span id="sdk-for-flutter-navigate-param-onDestroyLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDestroyLambda</span>()</span>)</span>  
Provides a mechanism for observing a lifecycle of a map view and/or implementing components whose lifecycle needs to be linked with that of a map view.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onattach">onAttach</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onAttach-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called when adding <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> to the map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-ondestroy">onDestroy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Called when the map view to which this is attached to is destroyed.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-ondetach">onDetach</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onDetach-param-mapView" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapviewbase-class">MapViewBase</a></span> <span class="parameter-name">mapView</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called when removing <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> from the map view.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onpause">onPause</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Called when the map view to which this <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> is attached to gets paused (usually when the app goes into background).

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-onresume">onResume</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Called when the map view to which this <a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-class">MapViewLifecycleListener</a> is attached to gets resumed (usually when the app goes into foreground).

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapviewlifecyclelistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

