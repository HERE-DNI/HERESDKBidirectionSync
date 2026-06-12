---
title: "OffRoadProgressListener constructor"
slug: "sdk-for-flutter-navigate-navigation-offroadprogresslistener-offroadprogresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OffRoadProgressListener.html -->


<div>
<h1>OffRoadProgressListener constructor</h1></div>

OffRoadProgressListener(<ol class="parameter-list single-line"> <li>void onOffRoadProgressUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-offroadprogress-class">OffRoadProgress</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to
receive notifications about the current off-road location from <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory OffRoadProgressListener(
  void Function(OffRoadProgress) onOffRoadProgressUpdatedLambda,

) =&gt; OffRoadProgressListener$Lambdas(
  onOffRoadProgressUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
