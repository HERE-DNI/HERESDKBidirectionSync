---
title: "searchByPlaceId abstract method"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbyplaceid"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByPlaceId.html -->


<div>
<h1>searchByPlaceId abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByPlaceId(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-search-placeidquery-class">PlaceIdQuery</a> query, </li>
<li><a href="/sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>? languageCode, </li>
<li><a href="/sdk-for-flutter-navigate-search-placeidsearchcallback">PlaceIdSearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous search for a <a href="/sdk-for-flutter-navigate-search-place-class">Place</a> based on its ID and
<a href="/sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>.</p>
<ul>
<li>
<p><code>query</code> The id of place to search.</p>
</li>
<li>
<p><code>languageCode</code> The preferred language for the search results. When unset or unsupported language is chosen,
results will be returned in their local language.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByPlaceId(PlaceIdQuery query, LanguageCode? languageCode, PlaceIdSearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
