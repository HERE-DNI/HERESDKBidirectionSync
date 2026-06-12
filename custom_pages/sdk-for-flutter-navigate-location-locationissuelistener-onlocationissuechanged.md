---
title: "onLocationIssueChanged abstract method"
slug: "sdk-for-flutter-navigate-location-locationissuelistener-onlocationissuechanged"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onLocationIssueChanged.html -->


<div>
<h1>onLocationIssueChanged abstract method</h1></div>

void
onLocationIssueChanged(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-location-locationissuetype">LocationIssueType</a>&gt; issues</li>
</ol>)

      

    

<p>Called when the snapshot of currently active location issues changes.</p>
<p>Invoked whenever the LocationEngine detects a change in the set of active issues,
including when all issues clear (empty list). Replace any previously stored issue
list with this snapshot.</p>
<ul>
<li><code>issues</code> Current snapshot of active location issues. Empty list indicates no active issues.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onLocationIssueChanged(List&lt;LocationIssueType&gt; issues);</code></pre>

 



</div>
`
}</HTMLBlock>
