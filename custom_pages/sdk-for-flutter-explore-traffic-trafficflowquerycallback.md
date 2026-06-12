---
title: "TrafficFlowQueryCallback typedef"
slug: "sdk-for-flutter-explore-traffic-trafficflowquerycallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficFlowQueryCallback.html -->


<div>
<h1>TrafficFlowQueryCallback typedef</h1></div>

TrafficFlowQueryCallback =
     void Function(<a href="/sdk-for-flutter-explore-traffic-trafficqueryerror">TrafficQueryError</a>? queryError, List&lt;<a href="/sdk-for-flutter-explore-traffic-trafficflow-class">TrafficFlow</a>&gt;? result)


<p>Callback passed to following functions:
<a href="/sdk-for-flutter-explore-traffic-trafficengine-queryforflowinbox">TrafficEngine.queryForFlowInBox</a>
<a href="/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle">TrafficEngine.queryForFlowInCircle</a>
<a href="/sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor">TrafficEngine.queryForFlowInCorridor</a>
The method will be called on the main thread when a search call has been completed.</p>
<p>The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
The second argument is the list of flow items in the case of the success. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>queryError</code> The error in the case of the failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>result</code> The list of incidents in the case of the success. It is <code>null</code> in case of an error.</p>
</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef TrafficFlowQueryCallback = void Function(TrafficQueryError? queryError, List&lt;TrafficFlow&gt;? result);</code></pre>

 



</div>
`
}</HTMLBlock>
