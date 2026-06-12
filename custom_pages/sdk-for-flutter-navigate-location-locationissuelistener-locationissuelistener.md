---
title: "LocationIssueListener constructor"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-locationissuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationIssueListener.html -->


<div>
<h1>LocationIssueListener constructor</h1></div>

LocationIssueListener(<ol class="parameter-list single-line"> <li>void onLocationIssueChangedLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>abstract class receiving notifications when the set of
currently active location issues changes.</p>
<p>Location issues represent unexpected or degraded conditions affecting positioning quality,
availability, or functionality. The LocationEngine monitors various positioning subsystems
and aggregates detected issues into a unified snapshot delivered via this interface.</p>
<ul>
<li>Each callback delivers the complete current set of active issues.</li>
<li>An empty list indicates all previously reported issues have cleared.</li>
<li>Issues are transient by design and automatically removed once underlying conditions improve.
No explicit clear/dismiss API is provided.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LocationIssueListener(
  void Function(List&lt;LocationIssueType&gt;) onLocationIssueChangedLambda,

) =&gt; LocationIssueListener$Lambdas(
  onLocationIssueChangedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
