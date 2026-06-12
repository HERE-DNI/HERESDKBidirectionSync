---
title: "suggestByAddressElements abstract method"
slug: "sdk-for-flutter-navigate-search-offlinesearchengine-suggestbyaddresselements"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- suggestByAddressElements.html -->


<div>
<h1>suggestByAddressElements abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
suggestByAddressElements(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a> query, </li>
<li><a href="/sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="/sdk-for-flutter-navigate-search-suggestcallback">SuggestCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to suggest places for a <a href="/sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a> built with address elements and
returns candidate suggestions sorted by relevance.</p>
<p>For example, when user wants suggestions of type street for a text query <code>Invalidenstraße</code> in <code>Berlin</code>, it can be searched
by preparing <a href="/sdk-for-flutter-navigate-search-structuredquery-class">StructuredQuery</a> providing <a href="/sdk-for-flutter-navigate-search-structuredquery-query">StructuredQuery.query</a> as <code>Invalidenstraße</code>,
<a href="/sdk-for-flutter-navigate-search-structuredquery-areacenter">StructuredQuery.areaCenter</a>, <a href="/sdk-for-flutter-navigate-search-structuredqueryaddresselements-country">StructuredQueryAddressElements.country</a> as <code>Germany</code>,
<a href="/sdk-for-flutter-navigate-search-structuredqueryaddresselements-city">StructuredQueryAddressElements.city</a> as <code>Berlin</code> and <a href="/sdk-for-flutter-navigate-search-structuredqueryresulttype">StructuredQueryResultType</a> as <code>STREET</code>.
The suggestions will be presented only from the given geographical area.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>query</code> Desired structured query to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle suggestByAddressElements(StructuredQuery query, SearchOptions options, SuggestCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
