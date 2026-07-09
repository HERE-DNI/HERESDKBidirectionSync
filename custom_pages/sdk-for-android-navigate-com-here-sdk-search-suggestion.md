---
title: "Suggestion (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-search-suggestion"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- Suggestion.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.search</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.search.Suggestion</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">Suggestion</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>Suggestion is meant to provide relevant suggestions to partial queries, like "restaur", "starbu", "eiffel".
 Represents a relevant response to user queries.
 Suggestions (please check <a href="sdk-for-android-navigate-com-here-sdk-search-suggestiontype" title="enum class in com.here.sdk.search"><code>SuggestionType</code></a>) are either:
 Place: <a href="sdk-for-android-navigate-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a>
 Query: <a href="sdk-for-android-navigate-suggestiontype#CHAIN"><code>SuggestionType.CHAIN</code></a> or <a href="sdk-for-android-navigate-suggestiontype#CATEGORY"><code>SuggestionType.CATEGORY</code></a>
With "Place" you get data for a concrete place in the world.
 With "Query" something to follow-up, a way to perform more focused search.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="getHighlights()">
<h3>getHighlights</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-highlighttype" title="enum class in com.here.sdk.search">HighlightType</a>,<wbr/><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-navigate-com-here-sdk-search-indexrange" title="class in com.here.sdk.search">IndexRange</a>&gt;&gt;</span> <span className="element-name">getHighlights</span>()</div>
<div className="block"><p>The text slices matching the input query.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Associated container where <a href="sdk-for-android-navigate-com-here-sdk-search-highlighttype" title="enum class in com.here.sdk.search"><code>HighlightType</code></a> is a key and list of <a href="sdk-for-android-navigate-com-here-sdk-search-indexrange" title="class in com.here.sdk.search"><code>IndexRange</code></a> value.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getTitle()">
<h3>getTitle</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getTitle</span>()</div>
<div className="block"><p>Gets the localized title for the suggestion.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The localized title for the suggestion.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getType()">
<h3>getType</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-suggestiontype" title="enum class in com.here.sdk.search">SuggestionType</a></span> <span className="element-name">getType</span>()</div>
<div className="block"><p>Gets the type of suggestion.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>Type of the suggestion.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getPlace()">
<h3>getPlace</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-search-place" title="class in com.here.sdk.search">Place</a></span> <span className="element-name">getPlace</span>()</div>
<div className="block"><p>Gets the suggested place item.
 Available only for <a href="sdk-for-android-navigate-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a>.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The suggested place.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getId()">
<h3>getId</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getId</span>()</div>
<div className="block"><p>Gets the suggested item id.
 For online search, suggestion of type <a href="sdk-for-android-navigate-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a>
 will have Suggestion.id same as Place.id.
 For offline search, only suggestion of type <a href="sdk-for-android-navigate-suggestiontype#CHAIN"><code>SuggestionType.CHAIN</code></a>,
 will have this property filled with identifier number of an associated chain.
 For example, the chain ID "8778" corresponds to the chain name "ABC Shop".
 For other types, <a href="sdk-for-android-navigate-suggestiontype#PLACE"><code>SuggestionType.PLACE</code></a> and <a href="sdk-for-android-navigate-suggestiontype#CATEGORY"><code>SuggestionType.CATEGORY</code></a>
 this property will be null.</p></div>
<dl className="notes">
<dt>Returns:</dt>
<dd><p>The unique id of suggested item. It can be used to query further information.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getHref()">
<h3>getHref</h3>
<div className="member-signature"><span className="annotations">@Nullable
</span><span className="modifiers">public</span> <span className="return-type"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" title="class or interface in java.lang">String</a></span> <span className="element-name">getHref</span>()</div>
<div className="block"><p>Gets the direct link for Discover query.
 Available only for <a href="sdk-for-android-navigate-suggestiontype#CHAIN"><code>SuggestionType.CHAIN</code></a> and <a href="sdk-for-android-navigate-suggestiontype#CATEGORY"><code>SuggestionType.CATEGORY</code></a>.
 This is not supported in offline search.</p></div>
<dl className="notes">
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
