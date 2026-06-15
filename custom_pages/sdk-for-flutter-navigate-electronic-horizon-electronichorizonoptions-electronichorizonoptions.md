---
title: "ElectronicHorizonOptions constructor"
slug: "sdk-for-flutter-navigate-electronic-horizon-electronichorizonoptions-electronichorizonoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ElectronicHorizonOptions.html -->


<div>
<h1>ElectronicHorizonOptions constructor</h1></div>

ElectronicHorizonOptions(<ol class="parameter-list single-line"> <li>List&lt;double&gt; lookAheadDistancesInMeters, </li>
<li>double trailingDistanceInMeters</li>
</ol>)
    

<p>Creates a new instance.</p>
<p>Offline availability: This property is available online and offline.</p>
<ul>
<li><code>lookAheadDistancesInMeters</code> The ordered list of distances that define how far to look ahead in meters when calculating electronic horizon paths.
The first entry of the list is for the most preferred path, the second is for the side paths of the first level,
the third is for the side paths of the second level, and so on. Each entry defines how far ahead the path should be provided.
The valid number of values is from one to ten. Values beyond the tenth entry are removed from the list.
If the list is empty, a single default distance value is used instead.</li>
<li><code>trailingDistanceInMeters</code> The trailing distance of the electronic horizon path in meters.
Segments are removed from the path once they are passed and the distance to them exceeds this value.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ElectronicHorizonOptions(this.lookAheadDistancesInMeters, this.trailingDistanceInMeters);</code></pre>

 



</div>
`
}</HTMLBlock>
