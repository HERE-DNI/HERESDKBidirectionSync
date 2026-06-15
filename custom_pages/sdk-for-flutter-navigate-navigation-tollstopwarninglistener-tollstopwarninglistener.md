---
title: "TollStopWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-tollstopwarninglistener-tollstopwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TollStopWarningListener.html -->


<div>
<h1>TollStopWarningListener constructor</h1></div>

TollStopWarningListener(<ol class="parameter-list single-line"> <li>void onTollStopWarningLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-tollstop-class">TollStop</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive information on the upcoming toll booth structure.</p>
<p>The warner might also warn about gates/checkpoints for vignette, border checkpoints
and similar structures on the street.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.
A <code>TollStop</code> will not be given until the previous warning of that type has been passed.
For example, a route with <code>TollStop</code> 120 meters and <code>TollStop</code> 160 meters ahead,
the first <code>TollStop.distance_to_toll_stop_in_meters</code> is 120 meters
and the next <code>TollStop.distance_to_toll_stop_in_meters</code> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TollStopWarningListener(
  void Function(TollStop) onTollStopWarningLambda,

) =&gt; TollStopWarningListener$Lambdas(
  onTollStopWarningLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
