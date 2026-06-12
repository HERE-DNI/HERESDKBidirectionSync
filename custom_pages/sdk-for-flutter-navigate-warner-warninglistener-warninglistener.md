---
title: "WarningListener constructor"
slug: "sdk-for-flutter-navigate-warner-warninglistener-warninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- WarningListener.html -->


<div>
<h1>WarningListener constructor</h1></div>

WarningListener(<ol class="parameter-list single-line"> <li>void onWarningsLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-warner-warning-class">Warning</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>A generic listener interface abstract class for receiving warning notifications.</p>
<p>Implementations of this interface are notified whenever the <code>WarnerEngine</code> detects new warnings.
The listener receives a list of <code>Warning</code> objects, each describing a specific event or condition that requires user attention.</p>
<p>Classes interested in warning updates should implement this listener
and register themselves via <code>WarnerEngine.addWarningListener</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory WarningListener(
  void Function(List&lt;Warning&gt;) onWarningsLambda,

) =&gt; WarningListener$Lambdas(
  onWarningsLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
