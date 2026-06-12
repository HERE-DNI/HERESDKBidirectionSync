---
title: "MapPolylineSolidMultiColorRepresentation constructor"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidmulticolorrepresentation-mappolylinesolidmulticolorrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidMultiColorRepresentation.html -->


<div>
<h1>MapPolylineSolidMultiColorRepresentation constructor</h1></div>

MapPolylineSolidMultiColorRepresentation(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> lineWidth, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-linecap">LineCap</a> capShape, </li>
<li>List&lt;double&gt; colorStops, </li>
<li>List&lt;int&gt; colorIndices, </li>
<li>List&lt;Color&gt; colors, </li>
<li>double gradientLength, </li>
</ol>)
    

<p>Creates a representation for a multicolored line without an outline.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code>MapPolyline.progressColor</code> overrides any of the multiple color.</p>
<p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures between two nearest given map measures line width is
linearly interpolated between width values given for these map measures.</p>
<p>For <a href="/sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="/sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.</p>
<p>For <a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.</p>
<p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>lineWidth</code> The width of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>capShape</code> The cap shape applied to both ends of the polyline.</p>
</li>
<li>
<p><code>colorStops</code> List containing color stop values indicating a change of color on a polyline.
Color stops must be in the range of [0.0, 1.0].
Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
Color stop list must be of the same size as color indices list.
Maximum size is 100 color stops.
An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
</li>
<li>
<p><code>colorIndices</code> List of color indices (from the color list) corresponding to the color stops.
Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
Color indices list must be of the same size as color stop list.
Maximum size is 100 color indices.</p>
</li>
<li>
<p><code>colors</code> List of colors.
Maximum size is 16 colors.
An empty list is not allowed.</p>
</li>
<li>
<p><code>gradientLength</code> Multiple color segment gradient length.</p>
</li>
</ul>
<p>Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
gradient of specific length which is part of the color segment being blended.</p>
<p>Start of the segment is blended with a color from the previous segment.
Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
E.g. a value of '0.1' means 10% of the length of the smallest segment will be blended with a color from its previous segment.
For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
smallest segment's size to other segment size ratio.</p>
<p>Length of '0.0' is the default value which means blending will not be applied.
Valid value range is [0.0, 1.0]. Out of range values are not supported.</p>
<p>Throws <a href="/sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineSolidMultiColorRepresentation(MapMeasureDependentRenderSize lineWidth, LineCap capShape, List&lt;double&gt; colorStops, List&lt;int&gt; colorIndices, List&lt;ui.Color&gt; colors, double gradientLength) =&gt; $prototype.$init(lineWidth, capShape, colorStops, colorIndices, colors, gradientLength);</code></pre>

 



</div>
`
}</HTMLBlock>
