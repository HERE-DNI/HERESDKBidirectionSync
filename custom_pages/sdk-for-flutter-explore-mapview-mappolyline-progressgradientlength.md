---
title: "progressGradientLength property"
slug: "sdk-for-flutter-explore-mapview-mappolyline-progressgradientlength"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- progressGradientLength.html -->


<div>
<h1>progressGradientLength property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>
progressGradientLength


<p>The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
Gets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureDependentRenderSize get progressGradientLength;</code></pre>

</section>
<section id="setter">

void
progressGradientLength=(<a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> value)


<p>The maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
Sets the maximum gradient length between <code>MapPolyline.lineColor' and 'MapPolyline.progressColor</code> in zoom level dependent pixels.
To achieve a constant gradient length, use <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>
with a single value. To achieve a gradient length dependent on map zoom,
use <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> with multiple values. The default value is a constant
gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the
actual gradient can be shorter then <code>progressGradientLength</code>.</p>
<p>For <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind</a> only <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported.
For <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> only <a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit.pixels</a> is supported.
A parameter with unsupported values is ignored.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set progressGradientLength(MapMeasureDependentRenderSize value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
