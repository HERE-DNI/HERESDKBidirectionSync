---
title: "MapSceneLights class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapscenelights-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapSceneLights-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapSceneLights-class-sidebar.html">

<div>

# <span class="kind-class">MapSceneLights</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Manage the lights and their attributes in a scene.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-mapscenelights">MapSceneLights</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-getcolor">getColor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getColor-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span></span>) <span class="returntype parameter">→ Color?</span> </span>  
Retrieves the current color of the light based on its category.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-getdirection">getDirection</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDirection-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a>?</span> </span>  
Retrieves the current direction of the light based on its category.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-getintensity">getIntensity</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getIntensity-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span></span>) <span class="returntype parameter">→ double?</span> </span>  
Retrieves the current intensity of the light based on its category.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-reset">reset</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Resets all attributes of each light to their default values based on the current map scene settings.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-setcolor">setColor</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setColor-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span>, </span><span id="sdk-for-flutter-navigate-setColor-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span><span id="sdk-for-flutter-navigate-setColor-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Set a new color for the light based on its category.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-setdirection">setDirection</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setDirection-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span>, </span><span id="sdk-for-flutter-navigate-setDirection-param-direction" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsdirection-class">MapSceneLightsDirection</a></span> <span class="parameter-name">direction</span>, </span><span id="sdk-for-flutter-navigate-setDirection-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Set a new direction for the light based on its category.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-setintensity">setIntensity</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-setIntensity-param-category" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightscategory">MapSceneLightsCategory</a></span> <span class="parameter-name">category</span>, </span><span id="sdk-for-flutter-navigate-setIntensity-param-intensity" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">intensity</span>, </span><span id="sdk-for-flutter-navigate-setIntensity-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-mapview-mapscenelightsattributesettingcallback">MapSceneLightsAttributeSettingCallback</a>?</span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Set a new intensity for the light based on its category.

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mapscenelights-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
