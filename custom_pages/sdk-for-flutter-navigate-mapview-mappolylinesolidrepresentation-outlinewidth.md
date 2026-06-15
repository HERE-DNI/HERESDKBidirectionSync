---
title: "outlineWidth property"
slug: "sdk-for-flutter-navigate-mapview-mappolylinesolidrepresentation-outlinewidth"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- outlineWidth.html -->


<div>
<h1>outlineWidth property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-navigate-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>
outlineWidth


<p>The width of the outline on one side of the polyline depending on the map measure.
The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code>outlineWidth</code>,
outline width is constant and equal to the width given for the smallest
map measure in the <code>outlineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>outlineWidth</code>,
outline width is constant and equal to the width given for the biggest
map measure in the <code>outlineWidth</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.
Gets the map measure dependent polyline outline width.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureDependentRenderSize get outlineWidth;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
