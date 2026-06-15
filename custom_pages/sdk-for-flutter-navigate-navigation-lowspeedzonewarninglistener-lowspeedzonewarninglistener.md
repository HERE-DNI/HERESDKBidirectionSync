---
title: "LowSpeedZoneWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-lowspeedzonewarninglistener-lowspeedzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LowSpeedZoneWarningListener.html -->


<div>
<h1>LowSpeedZoneWarningListener constructor</h1></div>

LowSpeedZoneWarningListener(<ol class="parameter-list single-line"> <li>void onLowSpeedZoneWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-lowspeedzonewarning-class">LowSpeedZoneWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive low speed zone warnings.</p>
<p><strong>Note:</strong> This is currently available <em>only</em> for Japan.
The low speed zone warner is a zone warner, which means that for a low speed zone there will <em>always</em>
be 3 warnings emitted, with the <code>LowSpeedZoneWarning.distance_type</code> set to <code>DistanceType.AHEAD</code>, <code>DistanceType.REACHED</code>
and lastly <code>DistanceType.PASSED</code> when the end of the low speed zone is passed.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LowSpeedZoneWarningListener(
  void Function(LowSpeedZoneWarning) onLowSpeedZoneWarningUpdatedLambda,

) =&gt; LowSpeedZoneWarningListener$Lambdas(
  onLowSpeedZoneWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
