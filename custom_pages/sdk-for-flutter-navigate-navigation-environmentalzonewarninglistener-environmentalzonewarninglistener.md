---
title: "EnvironmentalZoneWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-environmentalzonewarninglistener-environmentalzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EnvironmentalZoneWarningListener.html -->


<div>
<h1>EnvironmentalZoneWarningListener constructor</h1></div>

EnvironmentalZoneWarningListener(<ol class="parameter-list single-line"> <li>void onEnvironmentalZoneWarningsUpdatedLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-navigation-environmentalzonewarning-class">EnvironmentalZoneWarning</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications about the environmental zones.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory EnvironmentalZoneWarningListener(
  void Function(List&lt;EnvironmentalZoneWarning&gt;) onEnvironmentalZoneWarningsUpdatedLambda,

) =&gt; EnvironmentalZoneWarningListener$Lambdas(
  onEnvironmentalZoneWarningsUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
