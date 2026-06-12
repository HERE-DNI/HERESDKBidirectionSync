---
title: "MapMeasureDependentRenderSize constructor"
slug: "sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-mapmeasuredependentrendersize"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMeasureDependentRenderSize.html -->


<div>
<h1>MapMeasureDependentRenderSize constructor</h1></div>

MapMeasureDependentRenderSize(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind</a> measureKind, </li>
<li><a href="/sdk-for-flutter-navigate-mapview-rendersizeunit">RenderSizeUnit</a> sizeUnit, </li>
<li>Map&lt;double, double&gt; sizes</li>
</ol>)
    

<p>Constructs a <code>MapMeasureDependentRenderSize</code> from given parameters.</p>
<p>Supplying <code>sizes</code> map with a single entry indicates using a fixed size value across all map measures.</p>
<ul>
<li>
<p><code>measureKind</code> The unit used for the key in <code>sizes</code>.</p>
</li>
<li>
<p><code>sizeUnit</code> The unit used for the value in <code>sizes</code>.</p>
</li>
<li>
<p><code>sizes</code> The dictionary describing the size (value) per map measure (key).</p>
</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersizeinstantiationexception-class">MapMeasureDependentRenderSizeInstantiationException</a>. Instantiation error if <code>sizes</code> map is empty or contains negative keys or values.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMeasureDependentRenderSize(MapMeasureKind measureKind, RenderSizeUnit sizeUnit, Map&lt;double, double&gt; sizes) =&gt; $prototype.$init(measureKind, sizeUnit, sizes);</code></pre>

 



</div>
`
}</HTMLBlock>
