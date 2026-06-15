---
title: "MapPolylineSolidRepresentation.withOutline constructor"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-mappolylinesolidrepresentation-withoutline"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineSolidRepresentation.withOutline.html -->


<div>
<h1>MapPolylineSolidRepresentation.withOutline constructor</h1></div>

MapPolylineSolidRepresentation.withOutline(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> lineWidth, </li>
<li>Color color, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> outlineWidth, </li>
<li>Color outlineColor, </li>
<li><a href="sdk-for-flutter-navigate-mapview-linecap">LineCap</a> capShape, </li>
</ol>)
    

<p>Creates a representation for a solid line with outline.</p>
<p>The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
and <code>outlineWidth</code>, the value is constant and equal to the width given for
the smallest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
and <code>outlineWidth</code>, the value is constant and equal to the width given for
the biggest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.</p>
<p>At map measures between two nearest given map measure is
linearly interpolated between width values given for these map measures.</p>
<p>For <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.</p>
<p>For <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.</p>
<p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<ul>
<li>
<p><code>lineWidth</code> The width of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>color</code> The color of the polyline.</p>
</li>
<li>
<p><code>outlineWidth</code> The width of the outline on one side of the polyline depending on
the map measure.</p>
</li>
<li>
<p><code>outlineColor</code> The outline color of the polyline.</p>
</li>
<li>
<p><code>capShape</code> The cap shape applied to both ends of the polyline.</p>
</li>
</ul>
<p>Throws <a href="sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineSolidRepresentation.withOutline(MapMeasureDependentRenderSize lineWidth, ui.Color color, MapMeasureDependentRenderSize outlineWidth, ui.Color outlineColor, LineCap capShape) =&gt; $prototype.withOutline(lineWidth, color, outlineWidth, outlineColor, capShape);</code></pre>

 



</div>
`
}</HTMLBlock>
