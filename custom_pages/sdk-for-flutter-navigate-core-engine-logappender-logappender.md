---
title: "LogAppender constructor"
slug: "sdk-for-flutter-navigate-core-engine-logappender-logappender"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LogAppender.html -->


<div>
<h1>LogAppender constructor</h1></div>

LogAppender(<ol class="parameter-list single-line"> <li>void logLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-engine-loglevel">LogLevel</a>, </li>
<li>String</li>
</ol>)</li>
</ol>)
    

<p>An interface to implement a listener to receive log messages.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LogAppender(
  void Function(LogLevel, String) logLambda,

) =&gt; LogAppender$Lambdas(
  logLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
