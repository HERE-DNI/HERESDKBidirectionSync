---
title: "searchByPickedPlace abstract method"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbypickedplace"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByPickedPlace.html -->


<div>
<h1>searchByPickedPlace abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByPickedPlace(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a> pickedPlace, </li>
<li><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a>? languageCode, </li>
<li><a href="sdk-for-flutter-navigate-search-placeidsearchcallback">PlaceIdSearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous search for a <a href="sdk-for-flutter-navigate-search-place-class">Place</a> based on the content found in <a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a>.</p>
<p>If <a href="sdk-for-flutter-navigate-core-pickedplace-class">PickedPlace</a> data is obtained from the offline map, it may happen that the newer version
that is used by the online service represented by <code>SearchEngine</code> no longer contains the
related POI. In that case, <a href="sdk-for-flutter-navigate-search-searcherror">SearchError.noResultsFound</a> error is reported.
When that happens, you may try to obtain the POI from the offline map by calling
<code>OfflineSearchEngine.searchByPickedPlace</code>, only available for the Navigate license.</p>
<ul>
<li>
<p><code>pickedPlace</code> The content picked from map.</p>
</li>
<li>
<p><code>languageCode</code> The preferred language for the search result. When unset or unsupported language is chosen,
result will be returned in the local language.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByPickedPlace(PickedPlace pickedPlace, LanguageCode? languageCode, PlaceIdSearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
