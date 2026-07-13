---
title: "TriangleMeshBuilder class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/TriangleMeshBuilder-class-sidebar.html">

<div>

# <span class="kind-class">TriangleMeshBuilder</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Builder for a single triangle.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-trianglemeshbuilder">TriangleMeshBuilder</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-build">build</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mesh-class">Mesh</a>?</span> </span>  
Returns <a href="sdk-for-flutter-navigate-mapview-mesh-class">Mesh?</a>. mesh containing added geometry or 'null' if no geometry was added.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-quad">quad</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-quad-param-a" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">a</span>, </span><span id="sdk-for-flutter-navigate-quad-param-b" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">b</span>, </span><span id="sdk-for-flutter-navigate-quad-param-c" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">c</span>, </span><span id="sdk-for-flutter-navigate-quad-param-d" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">d</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-quadmeshbuilder-class">QuadMeshBuilder</a></span> </span>  
Adds a quad.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-triangle">triangle</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-triangle-param-a" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">a</span>, </span><span id="sdk-for-flutter-navigate-triangle-param-b" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">b</span>, </span><span id="sdk-for-flutter-navigate-triangle-param-c" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-point3d-class">Point3D</a></span> <span class="parameter-name">c</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-class">TriangleMeshBuilder</a></span> </span>  
Adds a triangle.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-trianglemeshbuilder-withtexturecoordinates">withTextureCoordinates</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-withTextureCoordinates-param-a" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">a</span>, </span><span id="sdk-for-flutter-navigate-withTextureCoordinates-param-b" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">b</span>, </span><span id="sdk-for-flutter-navigate-withTextureCoordinates-param-c" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></span> <span class="parameter-name">c</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-meshbuilder-class">MeshBuilder</a></span> </span>  
Adds texture coordinates to a triangle.

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-meshbuilder-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

