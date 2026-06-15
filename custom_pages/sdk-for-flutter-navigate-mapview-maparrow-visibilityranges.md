---
title: "visibilityRanges property"
slug: "sdk-for-flutter-navigate-mapview-maparrow-visibilityranges"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- visibilityRanges.html -->


<div>
<h1>visibilityRanges property</h1></div>
<section id="getter">

List&lt;<a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a>&gt;
visibilityRanges


<p>The list of visibility ranges, in which the map arrow is visible.
A range is half-open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the map arrows are visible without map measure restrictions.
Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type are supported.
<code>MapMeasureRange</code>(s) of other unsupported types will be ignored.}
Gets the list of visibility ranges.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;MapMeasureRange&gt; get visibilityRanges;</code></pre>

</section>
<section id="setter">

void
visibilityRanges=(List&lt;<a href="sdk-for-flutter-navigate-mapview-mapmeasurerange-class">MapMeasureRange</a>&gt; value)


<p>The list of visibility ranges, in which the map arrow is visible.
A range is half-open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the map arrows are visible without map measure restrictions.
Only <code>MapMeasureRange</code>(s) of <a href="sdk-for-flutter-navigate-mapview-mapmeasurekind">MapMeasureKind.zoomLevel</a> type are supported.
<code>MapMeasureRange</code>(s) of other unsupported types will be ignored.}
Sets visibility ranges for this map arrow.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">set visibilityRanges(List&lt;MapMeasureRange&gt; value);</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
