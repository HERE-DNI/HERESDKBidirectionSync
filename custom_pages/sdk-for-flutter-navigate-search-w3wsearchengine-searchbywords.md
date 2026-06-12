---
title: "searchByWords abstract method"
slug: "sdk-for-flutter-navigate-search-w3wsearchengine-searchbywords"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByWords.html -->


<div>
<h1>searchByWords abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByWords(<ol class="parameter-list single-line"> <li>String words, </li>
<li><a href="/sdk-for-flutter-navigate-search-w3wsearchcallback">W3WSearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for a <a href="/sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a> that corresponds to
the given 3 words.</p>
<ul>
<li>
<p><code>words</code> A 3 word address as a string. It must be three words separated with dots or
a japanese middle dot character (・). Words separated by spaces will be rejected.
Optionally, the 3 word address can be prefixed with ///.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that can be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByWords(String words, W3WSearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
