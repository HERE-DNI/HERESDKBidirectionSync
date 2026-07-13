---
title: "MaterialReflectivity class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-materialreflectivity-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaterialReflectivity-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MaterialReflectivity-class-sidebar.html">

<div>

# <span class="kind-class">MaterialReflectivity</span> class

</div>

<div class="section desc markdown">

Material reflectivity properties are used to enable per‑pixel lighting for supported map objects (e.g.

`LocationIndicator` markers and their halo).

## Lighting OFF vs ON

By default (when no MaterialReflectivity is assigned) objects are rendered "unlit" (emissive): their texture / color appears at a constant brightness, unaffected by scene lights. Assigning a `MaterialReflectivity` instance to an object that supports it (e.g. `LocationIndicator.materialReflectivity`) automatically enables lighting for this object and all its internal components. Clearing (setting the property to `null`) disables lighting again and restores the unlit appearance.

## Factors

Both factors are expected to be within \[0.0, 1.0\]. Values outside this range are allowed but may produce exaggerated results or be clamped by future implementations. Typical useful ranges:

- ambientFactor: 0.0 – 0.4 (higher values flatten the shading and reduce directional contrast)
- diffuseFactor: 0.5 – 1.0 (lower values dim the object under directional light)

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-materialreflectivity">MaterialReflectivity</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-ambientfactor">ambientFactor</a></span> <span class="signature">↔ double</span>  
The ambient factor controls how much of the object's base color is treated as constant ambient contribution (independent of light direction) when lighting is enabled. Default value is 0.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-diffusefactor">diffuseFactor</a></span> <span class="signature">↔ double</span>  
The diffuse factor controls how much of the object's color contributes to the diffuse lighting component when lighting is enabled. Default value is 1.0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-materialreflectivity-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
