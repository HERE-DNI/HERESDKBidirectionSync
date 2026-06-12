---
title: "SchoolZoneWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-schoolzonewarninglistener-schoolzonewarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SchoolZoneWarningListener.html -->


<div>
<h1>SchoolZoneWarningListener constructor</h1></div>

SchoolZoneWarningListener(<ol class="parameter-list single-line"> <li>void onSchoolZoneWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-navigation-schoolzonewarning-class">SchoolZoneWarning</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive school zone warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SchoolZoneWarningListener(
  void Function(List&lt;SchoolZoneWarning&gt;) onSchoolZoneWarningUpdatedLambda,

) =&gt; SchoolZoneWarningListener$Lambdas(
  onSchoolZoneWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
