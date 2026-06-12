---
title: "NavigableLocationListener constructor"
slug: "sdk-for-flutter-navigate-navigation-navigablelocationlistener-navigablelocationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- NavigableLocationListener.html -->


<div>
<h1>NavigableLocationListener constructor</h1></div>

NavigableLocationListener(<ol class="parameter-list single-line"> <li>void onNavigableLocationUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-navigablelocation-class">NavigableLocation</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications
about the current location from <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory NavigableLocationListener(
  void Function(NavigableLocation) onNavigableLocationUpdatedLambda,

) =&gt; NavigableLocationListener$Lambdas(
  onNavigableLocationUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
