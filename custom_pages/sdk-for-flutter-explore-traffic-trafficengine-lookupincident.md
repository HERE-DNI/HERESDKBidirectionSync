---
title: "lookupIncident abstract method"
slug: "sdk-for-flutter-explore-traffic-trafficengine-lookupincident"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookupIncident.html -->


<div>
<h1>lookupIncident abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
lookupIncident(<ol class="parameter-list single-line"> <li>String originalId, </li>
<li><a href="/sdk-for-flutter-explore-traffic-trafficincidentlookupoptions-class">TrafficIncidentLookupOptions</a> lookupOptions, </li>
<li><a href="/sdk-for-flutter-explore-traffic-trafficincidentlookupcallback">TrafficIncidentLookupCallback</a> callback</li>
</ol>)

      

    

<p>Asynchronously queries for traffic incident by the original id.</p>
<p>See <a href="/sdk-for-flutter-explore-traffic-trafficincident-originalid">TrafficIncident.originalId</a> for more information.</p>
<ul>
<li>
<p><code>originalId</code> The requested incident original id.</p>
</li>
<li>
<p><code>lookupOptions</code> The options which are specific for the incident lookup query.</p>
</li>
<li>
<p><code>callback</code> The callback object that will be invoked after the incident lookup query.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle lookupIncident(String originalId, TrafficIncidentLookupOptions lookupOptions, TrafficIncidentLookupCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
