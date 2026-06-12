---
title: "RealisticViewWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-realisticviewwarninglistener-realisticviewwarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RealisticViewWarningListener.html -->


<div>
<h1>RealisticViewWarningListener constructor</h1></div>

RealisticViewWarningListener(<ol class="parameter-list single-line"> <li>void onRealisticViewWarningUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive realistic view warnings.</p>
<p>A <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> will not be given until the previous warning of that type has been passed.
For example, a route with <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 120 meters and <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-class">RealisticViewWarning</a> 160 meters ahead,
the first <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is 120 meters
and the next <a href="/sdk-for-flutter-navigate-navigation-realisticviewwarning-distancetorealisticviewinmeters">RealisticViewWarning.distanceToRealisticViewInMeters</a> is then 40 meters,
since that is the distance between the first and second warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RealisticViewWarningListener(
  void Function(RealisticViewWarning) onRealisticViewWarningUpdatedLambda,

) =&gt; RealisticViewWarningListener$Lambdas(
  onRealisticViewWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
