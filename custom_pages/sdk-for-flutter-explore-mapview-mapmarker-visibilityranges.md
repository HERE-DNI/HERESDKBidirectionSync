---
title: "visibilityRanges property"
slug: "sdk-for-flutter-explore-mapview-mapmarker-visibilityranges"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- visibilityRanges.html -->


<div>
<h1>visibilityRanges property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a>&gt;
visibilityRanges


<p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.
Gets the list of visibility ranges. The map marker is visible only inside these map measure
ranges. When empty (the default), the map marker is visible without map measure restrictions.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;MapMeasureRange&gt; get visibilityRanges;</code></pre>

</section>
<section id="setter">

void
visibilityRanges=(List&lt;<a href="/sdk-for-flutter-explore-mapview-mapmeasurerange-class">MapMeasureRange</a>&gt; value)


<p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.
Sets visibility ranges for this map marker.</p>
<p>A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range.
The map marker is visible only inside these map measure ranges.</p>
<p>When empty (the default), the map marker is visible without map measure restrictions.
Only <code>MapMeasureRange</code>(s) of <a href="/sdk-for-flutter-explore-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type are supported.
<code>MapMeasureRange</code>(s) of other unsupported types will be ignored.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set visibilityRanges(List&lt;MapMeasureRange&gt; value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
