---
title: "SegmentReference constructor"
slug: "sdk-for-flutter-navigate-routing-segmentreference-segmentreference"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SegmentReference.html -->


<div>
<h1>SegmentReference constructor</h1></div>

SegmentReference([<ol class="parameter-list"> <li>String segmentId = "", </li>
<li><a href="sdk-for-flutter-navigate-routing-traveldirection">TravelDirection</a> travelDirection = TravelDirection.bidirectional, </li>
<li>double offsetStart = 0.0, </li>
<li>double offsetEnd = 1.0, </li>
<li>int tilePartitionId = 0, </li>
<li>int? localId = 0, </li>
</ol>])
    

<p>Creates a new instance.</p>
<ul>
<li><code>segmentId</code> Topology segment id representing a unique identifier within the HERE platform catalogs.</li>
<li><code>travelDirection</code> Travel direction of the segment.</li>
<li><code>offsetStart</code> The start offset is a non-negative number between 0 and 1, representing the start of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</li>
<li><code>offsetEnd</code> The end offset is a non-negative number between 0 and 1, representing the end of the referenced range using a proportion of the length of the segment. 0 represents the start and 1 the end of the segment, relative to the indicated direction (or positive direction in case of undirected segments)</li>
<li><code>tilePartitionId</code> HERE tile partition id (Morton-encoding + level indicator) of the segment.
As in HERE Map Content.</li>
<li><code>localId</code> Local ID of the segment inside the OCM tile.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentReference([String segmentId = "", TravelDirection travelDirection = TravelDirection.bidirectional, double offsetStart = 0.0, double offsetEnd = 1.0, int tilePartitionId = 0, int? localId = 0])
  : segmentId = segmentId, travelDirection = travelDirection, offsetStart = offsetStart, offsetEnd = offsetEnd, tilePartitionId = tilePartitionId, localId = localId;</code></pre>

 



</div>
`
}</HTMLBlock>
