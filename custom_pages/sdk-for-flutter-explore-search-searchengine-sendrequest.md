---
title: "sendRequest abstract method"
slug: "sdk-for-flutter-explore-search-searchengine-sendrequest"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sendRequest.html -->


<div>
<h1>sendRequest abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
sendRequest(<ol class="parameter-list single-line"> <li>String href, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request by using the given href.</p>
<p>The href value can be obtained from <a href="/sdk-for-flutter-explore-search-suggestion-class">Suggestion</a> objects,
which are the result of successful call to <a href="/sdk-for-flutter-explore-search-searchengine-suggestextended">SearchEngine.suggestExtended</a>.
Currently supports only /v1/discover path.
Provides candidate places sorted by relevance.</p>
<ul>
<li>
<p><code>href</code> The direct link.</p>
</li>
<li>
<p><code>callback</code> Callback which receives result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle sendRequest(String href, SearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
