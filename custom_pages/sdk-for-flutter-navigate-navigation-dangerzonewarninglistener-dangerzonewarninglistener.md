---
title: "DangerZoneWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-dangerzonewarninglistener-dangerzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DangerZoneWarningListener.html -->


<div>
<h1>DangerZoneWarningListener constructor</h1></div>

DangerZoneWarningListener(<ol class="parameter-list single-line"> <li>void onDangerZoneWarningsUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-dangerzonewarning-class">DangerZoneWarning</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications about the Danger zones.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DangerZoneWarningListener(
  void Function(DangerZoneWarning) onDangerZoneWarningsUpdatedLambda,

) =&gt; DangerZoneWarningListener$Lambdas(
  onDangerZoneWarningsUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
