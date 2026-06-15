---
title: "cancel abstract method"
slug: "sdk-for-flutter-explore-core-threading-taskhandle-cancel"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cancel.html -->


<div>
<h1>cancel abstract method</h1></div>

bool
cancel()

      

    

<p>Sets internal state of task to 'canceled'.</p>
<p>If the task is still in the queue, it will be
removed from it immediately. However, if the task is in a running state, it will nevertheless be completed, as there is no way
to interrupt it.</p>
<p>Returns <code>bool</code>. True, if the task was canceled.</p>
<p>False, if the task can't be canceled due to a
platform dependent reason.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool cancel();</code></pre>

 



</div>
`
}</HTMLBlock>
