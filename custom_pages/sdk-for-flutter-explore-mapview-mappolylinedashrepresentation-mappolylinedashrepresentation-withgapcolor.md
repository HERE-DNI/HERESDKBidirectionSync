---
title: "MapPolylineDashRepresentation.withGapColor constructor"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-mappolylinedashrepresentation-withgapcolor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashRepresentation.withGapColor.html -->


<div>
<h1>MapPolylineDashRepresentation.withGapColor constructor</h1></div>

MapPolylineDashRepresentation.withGapColor(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> lineWidth, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> dashLength, </li>
<li><a href="/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> gapLength, </li>
<li>Color dashColor, </li>
<li>Color gapColor, </li>
</ol>)
    

<p>Creates a representation for a dashed line with both dash and the gap being colored.</p>
<p>At map measures smaller than the smallest map measure in the <code>lineWidth</code>,
<code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
and equal to the value given for the smallest map measure in the
respective <a href="/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> object.</p>
<p>At map measures bigger than the biggest map measure in the <code>lineWidth</code>,
<code>dashLength</code> and <code>gapLength</code>, the value used for rendering is constant
and equal to the value given for the biggest map measure in the
respective <a href="/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> object.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="/sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.</p>
<p>For <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="/sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.</p>
<p>All sizes must not be 0 (<a href="/sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> with all values set to 0.0).</p>
<ul>
<li>
<p><code>lineWidth</code> The width of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>dashLength</code> The dash length of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>gapLength</code> The gap length of the polyline depending on the map measure.</p>
</li>
<li>
<p><code>dashColor</code> The color of the dashes.</p>
</li>
<li>
<p><code>gapColor</code> The color of the gaps.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-explore-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineDashRepresentation.withGapColor(MapMeasureDependentRenderSize lineWidth, MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, ui.Color dashColor, ui.Color gapColor) =&gt; $prototype.withGapColor(lineWidth, dashLength, gapLength, dashColor, gapColor);</code></pre>

 



</div>
`
}</HTMLBlock>
