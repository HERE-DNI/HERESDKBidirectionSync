---
title: "MapPolygon class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mappolygon-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolygon-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/mapview-library-sidebar.html" data-below-sidebar="mapview/MapPolygon-class-sidebar.html">

<div>

# <span class="kind-class">MapPolygon</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A visual representation of a polygon on the map.

Can be used to visualize areas of all shapes and sizes.

The geometry to be visualized is represented by an instance of <a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a>. To display circular areas (for example, a position accuracy indicator) use a GeoPolygon created from a <a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a> using <a href="sdk-for-flutter-navigate-core-geopolygon-geopolygon-withgeocircle">GeoPolygon.withGeoCircle</a>.

Note:

- The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur.
- Polygons which are self-intersecting are not supported and may lead to render artifacts.
- The inner boundaries (holes) specified in the GeoPolygon are ignored.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-mappolygon">MapPolygon</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geometry</span>, </span><span id="sdk-for-flutter-navigate-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span></span>)</span>  
Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.

<div class="constructor-modifier features">

factory

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-mappolygon-withoutlinecolorandoutlinewidthinpixels">MapPolygon.withOutlineColorAndOutlineWidthInPixels</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-geometry" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">geometry</span>, </span><span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-color" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">color</span>, </span><span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-outlineColor" class="parameter"><span class="type-annotation">Color</span> <span class="parameter-name">outlineColor</span>, </span><span id="sdk-for-flutter-navigate-withOutlineColorAndOutlineWidthInPixels-param-outlineWidthInPixels" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">outlineWidthInPixels</span></span>)</span>  
Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-draworder">drawOrder</a></span> <span class="signature">↔ int</span>  
The draw order of this map polygon relative to other map polygons. Gets the draw order of this map polygon relative to other map polygons. Default value is 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-fillcolor">fillColor</a></span> <span class="signature">↔ Color</span>  
Color of the polygon's fill. Gets the current color of the fill.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-geometry">geometry</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span>  
The geometry of the polygon. Setting a new geometry will update the appearance. Gets the current geometry of the polygon.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-metadata">metadata</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-core-metadata-class">Metadata</a>?</span>  
The Metadata instance attached to this polygon, `null` by default. Gets the Metadata instance attached to this polygon.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-outlinecolor">outlineColor</a></span> <span class="signature">↔ Color</span>  
The color of the polygon outline. Gets the color of the polygon outline. The default outline color is opaque white.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-outlinewidth">outlineWidth</a></span> <span class="signature">↔ double</span>  
The width of the polygon outline in pixels. Gets the outline width of the polygon in pixels.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-visibilityranges">visibilityRanges</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a></span>\></span></span>  
The list of visibility ranges. The map polygon is visible only inside these map measure ranges. Gets the list of visibility ranges. The map polygon is visible only inside these map measure ranges. When empty (the default), the map polygon is visible without map measure restrictions.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-mapview-mappolygon-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
