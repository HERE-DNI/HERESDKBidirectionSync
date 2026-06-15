---
title: "MapMeasureDependentRenderSize.withSingleSize constructor"
slug: "sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize-withsinglesize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMeasureDependentRenderSize.withSingleSize.html -->


<div>
<h1>MapMeasureDependentRenderSize.withSingleSize constructor</h1></div>

MapMeasureDependentRenderSize.withSingleSize(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-rendersizeunit">RenderSizeUnit</a> sizeUnit, </li>
<li>double size</li>
</ol>)
    

<p>Constructs a <code>MapMeasureDependentRenderSize</code> from single size value which is constant across all map measures.</p>
<p>The given <code>size</code> value is stored in <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-sizes">MapMeasureDependentRenderSize.sizes</a> map at key 0 and <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-measurekind">MapMeasureDependentRenderSize.measureKind</a> is set to <a href="sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a>.</p>
<ul>
<li>
<p><code>sizeUnit</code> The unit used for the value in <code>size</code>.</p>
</li>
<li>
<p><code>size</code> The size independent of map measure. Must not be negative.</p>
</li>
</ul>
<p>Throws <a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersizeinstantiationexception-class">MapMeasureDependentRenderSizeInstantiationException</a>. Instantiation error if <code>size</code> is negative.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMeasureDependentRenderSize.withSingleSize(RenderSizeUnit sizeUnit, double size) =&gt; $prototype.withSingleSize(sizeUnit, size);</code></pre>

 



</div>
`
}</HTMLBlock>
