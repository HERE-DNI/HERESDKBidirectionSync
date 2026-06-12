---
title: "TrafficIncidentLookupCallback typedef"
slug: "sdk-for-flutter-navigate-traffic-trafficincidentlookupcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficIncidentLookupCallback.html -->


<div>
<h1>TrafficIncidentLookupCallback typedef</h1></div>

TrafficIncidentLookupCallback =
     void Function(<a href="/sdk-for-flutter-navigate-traffic-trafficqueryerror">TrafficQueryError</a>? queryError, <a href="/sdk-for-flutter-navigate-traffic-trafficincident-class">TrafficIncident</a>? result)


<p>Callback passed to <a href="/sdk-for-flutter-navigate-traffic-trafficengine-lookupincident">TrafficEngine.lookupIncident</a>.</p>
<p>The method will be called on the main thread when a search call has been completed.
The first argument is the error in the case of the failure. It is <code>null</code> for an operation that succeeds.
The second argument is the incident in the case of the success. It is <code>null</code> in case of an error.</p>
<ul>
<li>
<p><code>queryError</code> The error in the case of the failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>result</code> The incident in the case of the success. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef TrafficIncidentLookupCallback = void Function(TrafficQueryError? queryError, TrafficIncident? result);</code></pre>

 



</div>
`
}</HTMLBlock>
