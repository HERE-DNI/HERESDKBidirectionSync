---
title: "UsageStatsNetworkStats constructor"
slug: "sdk-for-flutter-explore-core-engine-usagestatsnetworkstats-usagestatsnetworkstats"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- UsageStatsNetworkStats.html -->


<div>
<h1>UsageStatsNetworkStats constructor</h1></div>

UsageStatsNetworkStats(<ol class="parameter-list"> <li>int sentBytes, </li>
<li>int receivedBytes, </li>
<li>String methodCall, </li>
<li>int requestCounter, </li>
</ol>)
    

<p>Creates a new instance.</p>
<ul>
<li><code>sentBytes</code> Number of bytes sent over the network.</li>
<li><code>receivedBytes</code> Number of bytes received from the network.</li>
<li><code>methodCall</code> Name or description of the method being called.</li>
<li><code>requestCounter</code> Amount of calls for particular family of methodCall.
methodCall in this case is considered as base request,
additional query params are ignored, all calculated as one request.
e.g. <a href="https://search.hereapi.com/someparams">https://search.hereapi.com/someparams</a> and <a href="https://search.hereapi.com/someparams2">https://search.hereapi.com/someparams2</a>
will be considered as 1 methodCall, and requestCounter is 2.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">UsageStatsNetworkStats(this.sentBytes, this.receivedBytes, this.methodCall, this.requestCounter);</code></pre>

 



</div>
`
}</HTMLBlock>
