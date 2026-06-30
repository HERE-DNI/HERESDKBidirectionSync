---
title: "Suggestion (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-suggestion"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- Suggestion.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.search</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.search.Suggestion</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">Suggestion</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel".
 Represents a relevant response to user queries.
 Suggestions (please check <a href="sdk-for-android-explore-com-here-sdk-search-suggestiontype" title="enum class in com.here.sdk.search"><code>SuggestionType</code></a>) are either:
 Place: <a href="sdk-for-android-explore-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a>
 Query: <a href="sdk-for-android-explore-suggestiontype#CHAIN"><code>SuggestionType.CHAIN</code></a> or <a href="sdk-for-android-explore-suggestiontype#CATEGORY"><code>SuggestionType.CATEGORY</code></a>
With "Place" you get data for a concrete place in the world.
 With "Query" something to follow-up, a way to perform more focused search.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-search-highlighttype" title="enum class in com.here.sdk.search">HighlightType</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-search-indexrange" title="class in com.here.sdk.search">IndexRange</a>&gt;&gt;</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-suggestion#getHighlights()">getHighlights</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">The text slices matching the input query.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-suggestion#getHref()">getHref</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the direct link for Discover query.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-suggestion#getId()">getId</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the suggested item id.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-search-place" title="class in com.here.sdk.search">Place</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-suggestion#getPlace()">getPlace</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the suggested place item.</div>
</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-suggestion#getTitle()">getTitle</a>()</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the localized title for the suggestion.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-search-suggestiontype" title="enum class in com.here.sdk.search">SuggestionType</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-search-suggestion#getType()">getType</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Gets the type of suggestion.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="getHighlights()">
<h3>getHighlights</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-search-highlighttype" title="enum class in com.here.sdk.search">HighlightType</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-com-here-sdk-search-indexrange" title="class in com.here.sdk.search">IndexRange</a>&gt;&gt;</span> <span class="element-name">getHighlights</span>()</div>
<div class="block"><p>The text slices matching the input query.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Associated container where <a href="sdk-for-android-explore-com-here-sdk-search-highlighttype" title="enum class in com.here.sdk.search"><code>HighlightType</code></a> is a key and list of <a href="sdk-for-android-explore-com-here-sdk-search-indexrange" title="class in com.here.sdk.search"><code>IndexRange</code></a> value.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getTitle()">
<h3>getTitle</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getTitle</span>()</div>
<div class="block"><p>Gets the localized title for the suggestion.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The localized title for the suggestion.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getType()">
<h3>getType</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-search-suggestiontype" title="enum class in com.here.sdk.search">SuggestionType</a></span> <span class="element-name">getType</span>()</div>
<div class="block"><p>Gets the type of suggestion.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Type of the suggestion.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getPlace()">
<h3>getPlace</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-search-place" title="class in com.here.sdk.search">Place</a></span> <span class="element-name">getPlace</span>()</div>
<div class="block"><p>Gets the suggested place item.
 Available only for <a href="sdk-for-android-explore-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a>.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The suggested place.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getId()">
<h3>getId</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getId</span>()</div>
<div class="block"><p>Gets the suggested item id.
 For online search, suggestion of type <a href="sdk-for-android-explore-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a>
 will have Suggestion.id same as Place.id.
 For offline search, only suggestion of type <a href="sdk-for-android-explore-suggestiontype#CHAIN"><code>SuggestionType.CHAIN</code></a>,
 will have this property filled with identifier number of an associated chain.
 For example, the chain ID "8778" corresponds to the chain name "ABC Shop".
 For other types, <a href="sdk-for-android-explore-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a> and <a href="sdk-for-android-explore-suggestiontype#CATEGORY"><code>SuggestionType.CATEGORY</code></a>
 this property will be null.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>The unique id of suggested item. It can be used to query further information.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getHref()">
<h3>getHref</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span class="element-name">getHref</span>()</div>
<div class="block"><p>Gets the direct link for Discover query.
 Available only for <a href="sdk-for-android-explore-suggestiontype#CHAIN"><code>SuggestionType.CHAIN</code></a> and <a href="sdk-for-android-explore-suggestiontype#CATEGORY"><code>SuggestionType.CATEGORY</code></a>.
 This is not supported in offline search.</p></div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Direct URL for precise query.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
