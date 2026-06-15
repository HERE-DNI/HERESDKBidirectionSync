---
title: "TrafficLocation constructor"
slug: "sdk-for-flutter-explore-traffic-trafficlocation-trafficlocation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficLocation.html -->


<div>
<h1>TrafficLocation constructor</h1></div>

TrafficLocation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a> polyline, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-core-geopolyline-class">GeoPolyline</a>&gt; additionalPolylines, </li>
<li>int lengthInMeters</li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>polyline</code> The polyline representing the traffic entity shape.
The current field contains a continuous polyline with no gaps between geo-coordinates.
All others following the gap are present in the <code>additional_polylines</code> field.</li>
<li><code>additionalPolylines</code> List of polylines that were not included in continuous polyline.
Use this to fill any gaps in the continuous polyline.</li>
<li><code>lengthInMeters</code> The affected road length in meters.
The length can be 0 only if the incident supplier has provided incomplete data.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TrafficLocation(this.polyline, this.additionalPolylines, this.lengthInMeters)
    : description = "";</code></pre>

 



</div>
`
}</HTMLBlock>
