---
title: "id property"
slug: "sdk-for-flutter-navigate-search-suggestion-id"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- id.html -->


<div>
<h1>id property</h1></div>
<section id="getter">

String?
id


<p>The unique id of suggested item. It can be used to query further information.
For online search, suggestion of type <a href="/sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.place</a>
will have Suggestion.id same as Place.id.
For offline search, only suggestion of type <a href="/sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.chain</a>,
will have this property filled with identifier number of an associated chain.
For example, the chain ID "8778" corresponds to the chain name "ABC Shop".
For other types, <a href="/sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.place</a> and <a href="/sdk-for-flutter-navigate-search-suggestiontype">SuggestionType.category</a>
this property will be null.
Gets the suggested item id.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">String? get id;</code></pre>

</section>
 



</div>
`
}</HTMLBlock>
