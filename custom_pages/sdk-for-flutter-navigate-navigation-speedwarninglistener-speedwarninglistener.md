---
title: "SpeedWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-speedwarninglistener-speedwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedWarningListener.html -->


<div>
<h1>SpeedWarningListener constructor</h1></div>

SpeedWarningListener(<ol class="parameter-list single-line"> <li>void onSpeedWarningStatusChangedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-speedwarningstatus">SpeedWarningStatus</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications
when a speed limit on a road is exceeded or driving speed is restored back to normal.</p>
<p><strong>Note:</strong>
The warnings issued by this abstract class
don't take into account any temporary special speed limits. See <code>SpeedLimitListener</code>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SpeedWarningListener(
  void Function(SpeedWarningStatus) onSpeedWarningStatusChangedLambda,

) =&gt; SpeedWarningListener$Lambdas(
  onSpeedWarningStatusChangedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
