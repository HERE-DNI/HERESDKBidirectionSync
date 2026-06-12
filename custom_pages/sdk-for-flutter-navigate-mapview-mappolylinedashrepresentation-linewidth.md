---
title: "lineWidth property"
slug: "sdk-for-flutter-navigate-mapview-mappolylinedashrepresentation-linewidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lineWidth.html -->


<div>
<h1>lineWidth property</h1></div>
<section id="getter">

<a href="/sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>
lineWidth


<p>The width of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.
Gets the map measure dependent polyline width.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureDependentRenderSize get lineWidth;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
