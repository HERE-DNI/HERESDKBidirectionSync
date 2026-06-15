---
title: "MatchedLocationListener constructor"
slug: "sdk-for-flutter-navigate-mapmatcher-matchedlocationlistener-matchedlocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MatchedLocationListener.html -->


<div>
<h1>MatchedLocationListener constructor</h1></div>

MatchedLocationListener(<ol class="parameter-list single-line"> <li>void onMatchedLocationUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapmatcher-matchedlocation-class">MatchedLocation</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented to receive notifications
about the current location from <a href="sdk-for-flutter-navigate-navigation-mapmatchedlocation-class">MapMatchedLocation</a>.</p>
<p><strong>Note:</strong> This is a <strong>beta</strong> release of this feature. There may be bugs and unexpected
behaviors. Related APIs may change in future releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MatchedLocationListener(
  void Function(MatchedLocation) onMatchedLocationUpdatedLambda,

) =&gt; MatchedLocationListener$Lambdas(
  onMatchedLocationUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
