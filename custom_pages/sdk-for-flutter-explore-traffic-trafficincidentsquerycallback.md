---
title: "TrafficIncidentsQueryCallback typedef"
slug: "sdk-for-flutter-explore-traffic-trafficincidentsquerycallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentsQueryCallback.html -->


<div>
<h1>TrafficIncidentsQueryCallback typedef</h1></div>

TrafficIncidentsQueryCallback =
     void Function(<a href="/sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a>? queryError, List&lt;<a href="/sdk-for-flutter-explore-traffic-trafficincident-class">TrafficIncident</a>&gt;? result)


<p>Callback passed to <a href="/sdk-for-flutter-explore-traffic-trafficengine-queryforincidentsincorridor">TrafficEngine.queryForIncidentsInCorridor</a>.</p>
<p>The method will be called on the main thread when a search call has been completed.
The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
The second argument is the list of incidents in the case of the success. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>queryError</code> The error in the case of the failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>result</code> The list of incidents in the case of the success. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef TrafficIncidentsQueryCallback = void Function(TrafficQueryError? queryError, List&lt;TrafficIncident&gt;? result);</code></pre>

 



</div>
`
}</HTMLBlock>
