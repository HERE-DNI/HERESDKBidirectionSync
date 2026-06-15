---
title: "searchByPlaceIdWithLanguageCodeExtended abstract method"
slug: "sdk-for-flutter-explore-search-searchengine-searchbyplaceidwithlanguagecodeextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByPlaceIdWithLanguageCodeExtended.html -->


<div>
<h1>searchByPlaceIdWithLanguageCodeExtended abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
searchByPlaceIdWithLanguageCodeExtended(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a> query, </li>
<li><a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>? languageCode, </li>
<li><a href="sdk-for-flutter-explore-search-placeidsearchcallbackextended">PlaceIdSearchCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for a <a href="sdk-for-flutter-explore-search-place-class">Place</a> based on its ID and
<a href="sdk-for-flutter-explore-core-languagecode">LanguageCode</a>.</p>
<ul>
<li>
<p><code>query</code> The id of place to search.</p>
</li>
<li>
<p><code>languageCode</code> The preferred language for the search results. When unset or unsupported language is
chosen, results will be returned in their local language.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByPlaceIdWithLanguageCodeExtended(PlaceIdQuery query, LanguageCode? languageCode, PlaceIdSearchCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
