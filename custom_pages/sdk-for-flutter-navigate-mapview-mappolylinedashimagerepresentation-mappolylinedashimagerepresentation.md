---
title: "MapPolylineDashImageRepresentation constructor"
slug: "sdk-for-flutter-navigate-mapview-mappolylinedashimagerepresentation-mappolylinedashimagerepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineDashImageRepresentation.html -->


<div>
<h1>MapPolylineDashImageRepresentation constructor</h1></div>

MapPolylineDashImageRepresentation(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> dashLength, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> gapLength, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> dashWidth, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-mapimage-class">MapImage</a> image, </li>
</ol>)
    

<p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.</p>
<p>Dashes are rendered as image.</p>
<p>This allows for patterns like <code>'  —  —  —  —'</code> or <code>' ——— ——— ———'</code>.</p>
<p>For <a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a> supplied for <code>dashLength</code>, <code>gapLength</code> and <code>dashWidth</code>,
only <a href="/sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> is supported for <a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-measurekind">MapMeasureDependentRenderSize.measureKind</a>
and only <a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit.meters</a> is supported for <a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizeunit">MapMeasureDependentRenderSize.sizeUnit</a>.</p>
<p>Only map measure values in range [3-19] are supported.</p>
<p>The value of the keys in <a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> is truncated to integer values,
hence only a single value can be provided per zoom level.</p>
<p>The values are interpolated linearly between zoom levels.</p>
<ul>
<li>
<p><code>dashLength</code> The map measure dependent length of a dash, to which image width is stretched.</p>
</li>
<li>
<p><code>gapLength</code> The map measure dependent length of a gap between dash images.</p>
</li>
<li>
<p><code>dashWidth</code> The map measure dependent width of a dash, to which image height is stretched.</p>
</li>
<li>
<p><code>image</code> Image to be rendered in place of dash space. It is stretched to match <code>dashWidth</code> and <code>dashLength</code>.</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-mapview-mappolylinerepresentationinstantiationexception-class">MapPolylineRepresentationInstantiationException</a>. In case of invalid input parameters.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineDashImageRepresentation(MapMeasureDependentRenderSize dashLength, MapMeasureDependentRenderSize gapLength, MapMeasureDependentRenderSize dashWidth, MapImage image) =&gt; $prototype.$init(dashLength, gapLength, dashWidth, image);</code></pre>

 



</div>
`
}</HTMLBlock>
