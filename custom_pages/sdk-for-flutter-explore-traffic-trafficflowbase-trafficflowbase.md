---
title: "TrafficFlowBase constructor"
slug: "sdk-for-flutter-explore-traffic-trafficflowbase-trafficflowbase"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficFlowBase.html -->


<div>
<h1>TrafficFlowBase constructor</h1></div>

TrafficFlowBase(<ol class="parameter-list single-line"> <li>double freeFlowSpeedInMetersPerSecondGetLambda(), </li>
<li>double jamFactorGetLambda()</li>
</ol>)
    

<p>This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TrafficFlowBase(
  double Function() freeFlowSpeedInMetersPerSecondGetLambda,
  double Function() jamFactorGetLambda
) =&gt; TrafficFlowBase$Lambdas(
  freeFlowSpeedInMetersPerSecondGetLambda,
  jamFactorGetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
