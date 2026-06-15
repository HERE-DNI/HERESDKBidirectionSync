---
title: "queryForFlowInCorridor abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforflowincorridor"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForFlowInCorridor.html -->


<div>
<h1>queryForFlowInCorridor abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
queryForFlowInCorridor(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a> corridorArea, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a> queryOptions, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic flow by a corridor as a filter.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li><code>corridorArea</code> The corridor box to search for traffic flow.
The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.</li>
</ul>
<p>Maximum number of points in the corridor is 300.</p>
<p>To reduce number of points in the corridor use <a href="sdk-for-flutter-explore-core-polylinesimplifier-class">PolylineSimplifier</a>.</p>
<p>If no <code>GeoCorridor.half_width_in_meters</code> is specified, the default value is used. The default value is 30 meters.</p>
<ul>
<li>
<p><code>queryOptions</code> The options which are specific for flow query.</p>
</li>
<li>
<p><code>callback</code> It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle queryForFlowInCorridor(GeoCorridor corridorArea, TrafficFlowQueryOptions queryOptions, TrafficFlowQueryCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
