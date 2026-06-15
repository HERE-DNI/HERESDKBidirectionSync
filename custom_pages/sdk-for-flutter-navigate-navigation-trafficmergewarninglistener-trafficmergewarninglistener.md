---
title: "TrafficMergeWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-trafficmergewarninglistener-trafficmergewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TrafficMergeWarningListener.html -->


<div>
<h1>TrafficMergeWarningListener constructor</h1></div>

TrafficMergeWarningListener(<ol class="parameter-list single-line"> <li>void onTrafficMergeWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-trafficmergewarning-class">TrafficMergeWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive traffic merge warnings.</p>
<p><strong>Note:</strong> The traffic merge warner is a point warner, which means that for a traffic merge there will <em>always</em> be
2 warnings emitted, with the <code>TrafficMergeWarning.distance_type</code> set to <code>DistanceType.AHEAD</code> and <code>DistanceType.PASSED</code>
which is given when the location of the traffic merge is reached.
A <code>TrafficMergeWarning</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TrafficMergeWarning</code> 120 meters and <code>TrafficMergeWarning</code> 160 meters ahead,
the first <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is 120 meters
and the next <code>TrafficMergeWarning.distance_to_traffic_merge_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TrafficMergeWarningListener(
  void Function(TrafficMergeWarning) onTrafficMergeWarningUpdatedLambda,

) =&gt; TrafficMergeWarningListener$Lambdas(
  onTrafficMergeWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
