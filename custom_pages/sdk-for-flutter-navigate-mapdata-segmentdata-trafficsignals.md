---
title: "trafficSignals property"
slug: "sdk-for-flutter-navigate-mapdata-segmentdata-trafficsignals"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- trafficSignals.html -->


<div>
<h1>trafficSignals property</h1></div>
<section id="getter">

List&lt;<a href="/sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a>&gt;?
trafficSignals


<p>The list of <a href="/sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a> of the given segment.
Returns an empty list if no data is found.
Returns <code>null</code> if <a href="/sdk-for-flutter-navigate-mapdata-segmentdataloaderoptions-loadtrafficsignals">SegmentDataLoaderOptions.loadTrafficSignals</a> is set to <code>false</code>.
The <a href="/sdk-for-flutter-navigate-mapdata-trafficsignallocation">TrafficSignalLocation</a> indicates the location of a single traffic signal, which can be any combination of left, right and overhead.
The <a href="/sdk-for-flutter-navigate-mapdata-trafficsignal-offsetinmeters">TrafficSignal.offsetInMeters</a> is the location along the segment,
while the traffic signal location have details on how the traffic signal is display/deploy in that specific location in the segment.
Gets the list of <a href="/sdk-for-flutter-navigate-mapdata-trafficsignal-class">TrafficSignal</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;TrafficSignal&gt;? get trafficSignals;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
