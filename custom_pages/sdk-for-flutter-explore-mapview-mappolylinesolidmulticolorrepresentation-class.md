---
title: "MapPolylineSolidMultiColorRepresentation class - mapview library - Dart API"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidMultiColorRepresentation-class.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolylineSolidMultiColorRepresentation-class-sidebar.html">

<div>

# <span class="kind-class">MapPolylineSolidMultiColorRepresentation</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Representation allows map polyline to be colored in multiple specified color segments.

Color segment is defined by color stops. Color stop is specified as a polyline length ratio (0.0 - start of the polyline, 1.0 - end of the polyline). Color stop represents a color change starting at that exact point up until either the next color stop (if one exists) or the end of the polyline.

Progress color `MapPolyline.progressColor` overrides any of the multiple color.

Examples: The following configuration will color map polyline as follows:

- from the start to the middle of it at the 0.5 point - in Red
- from the middle point 0.5 to the 0.7 point - in Green
- from 0.7 to 1.0 - in Red 'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'

Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section">

Implemented types  
- <a href="sdk-for-flutter-explore-mapview-mappolylinerepresentation-class">MapPolylineRepresentation</a>

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation">MapPolylineSolidMultiColorRepresentation</a></span><span class="signature">(<span id="sdk-for-flutter-explore-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span><span id="sdk-for-flutter-explore-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span>, </span><span id="sdk-for-flutter-explore-param-colorStops" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">colorStops</span>, </span><span id="sdk-for-flutter-explore-param-colorIndices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">colorIndices</span>, </span><span id="sdk-for-flutter-explore-param-colors" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">Color</span>\></span></span> <span class="parameter-name">colors</span>, </span><span id="sdk-for-flutter-explore-param-gradientLength" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">gradientLength</span></span>)</span>  
Creates a representation for a multicolored line without an outline.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation-withoutline">MapPolylineSolidMultiColorRepresentation.withOutline</a></span><span class="signature">(<span id="sdk-for-flutter-explore-withOutline-param-lineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">lineWidth</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-outlineWidth" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a></span> <span class="parameter-name">outlineWidth</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-outlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">outlineColor</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-capShape" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-mapview-linecap">LineCap</a></span> <span class="parameter-name">capShape</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-colorStops" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">colorStops</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-colorIndices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">colorIndices</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-colors" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">Color</span>\></span></span> <span class="parameter-name">colors</span>, </span><span id="sdk-for-flutter-explore-withOutline-param-gradientLength" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">gradientLength</span></span>)</span>  
Creates a representation for a multicolored line with an outline.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapitemrepresentation-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapitemrepresentation-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapitemrepresentation-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolorgradientlength">setMultiColorGradientLength</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setMultiColorGradientLength-param-length" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">length</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Sets the multiple color segment gradient length.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolors">setMultiColors</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-setMultiColors-param-colorStops" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>\></span></span> <span class="parameter-name">colorStops</span>, </span><span id="sdk-for-flutter-explore-setMultiColors-param-colorIndices" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">int</span>\></span></span> <span class="parameter-name">colorIndices</span>, </span><span id="sdk-for-flutter-explore-setMultiColors-param-colors" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">Color</span>\></span></span> <span class="parameter-name">colors</span></span>) <span class="returntype parameter">→ bool</span> </span>  
Sets lists of colors and multiple color segment stops for the polyline to be colored in.

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapitemrepresentation-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-explore-mapview-mapitemrepresentation-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-explore-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
