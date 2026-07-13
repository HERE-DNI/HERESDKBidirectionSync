---
title: "MapRenderMode enum - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maprendermode"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapRenderMode-enum-sidebar.html">

<div>

# <span class="kind-enum">MapRenderMode</span> enum

</div>

<div class="section desc markdown">

For Android only: Mode of rendering the map by a `HereMap` widget.

Specified by setting <a href="sdk-for-flutter-navigate-mapview-heremapoptions-rendermode">HereMapOptions.renderMode</a> and passing the options object to `HereMap` on creation time.

</div>

## Values

<span class="name">surface</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-maprendermode">MapRenderMode</a></span>  
Map rendering will use `SurfaceView`. This offers best performance but can cause graphical glitches in apps with complex, dynamic UI and/or multiple `MapView` instances.

<span class="name">texture</span> <span class="signature">→ const <a href="sdk-for-flutter-navigate-mapview-maprendermode">MapRenderMode</a></span>  
Map rendering will use `TextureView`. This method has a performance penalty, but makes `MapView` behave like a regular view, supporting view transformations and alpha and avoiding graphical glitches that `SurfaceView` can suffer from in certain scenarios.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-index">index</a></span> <span class="signature">→ int</span>  
A numeric identifier for the enumerated value.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Constants

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maprendermode-values-constant">values</a></span> <span class="signature">→ const List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-maprendermode">MapRenderMode</a></span>\></span></span>  
A constant List of the values in this enum, in order of their declaration.

</div>

<!-- /.main-content --> <!-- /.sidebar-offcanvas --> <span class="no-break"> here_sdk 4.26.0 </span>

