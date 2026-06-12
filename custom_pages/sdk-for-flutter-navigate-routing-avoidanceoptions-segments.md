---
title: "segments property"
slug: "sdk-for-flutter-navigate-routing-avoidanceoptions-segments"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- segments.html -->


<div>
<h1>segments property</h1></div>

        
        List&lt;<a href="/sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>&gt;
segments
<div class="features">getter/setter pair</div>


<p>Segments that routes will avoid going through.
Violations are reported as <a href="/sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This avoidance option is not supported in <code>IsolineOptions</code> for isoline calculation.</li>
<li>The engine does not support an unlimited number of segments to avoid.
The limit is defined by the HERE backend services and may change. For now,
the maximum number of segments to avoid should be below 250. This value may change
on the backend and it is therefore not guaranteed to be stable.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;SegmentReference&gt; segments;</code></pre>

 



</div>
`
}</HTMLBlock>
