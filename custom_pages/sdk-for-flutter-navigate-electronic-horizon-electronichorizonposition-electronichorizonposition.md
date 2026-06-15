---
title: "ElectronicHorizonPosition constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonposition-electronichorizonposition"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonPosition.html -->


<div>
<h1>ElectronicHorizonPosition constructor</h1></div>

ElectronicHorizonPosition(<ol class="parameter-list single-line"> <li>int pathIndex, </li>
<li>int pathSegmentIndex, </li>
<li>double pathSegmentOffsetInMeters</li>
</ol>)
    

<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
<ul>
<li><code>pathIndex</code> The index of the current path in the list of <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizon-paths">ElectronicHorizon.paths</a>.</li>
<li><code>pathSegmentIndex</code> The index of the segment inside the <a href="sdk-for-flutter-navigate-electronic-horizon-electronichorizonpath-segments">ElectronicHorizonPath.segments</a>.</li>
<li><code>pathSegmentOffsetInMeters</code> The offset from the start of the segment in meters.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ElectronicHorizonPosition(this.pathIndex, this.pathSegmentIndex, this.pathSegmentOffsetInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
