---
title: "roadSignSegment property"
slug: "sdk-for-flutter-navigate-navigation-roadsignwarning-roadsignsegment"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- roadSignSegment.html -->


<div>
<h1>roadSignSegment property</h1></div>

<a href="/sdk-for-flutter-navigate-routing-segmentreference-class">SegmentReference</a>
roadSignSegment
<div class="features">getter/setter pair</div>


<p>The reference to the segment where the road sign is located. It can be used to identify the
location of the road sign.
It allows to compare the road sign location with the <code>MapMatchedLocation.segment_reference</code>
provided by the <code>NavigableLocationListener</code> or with the <a href="/sdk-for-flutter-navigate-routing-span-segmentreference">Span.segmentReference</a>
available in the Route's Span.
By combining it with the geometry of the segment, that can be loaded using
<a href="/sdk-for-flutter-navigate-mapdata-segmentdataloader-class">SegmentDataLoader</a>, it is possible to identify the road sign's coordinates.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">SegmentReference roadSignSegment;</code></pre>

 



</div>
`
}</HTMLBlock>
