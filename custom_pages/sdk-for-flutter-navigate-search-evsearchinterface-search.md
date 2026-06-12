---
title: "search abstract method"
slug: "sdk-for-flutter-navigate-search-evsearchinterface-search"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- search.html -->


<div>
<h1>search abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
search(<ol class="parameter-list single-line"> <li>List&lt;String&gt; ids, </li>
<li><a href="/sdk-for-flutter-navigate-search-evsearchcallback">EVSearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request for <a href="/sdk-for-flutter-navigate-search-evcharginglocation-class">EVChargingLocation</a> instances with given Place IDs.</p>
<ul>
<li>
<p><code>ids</code> List of charging location identifiers.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle search(List&lt;String&gt; ids, EVSearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
