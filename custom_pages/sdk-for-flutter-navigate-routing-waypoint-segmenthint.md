---
title: "segmentHint property"
slug: "sdk-for-flutter-navigate-routing-waypoint-segmenthint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- segmentHint.html -->


<div>
<h1>segmentHint property</h1></div>

<a href="sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>?
        segmentHint
<div class="features">getter/setter pair</div>


<p>Optional segment hint causes the router to try and match to the specified segment.
Waypoint coordinates need to be on the segment, otherwise waypoint will be matched ignoring the segment hint.
This parameter can be used when the waypoint is too close to more than one segment to force matching to a specific one.
Only topology segment id and travel direction are used to define the segment hint</p>
<p><strong>Note:</strong>
The feature is not supported by the <code>OfflineRoutingEngine</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentReference? segmentHint;</code></pre>

 



</div>
`
}</HTMLBlock>
