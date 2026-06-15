---
title: "MaxSpeedOnSegment constructor"
slug: "sdk-for-flutter-explore-routing-maxspeedonsegment-maxspeedonsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MaxSpeedOnSegment.html -->


<div>
<h1>MaxSpeedOnSegment constructor</h1></div>

MaxSpeedOnSegment(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-routing-segmentreference-class">SegmentReference</a> segment, </li>
<li>double baseSpeedInMetersPerSecond</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>segment</code> A segment for which the new base speed is specified. Only the <code>segmendId</code> and <code>travelDirection</code>
parameters are used, other parameters are ignored. Setting a <code>segmendId</code> is mandatory.</li>
</ul>
<p><strong>Note:</strong> The <code>SegmentReference</code> is not directly accessible from the map via the HERE SDK.
Although, after route calculation you can retrieve the related segments for each <a href="sdk-for-flutter-explore-routing-span-class">Span</a>.
The segment IDs are the same that are also used by, for example, the <a href="https://www.here.com/docs/bundle/routing-api-developer-guide-v8/page/topics/use-cases/avoid-segments.html">Routing REST API</a>.
These IDs are mostly stable and only change when the underlying map data changes
due to a new road or similar changes in the real world.</p>
<ul>
<li><code>baseSpeedInMetersPerSecond</code> New maximum value in m/s of baseSpeed on segment.  The provided value must be in the range [1.0, 70.0].
Cannot increase base speed on segment. If the value is greater than the default base speed, then such penalty will have no effect.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MaxSpeedOnSegment(this.segment, this.baseSpeedInMetersPerSecond);</code></pre>

 



</div>
`
}</HTMLBlock>
