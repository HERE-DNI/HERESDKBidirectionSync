---
title: "TaskHandle constructor"
slug: "sdk-for-flutter-explore-core-threading-taskhandle-taskhandle"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TaskHandle.html -->


<div>
<h1>TaskHandle constructor</h1></div>

TaskHandle(<ol class="parameter-list single-line"> <li>bool cancelLambda(), </li>
<li>bool isFinishedGetLambda(), </li>
<li>bool isCancelledGetLambda()</li>
</ol>)
    

<p>Handle used for the manipulation of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TaskHandle(
  bool Function() cancelLambda,
  bool Function() isFinishedGetLambda,
  bool Function() isCancelledGetLambda
) =&gt; TaskHandle$Lambdas(
  cancelLambda,
  isFinishedGetLambda,
  isCancelledGetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
