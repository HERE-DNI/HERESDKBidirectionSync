---
title: "MapLayer class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-maplayer-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapLayer-class-sidebar.html">

<div>

# <span class="kind-class">MapLayer</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Interface for managing a map layer.

A map layer can be created by using the <a href="sdk-for-flutter-navigate-mapview-maplayerbuilder-class">MapLayerBuilder</a>. At creation, the layer gets added to a map. The layer gets removed from the map upon instance destruction.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-maplayer">MapLayer</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-destroy">destroy</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Frees all internally used resources.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-setenabled">setEnabled</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setEnabled-param-enable" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enable</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets whether or not the layer is enabled to be drawn.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-setpriority">setPriority</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setPriority-param-priority" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-maplayerpriority-class">MapLayerPriority</a></span> <span class="parameter-name">priority</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the render priority for the layer which replaces any previously defined priorities.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-setstyle">setStyle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setStyle-param-style" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-style-class">Style</a></span> <span class="parameter-name">style</span></span>) <span class="returntype parameter">→ void</span> </span>  
Sets the style to be used by the layer.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-maplayer-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

