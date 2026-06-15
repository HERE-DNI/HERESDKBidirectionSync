---
title: "dashLength property"
slug: "sdk-for-flutter-explore-mapview-mappolylinedashrepresentation-dashlength"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- dashLength.html -->


<div>
<h1>dashLength property</h1></div>
<section id="getter">

<a href="sdk-for-flutter-explore-mapview-mapmeasuredependentrendersize-class">MapMeasureDependentRenderSize</a>
dashLength


<p>The dash length of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>dashLength</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>dashLength</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>dashLength</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>dashLength</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.
Gets the map measure dependent polyline dash length.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapMeasureDependentRenderSize get dashLength;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
