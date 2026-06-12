---
title: "MapPolylineSolidMultiColorRepresentation class abstract"
slug: "sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidMultiColorRepresentation-class.html -->


<div>
<h1>MapPolylineSolidMultiColorRepresentation class abstract</h1></div>

<p>Representation allows map polyline to be colored in multiple specified color segments.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.</p>
<p>Examples:
The following configuration will color map polyline as follows:</p>
<ul>
<li>from the start to the middle of it at the 0.5 point - in Red</li>
<li>from the middle point 0.5 to the 0.7 point - in Green</li>
<li>from 0.7 to 1.0 - in Red
'colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}'</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<ul><li>Implemented types</li></ul>


<h2>Constructors</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation">MapPolylineSolidMultiColorRepresentation</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation-withoutline">MapPolylineSolidMultiColorRepresentation.withOutline</a></li></ul>


<h2>Properties</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-hashcode">hashCode</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-runtimetype">runtimeType</a></li></ul>


<h2>Methods</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-nosuchmethod">noSuchMethod</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolorgradientlength">setMultiColorGradientLength</a></li><li><a href="/sdk-for-flutter-explore-mapview-mappolylinesolidmulticolorrepresentation-setmulticolors">setMultiColors</a></li><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-tostring">toString</a></li></ul>


<h2>Operators</h2>
<ul><li><a href="/sdk-for-flutter-explore-mapview-mapitemrepresentation-operator-equals">operator ==</a></li></ul>

 



</div>
`
}</HTMLBlock>
