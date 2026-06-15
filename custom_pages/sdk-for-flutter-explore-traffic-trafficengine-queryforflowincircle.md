---
title: "queryForFlowInCircle abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-queryforflowincircle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- queryForFlowInCircle.html -->


<div>
<h1>queryForFlowInCircle abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
queryForFlowInCircle(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a> circleArea, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficflowqueryoptions-class">TrafficFlowQueryOptions</a> queryOptions, </li>
<li><a href="sdk-for-flutter-explore-traffic-trafficflowquerycallback">TrafficFlowQueryCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic flow using a circle as a filter.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>circleArea</code> The circle area to search for traffic flow.
The maximum radius of the circle filter is 50000 meters.</p>
</li>
<li>
<p><code>queryOptions</code> The options which are specific for flow query.</p>
</li>
<li>
<p><code>callback</code> It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle queryForFlowInCircle(GeoCircle circleArea, TrafficFlowQueryOptions queryOptions, TrafficFlowQueryCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
