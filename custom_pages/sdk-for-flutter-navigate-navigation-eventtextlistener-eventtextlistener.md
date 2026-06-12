---
title: "EventTextListener constructor"
slug: "sdk-for-flutter-navigate-navigation-eventtextlistener-eventtextlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EventTextListener.html -->


<div>
<h1>EventTextListener constructor</h1></div>

EventTextListener(<ol class="parameter-list single-line"> <li>void onEventTextUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-eventtext-class">EventText</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications
when text notifications are available from <a href="/sdk-for-flutter-navigate-navigation-navigator-class">Navigator</a>.</p>
<p>Multiple notifications
can be given for the same maneuver at different distances.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory EventTextListener(
  void Function(EventText) onEventTextUpdatedLambda,

) =&gt; EventTextListener$Lambdas(
  onEventTextUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
