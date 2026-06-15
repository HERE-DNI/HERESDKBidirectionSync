---
title: "segment property"
slug: "sdk-for-flutter-navigate-routing-maxspeedonsegment-segment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- segment.html -->


<div>
<h1>segment property</h1></div>

<a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>
segment
<div class="features">getter/setter pair</div>


<p>A segment for which the new base speed is specified. Only the <code>segmendId</code> and <code>travelDirection</code>
parameters are used, other parameters are ignored. Setting a <code>segmendId</code> is mandatory.</p>
<p><strong>Note:</strong> The <code>SegmentReference</code> is not directly accessible from the map via the HERE SDK.
Although, after route calculation you can retrieve the related segments for each <a href="sdk-for-flutter-navigate-routing-span-class">Span</a>.
The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>.
These IDs are mostly stable and only change when the underlying map data changes
due to a new road or similar changes in the real world.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentReference segment;</code></pre>

 



</div>
`
}</HTMLBlock>
