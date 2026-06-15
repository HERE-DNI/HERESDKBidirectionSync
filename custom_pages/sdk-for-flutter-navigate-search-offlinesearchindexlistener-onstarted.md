---
title: "onStarted abstract method"
slug: "sdk-for-flutter-navigate-search-offlinesearchindexlistener-onstarted"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onStarted.html -->


<div>
<h1>onStarted abstract method</h1></div>

void
onStarted(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-search-offlinesearchindexoperation">OfflineSearchIndexOperation</a> operation</li>
</ol>)

      

    

<p>Called each time that the indexing has started.</p>
<p>It is triggered by changes to persistent map
or by calling <code>OfflineSearchEngine.setIndexOptions</code>.
If a valid index was previously created for the installed regions, no additional indexing
is performed, so no notifications are sent. In this context, a valid index is the one
that contains data for the exact versions of the installed map regions. When any of them
is updated or new regions are downloaded or deleted, the index becomes invalid and is
automatically rebuilt, as long as indexing has been enabled previously.
Invoked on the main thread.</p>
<ul>
<li><code>operation</code> Shows whether the index is being created or removed.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onStarted(OfflineSearchIndexOperation operation);</code></pre>

 



</div>
`
}</HTMLBlock>
